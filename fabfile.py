# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function  # python3
from __future__ import unicode_literals, division  # python3
from os import path
from sets import Set
from StringIO import StringIO
from fabric.api import env, local, run, get, parallel, put
from fabric.decorators import runs_once
from project import settings_local

env.roledefs = settings_local.roledefs
env.forward_agent = True
env.user = settings_local.SSH_USER

servers = settings_local.servers
local_django_project = path.realpath(path.dirname(__file__))


@parallel
def update():
    local_paths = {
        'project': local_django_project
    }
    server = servers[env.host_string]
    # check / update requirements
    run('echo "* git update"')
    git_output = run('cd {path} && git pull'.format(**server))
    print(git_output)
    new_requirements = StringIO()
    current_requirements = run('{activate} && pip freeze'.format(**server))
    current_requirements = [
        r.strip() for r in current_requirements.split("\n")
    ]
    get("{path}/requirements.txt".format(**server), new_requirements)
    new_requirements.seek(0)
    new_requirements = [
        r.strip() for r in new_requirements.readlines() if r[0] != "#"
    ]

    if env_needs_update(current_requirements, new_requirements):
        run('''{activate} && pip install -q -r \
               {path}/requirements.txt'''.format(**server))
        run('''{activate} && ./manage.py syncdb && \
               ./manage.py migrate'''.format(**server))
    else:
        if any(["/migrations/" in l for l in git_output]):
            run('{activate} && ./manage.py migrate'.format(**server))

    # collect static & restart
    run('{activate} && ./manage.py collectstatic --noinput'.format(**server))
    run('touch {path}/project/uwsgi.ini'.format(**server))


def env_needs_update(current, new):
    new_req, current_req = Set(new), Set(current)
    needs_update = not new_req.issubset(current_req)
    if needs_update:
        print("This requirements changed:", new_req - current_req)
    return needs_update


def fix_req_github(requirements):
    # fix github branch problems with - in name
    for r in requirements:
        if "-origin/" in r:
            r = r.replace("-origin/", "_")
    return requirements


def update_req():
    # check / update requirements
    current_requirements = local("pip freeze", capture=True).split("\n")
    current_requirements = fix_req_github(current_requirements)
    with open("requirements.txt") as f:
        new_requirements = [r.strip() for r in f.readlines() if r[0] != "#"]
        new_requirements = fix_req_github(new_requirements)
    if env_needs_update(current_requirements, new_requirements):
        print("updating requirements")
        local("pip install -q -r requirements.txt")
        local("./manage.py syncdb && ./manage.py migrate")


def update_local():
    # update code git or svn
    if path.exists("/.git"):
        if local("git status", capture=True).count("working directory clean"):
            local("git pull", capture=False)
        else:
            local("git stash save -q hjupdatetemp && git pull && git stash pop -q", capture=False)
    update_req()


@parallel
def deploy():
    """
    Deploy the latest version of the site to the servers,
    install any required third party modules,
    """

    update()

=======
INSTALL
=======

requirements
------------
- django installed for setup
- virtualenv installed

setup
-----
project boostrap::

    django-admin.py startproject -e py,json \
    --template=https://github.com/yvess/project_template/archive/master.zip <project_name>

on server
^^^^^^^^^
on server::

    ln -fs /etc/uwsgi/apps-available/<project>.ini uwsgi.ini

cleanup
-------
run::

    init_project.sh

python setup
------------
virtualenv and db::

    cd <project_name>
    
    virtualenv-2.7 py27
    source py27/bin/activate
    pip install -r requirements.txt
    pip freeze -r requirements.txt > requirements.txt
    ./manage.py syncdb
    ./manage.py migrate

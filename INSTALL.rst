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

    django-admin.py startproject -e py,json --template=https://github.com/yvess/project_template/archive/master.zip <project_name>


cleanup::
    cd <project_name>
    mv gitignore .gitignore
    mv project/gitignore project/.gitignore
    mv project.sublime-project <project_name>.sublime-project
    mv anaconda.json .anaconda
    on server ln -fs /etc/uwsgi/apps-available/<project>.ini uwsgi.ini
    rm INSTALL.rst

virtualenv and db::

    cd <project_name>
    
    virtualenv-2.7 --system-site-packages py27
    source py27/bin/activate
    pip install -r requirements.txt
    ./manage.py syncdb
    ./manage.py migrate


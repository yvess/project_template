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

    django-admin.py startproject -e py,.anaconda --template=~/code/django/project_template <project_name>


cleanup::
    cd <project_name>
    mv gitignore .gitignore
    mv project/gitignore project/.gitignore
    mv project.sublime-project <project_name>.sublime-project
    mv anaconda.json .anaconda
    rm INSTALL.rst
    ln -fs /etc/uwsgi/apps-available/<project>.ini uwsgi.ini

virtualenv and db::

    cd <project_name>
    
    virtualenv-2.7 --system-site-packages py27
    source py27/bin/activate
    pip install -r requirements.txt
    ./manage.py syncdb
    ./manage.py migrate

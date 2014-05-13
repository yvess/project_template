#!/bin/bash
export PYTHONWARNINGS="ignore::DeprecationWarning:simplejson"
trap 'kill 0' SIGINT SIGTERM EXIT
. ./py27/bin/activate
RUNSERVER="./manage.py `python -c "from project.settings import CMD_RUNSERVER;import sys;sys.stdout.write(CMD_RUNSERVER)"`"

if [ "$1" != "" ]; then
    $RUNSERVER `python -c "from project.settings_local import RUN_SH;import sys;sys.stdout.write(RUN_SH['$1'])"`
else
    $RUNSERVER 0.0.0.0:8081
fi

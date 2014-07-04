#!/bin/bash
echo "move hidden files to the right places, rename files"
mv gitignore .gitignore
mv project/gitignore project/.gitignore
mv project.sublime-project `pwd|rev|cut -d "/" -f 1|rev`.sublime-project
mv anaconda.json .anaconda
rm init_project.sh
cat INSTALL.rst
rm INSTALL.rst

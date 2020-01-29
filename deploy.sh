#!/bin/sh
cd ~/odoo-dev/11/proyecto1/src/addons-ar

git pull origin master
git merge -s recursive -X theirs master

echo "done"

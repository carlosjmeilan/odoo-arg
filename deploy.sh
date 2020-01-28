#!/bin/sh
cd ~/odoo-dev/11/proyecto1/src/addons-ar
git add .
git commit -m "deploy"
git pull origin master
echo "deploy done"

#!/bin/bash
set -e
cmd="$@"

echo 'Waiting for postgres'
sleep 10

echo "Migrating database"
python estoque/manage.py migrate
python estoque/manage.py loaddata estoque/fixture.json

echo "Executing tests"
python estoque/manage.py test core


exec $cmd
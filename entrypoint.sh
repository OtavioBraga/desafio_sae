#!/bin/bash
set -e
cmd="$@"


function postgres_ready(){
python << END
import sys
import psycopg2
try:
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="postgres", host="db")
except psycopg2.OperationalError:
    sys.exit(-1)
sys.exit(0)
END
}

until postgres_ready; do
  >&2 echo "Postgres is unavailable - waiting"
  sleep 1
done

echo "Migrating database"
python estoque/manage.py migrate
python estoque/manage.py loaddata estoque/fixture.json

echo "Executing tests"
python estoque/manage.py test core


exec $cmd
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


function has_users(){
python << END
import sys
import psycopg2
conn = psycopg2.connect(dbname="postgres", user="postgres", password="postgres", host="db")
cursor = conn.cursor()
cursor.execute("select * from users_user")
if cursor.fetchall():
    sys.exit(0)
sys.exit(-1)
END
}

if ! has_users; then
    echo ""
    echo "#######################################"
    echo "#       Creating initial User         #"
    echo "#######################################"
    echo "# username: root | password: root1234 #"
    echo "#######################################"
    echo ""
    python estoque/manage.py loaddata estoque/fixture.json
else
    echo ""
    echo "#######################################"
    echo "#        The initial user is          #"
    echo "#######################################"
    echo "# username: root | password: root1234 #"
    echo "#######################################"
    echo ""
fi

echo "Executing tests"
python estoque/manage.py test core

exec $cmd


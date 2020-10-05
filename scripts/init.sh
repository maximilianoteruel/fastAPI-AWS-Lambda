#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

db_ready() {
python << END
import sys
import pymysql.cursors
import os

try:
    connection = pymysql.connect(
        host=os.environ.get('DATABASE_HOST'),
        user=os.environ.get('DATABASE_USER'),
        password=os.environ.get('DATABASE_PASSWORD'),
        db=os.environ.get('DATABASE_NAME'),
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor)

    with connection.cursor() as cursor:
        cursor.execute("SELECT 1")

    sys.exit(0)

except Exception as e:
    sys.exit(-1)

END
}

echo 'Checking DB connection...'
until db_ready; do
    echo 'Waiting for DB to become available...'
    sleep 1
done
echo 'DB is available'


if [ -z ${TYPE+x} ]; then
    echo 'Environment Variable TYPE is not defined. Setting to TYPE=API'
    TYPE="API"
fi

if [ "$TYPE" == "API" ]; then
    
    echo '*** Type API ***'
    
    
    # echo 'Generating Migrations...'
    # alembic revision --autogenerate -m "name"
    
    echo 'Runing Migrations...'
    alembic upgrade head
    
    echo 'Starting Server...'
    hypercorn app.main:app --reload --bind '0.0.0.0:8000'
    
fi

if [ "$TYPE" == "TEST" ]; then
    
    echo '*** Type TEST ***'
    
    echo 'Runing Migrations...'
    PYTHONPATH=. alembic upgrade head
    
    echo 'Runing Tests...'
    pytest --cov=app --cov-report=term-missing:skip-covered app/tests
    
fi



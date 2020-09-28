#!/bin/sh

set -o errexit
set -o pipefail
set -o nounset

echo '::: Entrypoint - BEGIN :::'

db_ready() {
python << END
import sys
import mysql.connector
import os

try:
    conn = mysql.connector.connect(
        host=os.environ.get('DATABASE_HOST'),
        user=os.environ.get('DATABASE_USER'),
        password=os.environ.get('DATABASE_PASSWORD'),
        database=os.environ.get('DATABASE_NAME'),
        autocommit=False)

    if conn.is_connected():
        conn.close()
        sys.exit(0)
    else:
        sys.exit(-1)

except mysql.connector.Error:
    sys.exit(-1)

sys.exit(-1)

END
}

echo 'Checking DB connection...'
until db_ready; do
    echo 'Waiting for DB to become available...'
    sleep 1
done
echo 'DB is available'


echo '::: Entrypoint - END :::'

exec "$@"

#!/bin/sh

set -o errexit
set -o pipefail
set -o nounset

echo '::: Start Dev - BEGIN :::'

if [ -z ${TYPE+x} ]; then
    echo 'Environment Variable TYPE is not defined. Setting to TYPE=API'
    TYPE="API"
fi

if [ "$TYPE" == "API" ]; then
    
    echo '*** Type API ***'
    
    
    # echo 'Generating Migrations...'
    # PYTHONPATH=. alembic revision --autogenerate -m "name"
    
    echo 'Runing migrations...'
    PYTHONPATH=. alembic upgrade head
    
    # echo 'Create initial data in DB...'
    # python /usr/src/app/app/initial_data.py
    
    echo 'Starting Server...'
    uvicorn app.main:app --reload --host 0.0.0.0
    
fi

echo '::: Start Dev - END :::'

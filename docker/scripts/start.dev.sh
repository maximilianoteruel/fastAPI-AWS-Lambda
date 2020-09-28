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
    
    echo 'Starting Server...'
    uvicorn main:app --reload --host 0.0.0.0
    
fi

echo '::: Start Dev - END :::'

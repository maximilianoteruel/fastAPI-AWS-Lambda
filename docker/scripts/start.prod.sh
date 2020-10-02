#!/bin/sh

set -o errexit
set -o pipefail
set -o nounset

echo '::: Start Production - BEGIN :::'

if [ -z ${TYPE+x} ]; then
    echo 'Environment Variable TYPE is not defined. Setting to TYPE=API'
    TYPE="API"
fi

if [ "$TYPE" == "API" ]; then
    echo '*** Type API ***'
    
    echo 'Starting Server...'
    hypercorn app.main:app --reload --bind '0.0.0.0:8000'
fi

echo '::: Start Production - END :::'

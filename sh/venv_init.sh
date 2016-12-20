#!/bin/bash

# Import utils.
source $CDF2CIM_WS_HOME/sh/init.sh

# Main entry point.
main()
{
    log "SH : installing virtual environment ..."

    pip install --upgrade pip
    pip install --upgrade virtualenv
    virtualenv $CDF2CIM_WS_HOME/venv
    source $CDF2CIM_WS_HOME/venv/bin/activate
    pip install --upgrade pip
    pip install --upgrade --no-cache-dir -I -r $CDF2CIM_WS_HOME/requirements.txt
    deactivate
}

# Invoke entry point.
main

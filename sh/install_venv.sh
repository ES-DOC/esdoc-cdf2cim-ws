#!/bin/bash

# Import utils.
source $CDF2CIM_WS_HOME/sh/utils.sh

# Main entry point.
main()
{
    log "installing virtual environment ..."

    pip install --upgrade pip
    pip install --upgrade virtualenv
    virtualenv $CDF2CIM_WS_HOME/ops/venv
	source $CDF2CIM_WS_HOME/sh/activate_venv.sh
    pip install --upgrade pip
    pip install --upgrade --no-cache-dir -I -r $CDF2CIM_WS_HOME/resources/requirements.txt
    pip install --upgrade --no-cache-dir -I -r $CDF2CIM_WS_HOME/resources/requirements-pyesdoc.txt
    deactivate
}

# Invoke entry point.
main

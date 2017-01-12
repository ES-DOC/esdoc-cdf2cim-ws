#!/bin/bash

# Import utils.
source $CDF2CIM_WS_HOME/sh/utils.sh

# Main entry point.
main()
{
    log "installing virtual environment ..."

    $CDF2CIM_WS_PIP install --upgrade pip
    $CDF2CIM_WS_PIP install --upgrade virtualenv
    virtualenv $CDF2CIM_WS_HOME/ops/venv
	source $CDF2CIM_WS_HOME/sh/activate_venv.sh
    $CDF2CIM_WS_PIP install --upgrade pip
    $CDF2CIM_WS_PIP install --upgrade --no-cache-dir -I -r $CDF2CIM_WS_HOME/resources/requirements.txt
    deactivate
}

# Invoke entry point.
main

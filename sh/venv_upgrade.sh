#!/bin/bash

# Import utils.
source $CDF2CIM_WS_HOME/sh/init.sh

# Main entry point.
main()
{
    log "SH : upgrading virtual environment ..."

    source $CDF2CIM_WS_HOME/venv/bin/activate
    pip install --upgrade pip
    pip install --upgrade --no-cache-dir -I -r $CDF2CIM_WS_HOME/requirements.txt
    deactivate
}

# Invoke entry point.
main
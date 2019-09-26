#!/bin/bash

# Import utils.
source $CDF2CIM_WS_HOME/sh/utils.sh

# Main entry point.
main()
{
	source $CDF2CIM_WS_HOME/sh/activate_venv.sh
    pip install --upgrade pip
    pip install --upgrade --no-cache-dir -I -r $CDF2CIM_WS_HOME/requirements.txt
    deactivate

    log "virtual environment updated"
}

# Invoke entry point.
main

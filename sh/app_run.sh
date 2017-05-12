#!/bin/bash

# Import utils.
source $CDF2CIM_WS_HOME/sh/utils.sh

# Main entry point.
main()
{
    log "running ... @ "$CDF2CIM_WS_HOME

    source $CDF2CIM_WS_HOME/sh/activate_venv.sh
	python $CDF2CIM_WS_HOME/sh/app_run.py
}

# Invoke entry point.
main

#!/bin/bash

# Import utils.
source $CDF2CIM_WS_HOME/sh/init.sh

# Main entry point.
main()
{
    log "WEB-SERVICE : running ..."

    source $CDF2CIM_WS_HOME/venv/bin/activate
	python $CDF2CIM_WS_HOME/sh/ws_run.py
}

# Invoke entry point.
main

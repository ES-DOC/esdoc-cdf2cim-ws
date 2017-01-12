#!/bin/bash

# Import utils.
source $CDF2CIM_WS_HOME/sh/utils.sh

# Main entry point.
main()
{
    log "update starts ..."

	cd $CDF2CIM_WS_HOME
	git pull
    log "shell updated"
	source $CDF2CIM_WS_HOME/sh/update_venv.sh

    log "update complete"
}

# Invoke entry point.
main

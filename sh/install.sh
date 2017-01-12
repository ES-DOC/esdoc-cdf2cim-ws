#!/bin/bash

# Import utils.
source $CDF2CIM_WS_HOME/sh/utils.sh

# Main entry point.
main()
{
    log "install starts ..."

	source $CDF2CIM_WS_HOME/sh/install_config.sh
	source $CDF2CIM_WS_HOME/sh/install_venv.sh

    log "install complete"
}

# Invoke entry point.
main

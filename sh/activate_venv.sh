#!/bin/bash

# Import utils.
source $CDF2CIM_WS_HOME/sh/utils.sh

# Main entry point.
main()
{
	export PYTHONPATH=$CDF2CIM_WS_HOME:$PYTHONPATH
	venv_path=${CDF2CIM_WS_VENV:-$CDF2CIM_WS_HOME/ops/venv}
	source $venv_path/bin/activate
	log "venv activated @ "$venv_path
}

# Invoke entry point.
main

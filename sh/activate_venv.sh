#!/bin/bash

# Import utils.
source $CDF2CIM_WS_HOME/sh/utils.sh

# Main entry point.
main()
{
	export PYTHONPATH=$PYTHONPATH:$CDF2CIM_WS_HOME
	source $CDF2CIM_WS_HOME/ops/venv/bin/activate
}

# Invoke entry point.
main

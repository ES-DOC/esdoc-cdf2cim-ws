#!/bin/bash

# Import utils.
source $CDF2CIM_WS_HOME/sh/utils.sh

# Main entry point.
main()
{
	rm $CDF2CIM_WS_HOME/ops/logs/*.log

	log "logs reset"
}

# Invoke entry point.
main

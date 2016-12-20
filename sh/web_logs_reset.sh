#!/bin/bash

# Import utils.
source $CDF2CIM_WS_HOME/sh/init.sh

# Main entry point.
main()
{
	rm $CDF2CIM_WS_HOME/ops/*.log

	log "WEB : reset web-service logs"
}

# Invoke entry point.
main

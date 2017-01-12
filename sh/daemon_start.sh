#!/bin/bash

# Import utils.
source $CDF2CIM_WS_HOME/sh/utils.sh

# Main entry point.
main()
{
	source $CDF2CIM_WS_HOME/sh/reset_logs.sh
	supervisord -c $CDF2CIM_WS_HOME/ops/config/supervisord.conf

	log "initialized web-service daemon"
}

# Invoke entry point.
main

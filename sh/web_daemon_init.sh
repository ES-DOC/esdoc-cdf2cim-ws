#!/bin/bash

# Import utils.
source $CDF2CIM_WS_HOME/sh/init.sh

# Main entry point.
main()
{
	source $CDF2CIM_WS_HOME/sh/web_logs_reset.sh
	supervisord -c $CDF2CIM_WS_HOME/ops/supervisord.conf

	log "WEB : initialized web-service daemon"
}

# Invoke entry point.
main

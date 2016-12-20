#!/bin/bash

# Import utils.
source $CDF2CIM_WS_HOME/sh/init.sh

# Main entry point.
main()
{
	supervisorctl -c $CDF2CIM_WS_HOME/ops/supervisord.conf stop all
	supervisorctl -c $CDF2CIM_WS_HOME/ops/supervisord.conf shutdown

	log "WEB : killed web-service daemon"
}

# Invoke entry point.
main

#!/bin/bash

# Import utils.
source $CDF2CIM_WS_HOME/sh/init.sh

# Main entry point.
main()
{
	cp $CDF2CIM_WS_HOME/templates/template-supervisord.conf $CDF2CIM_WS_HOME/ops/supervisord.conf
	cp $CDF2CIM_WS_HOME/templates/template-ws.conf $CDF2CIM_WS_HOME/ops/ws.conf

	log "WEB : updated web-service configuation"
}

# Invoke entry point.
main

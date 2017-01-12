#!/bin/bash

# Import utils.
source $CDF2CIM_WS_HOME/sh/utils.sh

# Main entry point.
main()
{
	cp $CDF2CIM_WS_HOME/resources/template-supervisord.conf $CDF2CIM_WS_HOME/ops/config/supervisord.conf
	cp $CDF2CIM_WS_HOME/resources/template-ws.conf $CDF2CIM_WS_HOME/ops/config/ws.conf

	log "configuration files initialized"
}

# Invoke entry point.
main

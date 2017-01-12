#!/bin/bash

# Import utils.
source $CDF2CIM_WS_HOME/sh/utils.sh

# Main entry point.
main()
{
	supervisorctl -c $CDF2CIM_WS_HOME/ops/config/supervisord.conf status all
}

# Invoke entry point.
main

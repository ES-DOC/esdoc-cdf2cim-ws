#!/bin/bash

# Import utils.
source $CDF2CIM_WS_HOME/sh/init.sh

# Main entry point.
main()
{
    log "CDF2CIM-WS-TESTS : running ..."

    nosetests -v -s $CDF2CIM_WS_HOME/tests

    log "CDF2CIM-WS-TESTS : complete ..."
}

# Invoke entry point.
main

#!/bin/bash

# Import utils.
source $CDF2CIM_WS_HOME/sh/utils.sh

# Main entry point.
main()
{
    log "TESTS : running ..."

    source $CDF2CIM_WS_HOME/sh/activate_venv.sh
    nosetests -v -s $CDF2CIM_WS_HOME/tests

    log "TESTS : complete ..."
}

# Invoke entry point.
main

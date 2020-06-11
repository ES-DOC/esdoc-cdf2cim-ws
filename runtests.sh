#!/bin/bash

# Set home path.
declare CDF2CIM_WS_HOME="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $CDF2CIM_WS_HOME

# Import utils.
source $CDF2CIM_WS_HOME/sh/utils.sh

# Main entry point.
main()
{
    log "CDF2CIM-TESTS : execution starts ..."

	pushd $CDF2CIM_WS_HOME
    pipenv run nosetests -v -s $CDF2CIM_WS_HOME/tests
    # pipenv run nosetests -v -s $CDF2CIM_WS_HOME/tests/test_ops.py
    # pipenv run nosetests -v -s $CDF2CIM_WS_HOME/tests/test_publication.py

    log "CDF2CIM-TESTS : execution complete ..."
}

# Invoke entry point.
main

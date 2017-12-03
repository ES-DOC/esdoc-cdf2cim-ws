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

    source $CDF2CIM_WS_HOME/sh/activate_venv.sh

    nosetests -v -s $CDF2CIM_WS_HOME/tests
    # nosetests -v -s $CDF2CIM_WS_HOME/tests/test_ops.py
    # nosetests -v -s $CDF2CIM_WS_HOME/tests/test_publication.py

    log "CDF2CIM-TESTS : execution complete ..."
}

# Invoke entry point.
main

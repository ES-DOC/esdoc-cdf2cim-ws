#!/bin/bash

# Import utils.
source $CDF2CIM_WS_HOME/sh/utils.sh

_update_src()
{
    pushd $CDF2CIM_WS_HOME
	git pull
}

_update_venv()
{
    pushd $CDF2CIM_WS_HOME
    pipenv install -r $CDF2CIM_WS_HOME/requirements.txt
}

# Main entry point.
main()
{
    log "update starts ..."

    _update_src
    _update_venv

    log "update complete"
}

# Invoke entry point.
main

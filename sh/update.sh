#!/bin/bash

# Import utils.
source $CDF2CIM_WS_HOME/sh/utils.sh

_update_src()
{
	git pull
}

_update_venv()
{
    pipenv install -r $CDF2CIM_WS_HOME/requirements.txt
}

# Main entry point.
main()
{
    log "update starts ..."

    pushd $CDF2CIM_WS_HOME
    _update_src
    _update_venv
    popd

    log "update complete"
}

# Invoke entry point.
main

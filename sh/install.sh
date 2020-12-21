#!/bin/bash

# Import utils.
source $CDF2CIM_WS_HOME/sh/utils.sh

# Main entry point.
main()
{
	_install_ops_dir
	_install_config
	_install_venv
	log "web-service installed"
}

_install_ops_dir()
{
	mkdir -p $CDF2CIM_WS_HOME/ops
	mkdir -p $CDF2CIM_WS_HOME/ops/config
	mkdir -p $CDF2CIM_WS_HOME/ops/daemon
	mkdir -p $CDF2CIM_WS_HOME/ops/logs
	log "ops directory installed"
}

_install_config()
{
	cp $CDF2CIM_WS_HOME/resources/*.conf $CDF2CIM_WS_HOME/ops/config
	log "configuration files installed"
}

_install_venv()
{
	pushd $CDF2CIM_WS_HOME

    log "installing virtual environment ..."

    # Update pip / pipenv to latest versions.
    pip3 install --upgrade pip
    pip3 install --upgrade pipenv

	# Install venv using pipenv.
	pipenv install 

	log "virtual environment installed"

	popd
}

# Invoke entry point.
main

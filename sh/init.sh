#!/bin/bash

# ###############################################################
# SECTION: HELPER FUNCTIONS
# ###############################################################

# Wraps standard echo by adding ESDOC prefix.
log()
{
	declare now=`date +%Y-%m-%dT%H:%M:%S`
	declare tabs=''
	if [ "$1" ]; then
		if [ "$2" ]; then
			for ((i=0; i<$2; i++))
			do
				declare tabs+='\t'
			done
	    	echo -e $now" [INFO] :: CDF2CIM-WS > "$tabs$1
	    else
	    	echo -e $now" [INFO] :: CDF2CIM-WS > "$1
	    fi
	else
	    echo -e $now" [INFO] :: CDF2CIM-WS > "
	fi
}

# ###############################################################
# SECTION: INITIALIZE VARS
# ###############################################################

# Set of ops sub-directories.
declare -a CDF2CIM_WS_OPS_DIRS=(
	$CDF2CIM_WS_HOME/ops
)

# ###############################################################
# SECTION: Initialise file system
# ###############################################################

# Ensure ops paths exist.
for ops_dir in "${CDF2CIM_WS_OPS_DIRS[@]}"
do
	mkdir -p $ops_dir
done

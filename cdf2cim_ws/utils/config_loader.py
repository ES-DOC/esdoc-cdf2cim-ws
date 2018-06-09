# -*- coding: utf-8 -*-
"""
.. module:: utils.config.py
   :license: GPL/CeCIL
   :platform: Unix
   :synopsis: Configuration utility functions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import os

from cdf2cim_ws.utils import logger
from cdf2cim_ws.utils.convertor import json_file_to_namedtuple



# Default configuration file path.
_CONFIG_FPATH = "ws.conf"

# Set of environment variables.
_ENV_VARS = {
    'CDF2CIM_ARCHIVE_HOME',
    }

# Configuration data.
data = None


def _init():
    """Initializes configuration.

    """
    global data

    # Validate expected environment variables.
    _validate_env_vars()

    # Get configuration file path (falling back to template if necessary).
    fpath = _get_config_fpath()

    # Convert config file to a named tuple.
    data = json_file_to_namedtuple(fpath)

    logger.log_web("Configuration file loaded @ {}".format(fpath))


def _get_config_fpath():
    """Returns configuration file path.

    """
    dpath = os.path.dirname(os.path.abspath(__file__))
    while dpath != '/':
        fpath = os.path.join(dpath, "ops/config")
        fpath = os.path.join(fpath, _CONFIG_FPATH)
        if os.path.exists(fpath):
            return fpath
        dpath = os.path.dirname(dpath)

    err = "ESDOC-CDF2CIM-WS configuration file ({0}) could not be found".format(_CONFIG_FPATH)
    raise RuntimeError(err)


def _validate_env_vars():
    """Validates environment variables.

    """
    for ev in _ENV_VARS:
        if os.getenv('CDF2CIM_ARCHIVE_HOME') is None:
            err = "ESDOC-CDF2CIM-WS environment variable ({0}) could not be found".format(ev)
            raise RuntimeError(err)


# Auto-initialize.
_init()

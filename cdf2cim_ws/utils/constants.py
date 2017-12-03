# -*- coding: utf-8 -*-
"""

.. module:: constants.py
   :license: GPL/CeCIL
   :platform: Unix
   :synopsis: ES-DOC CDF2CIM - web-service constants.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import os



# Default endpoint.
DEFAULT_ENDPOINT = r'/1/ops/heartbeat'

# HTTP CORS header.
HTTP_HEADER_Access_Control_Allow_Origin = "Access-Control-Allow-Origin"

# Processing error HTTP response codes.
HTTP_RESPONSE_BAD_REQUEST_ERROR = 400
HTTP_RESPONSE_SERVER_ERROR = 500

# I/O directory.
IO_DIR = os.getenv('CDF2CIM_WS_HOME')
IO_DIR = os.path.join(IO_DIR, 'ops')
IO_DIR = os.path.join(IO_DIR, 'output')

# TODO - leverage pyessv
# Institute - BADC.
INSTITUTE_BADC = u"badc"

# Institute - DKRZ.
INSTITUTE_DKRZ = u"dkrz"

# Institute - IPSL.
INSTITUTE_IPSL = u"ipsl"

# Institute - all.
INSTITUTE = [
	{
	    'key': INSTITUTE_BADC,
	    'label': u"BADC"
	},
	{
	    'key': INSTITUTE_DKRZ,
	    'label': u"DKRZ"
	},
	{
	    'key': INSTITUTE_IPSL,
	    'label': u"IPSL"
	}
]

# JSON field names.
JF_HASHID = '_hashid'

# Project - cmip5.
PROJECT_CMIP5 = u"cmip5"

# Project - cmip6.
PROJECT_CMIP6 = u"cmip6"

# Project - all.
PROJECT = [
	{
	    'key': PROJECT_CMIP5,
	    'label': u"CMIP5"
	},
	{
	    'key': PROJECT_CMIP6,
	    'label': u"CMIP6"
	}
]


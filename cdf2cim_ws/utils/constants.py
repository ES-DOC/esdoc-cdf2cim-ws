# -*- coding: utf-8 -*-
"""

.. module:: constants.py
   :license: GPL/CeCIL
   :platform: Unix
   :synopsis: ES-DOC CDF2CIM - web-service constants.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
# ESDOC GitHub team: cdf2cim-publication.
CDF2CIM_PUBLICATION_GH_TEAM = 'cdf2cim-publication'

# Default endpoint.
DEFAULT_ENDPOINT = r'/1/ops/heartbeat'

# Project - cmip5.
PROJECT_CMIP5 = u"cmip5"

# Project - cmip6.
PROJECT_CMIP6 = u"cmip6"

# Project - test.
PROJECT_TEST = u"test"

# Project - all.
PROJECT = [
	{
	    'key': PROJECT_CMIP5,
	    'label': u"CMIP5"
	},
	{
	    'key': PROJECT_CMIP6,
	    'label': u"CMIP6"
	},
	{
	    'key': PROJECT_TEST,
	    'label': u"TEST"
	}
]

# TODO - leverage pyesdoc
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

# -*- coding: utf-8 -*-
"""

.. module:: schemas.extender.py
   :license: GPL/CeCIL
   :platform: Unix
   :synopsis: ES-DOC CDF2CIM - endpoint validation schema cache extender.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import collections

import pyessv

from cdf2cim_ws.utils import constants


# Schema extender functions mapped by schema type and endpoint.
_EXTENDERS = collections.defaultdict(dict)


def extend(schema, typeof, endpoint):
    """Extends a JSON schema with data pulled from controlled vocabularies.

    :param dict schema: A JSON schema being extended.
    :param str typeof: Type of JSON schema to be extended.
    :param str endpoint: Endpoint being mapped to a JSON schema.

    """
    try:
        extender = _EXTENDERS[endpoint][typeof]
    except KeyError:
        pass
    else:
        extender(schema)


def _1_cmip6(schema):
    """Extends a JSON schema used to validate an HTTP operatino.

    """
    for vocab in {
        'wcrp:cmip6:activity_id',
        'wcrp:cmip6:experiment_id',
        'wcrp:cmip6:institution_id',
        'wcrp:cmip6:source_id'
        }:
        names = []
        for term in pyessv.load(vocab):
            names += term.all_names
        schema['properties'][vocab.split(':')[-1]]['enum'] = sorted(set(names))


# Map endpoints to extenders.
_EXTENDERS['/1/cmip6']['body'] = _1_cmip6

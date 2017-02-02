# -*- coding: utf-8 -*-

"""
.. module:: test_publishing.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Executes web-service publishing endpoint tests.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>

"""
import os

import requests

from tests import utils as tu



def test_publish_cmip5():
    """CDF2CIM :: WS :: Postive Test :: cmip5 publication.

    """
    _test_publication("cmip5", tu.SAMPLE_OUTPUT_CMIP5)


def test_publish_cmip5_negative():
    """CDF2CIM :: WS :: Negative Test :: cmip5 publication.

    """
    _test_publication("cmip5", tu.SAMPLE_OUTPUT_CMIP5_INVALID, 400)


def test_publish_cmip6():
    """CDF2CIM :: WS :: Postive Test :: cmip6 publication.

    """
    _test_publication("cmip6", tu.SAMPLE_OUTPUT_CMIP6)


def test_publish_cmip6_negative():
    """CDF2CIM :: WS :: Negative Test :: cmip6 publication.

    """
    _test_publication("cmip6", tu.SAMPLE_OUTPUT_CMIP6_INVALID, 400)


def _test_publication(mip_era, payload, status_code=200):
    """ERRATA :: WS :: Postive Test :: Create issue.

    """
    # Prepare request.
    credentials = tu.get_ws_credentials()
    headers = {'Content-Type': 'application/json'}
    endpoint = "{}/1/{}".format(os.getenv("CDF2CIM_WS_HOST"), mip_era)

    # Invoke endpoint.
    response = requests.post(
        endpoint,
        data=payload,
        headers=headers,
        auth=credentials
        )

    # Assert response.
    tu.assert_ws_response(endpoint, response, status_code)

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
    """CDF2CIM :: WS :: Test (+ve) :: cmip5 publication.

    """
    _exec_test("cmip5", tu.SAMPLE_OUTPUT_CMIP5, 200)


def test_publish_cmip5_negative():
    """CDF2CIM :: WS :: Test (-ve) :: cmip5 publication.

    """
    _exec_test("cmip5", tu.SAMPLE_OUTPUT_CMIP5_INVALID, 400)


def test_publish_cmip6():
    """CDF2CIM :: WS :: Test (+ve) :: cmip6 publication.

    """
    _exec_test("cmip6", tu.SAMPLE_OUTPUT_CMIP6, 200)


def test_publish_cmip6_negative():
    """CDF2CIM :: WS :: Test (-ve) :: cmip6 publication.

    """
    _exec_test("cmip6", tu.SAMPLE_OUTPUT_CMIP6_INVALID, 400)


def _exec_test(mip_era, payload, status_code):
    """Invoke web service.

    """
    # Invoke endpoint.
    url = "{}/1/{}".format(os.getenv("CDF2CIM_WS_HOST"), mip_era)
    response = requests.post(
        url,
        data=payload,
        headers={'Content-Type': 'application/json'},
        auth=tu.get_credentials()
        )

    # Assert response.
    tu.assert_ws_response(url, response, status_code)

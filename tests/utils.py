# -*- coding: utf-8 -*-

"""
.. module:: utils.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Unit test utilities.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>

"""
import json
import os

import requests



# Sample output.
SAMPLE_OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "sample-output")
with open(os.path.join(SAMPLE_OUTPUT_DIR, 'cmip5.json'), 'r') as _fstream:
    SAMPLE_OUTPUT_CMIP5 = _fstream.read()
with open(os.path.join(SAMPLE_OUTPUT_DIR, 'cmip5-invalid.json'), 'r') as _fstream:
    SAMPLE_OUTPUT_CMIP5_INVALID = _fstream.read()
with open(os.path.join(SAMPLE_OUTPUT_DIR, 'cmip6.json'), 'r') as _fstream:
    SAMPLE_OUTPUT_CMIP6 = _fstream.read()
with open(os.path.join(SAMPLE_OUTPUT_DIR, 'cmip6-invalid.json'), 'r') as _fstream:
    SAMPLE_OUTPUT_CMIP6_INVALID = _fstream.read()


def get_credentials():
    """Returns credentials to be passed to web-service.

    """
    return os.getenv('CDF2CIM_CLIENT_GITHUB_USER'), \
           os.getenv('CDF2CIM_CLIENT_GITHUB_ACCESS_TOKEN')


def assert_ws_response(
    url,
    response,
    status_code=requests.codes.OK,
    fields=set()
    ):
    """Asserts a response received from web-service.

    """
    # WS url.
    assert response.url.split('?')[0] == url.split('?')[0]

    # WS response HTTP status code.
    assert response.status_code == status_code, \
           "WEB-SERVICE FAILURE: {} :: {}".format(response.status_code, response.text)

    # WS response = unicode.
    assert isinstance(response.text, unicode)

    # WS response has no cookies.
    assert len(response.cookies) == 0

    # WS response history is empty (i.e. no intermediate servers).
    assert len(response.history) == 0
    assert response.is_permanent_redirect == False
    assert response.is_redirect == False
    assert len(response.links) == 0

    # Default WS respponse headers.
    assert len(response.headers) >= 3
    for header in {
        # 'Content-Length',
        'Content-Type',
        'Date',
        'Server',
        'Vary'
        }:
        assert header in response.headers

    # WS response content must be utf-8 encoded JSON.
    if response.text:
        assert response.encoding.lower() == u'utf-8'
        content = response.json()
        assert isinstance(content, dict)
        for field in fields:
            assert field in content

        return content

# -*- coding: utf-8 -*-

"""
.. module:: test_publishing.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Executes web-service publishing endpoint tests.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>

"""
import json
import os

import requests

from cdf2cim_ws.utils import constants



# Set of target urls.
_URL = os.getenv("CDF2CIM_WS_HOST")
_URL_CREATE = "{}/1/create".format(_URL)


def test_create():
    """ERRATA :: WS :: Postive Test :: Create issue.

    """
    # Invoke WS endpoint.
    response = requests.post(
        _URL_CREATE,
        data=json.dumps({
            "institution_id": "IPSL"
            }),
        headers={'Content-Type': 'application/json'},
        auth=_get_ws_credentials()
        )

    # Assert WS response.
    _assert_ws_response(_URL_CREATE, response)


def _get_ws_credentials():
    """Returns credentials to be passed to web-service.

    """
    return os.getenv('CDF2CIM_GITHUB_USER_NAME'), \
           os.getenv('CDF2CIM_GITHUB_ACCESS_TOKEN')


def _assert_ws_response(
    url,
    response,
    status_code=requests.codes.OK,
    expected_content=None
    ):
    """Asserts a response received from web-service.

    """
    # WS url.
    assert response.url == url

    # WS response HTTP status code.
    assert response.status_code == status_code, response.status_code

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
        'Content-Length',
        'Content-Type',
        'Date',
        'Server',
        'Vary'
        }:
        assert header in response.headers

    # WS response content must be utf-8 encoded JSON.
    if response.text:
        assert response.encoding == u'utf-8'
        content = response.json()
        assert isinstance(content, dict)

        # WS response content.
        if expected_content is not None:
            assert content == expected_content

        return content

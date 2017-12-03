# -*- coding: utf-8 -*-

"""
.. module:: test_ops.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Executes web-service operations (ops) endpoint tests.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>

"""
import os
import urllib

import requests

from tests import utils as tu



# Set of target urls.
_URL_HEARTBEAT = "{}/".format(os.getenv("CDF2CIM_WS_HOST"))
_URL_VERIFY_AUTHORIZATION = "{}/verify-authorization?".format(os.getenv("CDF2CIM_WS_HOST"))
_URL_VERIFY_AUTHORIZATION += urllib.urlencode({
    'login': os.getenv('CDF2CIM_CLIENT_GITHUB_USER'),
    'token': os.getenv('CDF2CIM_CLIENT_GITHUB_ACCESS_TOKEN')
    })


def test_heartbeat():
    """CDF2CIM :: WS :: Test (+ve) :: Ops heartbeat.

    """
    # Invoke WS endpoint.
    url = _URL_HEARTBEAT
    r = requests.get(url)

    # Assert WS response.
    tu.assert_ws_response(url, r, fields={'message', 'version'})


def test_verify_authorization():
    """CDF2CIM :: WS :: Test (+ve) :: Ops authorization verification.

    """
    # Invoke WS endpoint.
    url = _URL_VERIFY_AUTHORIZATION
    r = requests.get(url)

    # Assert WS response.
    tu.assert_ws_response(url, r, fields={'message',})

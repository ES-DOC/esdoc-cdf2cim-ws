# -*- coding: utf-8 -*-

"""
.. module:: test_ops.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Executes web-service operations (ops) endpoint tests.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>

"""
import os

import requests

from tests import utils as tu


# Set of target urls.
_URL_HEARTBEAT = "{}/".format(os.getenv("CDF2CIM_WS_HOST"))


def test_heartbeat():
    """CDF2CIM :: WS :: Postive Test :: Ops heartbeat.

    """
    # Invoke WS endpoint.
    url = _URL_HEARTBEAT
    response = requests.get(_URL_HEARTBEAT)

    # Assert WS response.
    response = tu.assert_ws_response(url, response)
    assert "message" in response
    assert "version" in response

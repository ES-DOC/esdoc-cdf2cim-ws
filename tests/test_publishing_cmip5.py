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
from tests import utils as tu



# Set of target urls.
_URL = os.getenv("CDF2CIM_WS_HOST")
_URL_CREATE = "{}/1/create/cmip5".format(_URL)


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
        auth=tu.get_ws_credentials()
        )

    # Assert WS response.
    tu.assert_ws_response(_URL_CREATE, response)




# -*- coding: utf-8 -*-
"""
.. module:: utils.http_security.py
   :license: GPL/CeCIL
   :platform: Unix
   :synopsis: Request security filter.

.. moduleauthor:: Mark A. Greenslade <momipsl@ipsl.jussieu.fr>


"""
import base64
import os

import requests

from cdf2cim_ws.utils import exceptions



# GitHub identifier of cdf2cim-publication team.
_GH_TEAM_ID = 2206031

# GitHub API - user within GitHub.
_GH_API_USER = "https://api.github.com/user"

# GitHub API - ES-DOC-OPS team membership endpoint.
_GH_API_TEAM_MEMBERSHIP = "https://api.github.com/teams/{}/memberships/{}"


def _authenticate(credentials):
    """Authenticates user credentials request against GitHub user api.

    """
    # Parse HTTP Basic base64 encoded credentials.
    credentials = credentials.replace('Basic ', '')
    try:
        credentials = base64.b64decode(credentials)
    except TypeError:
        raise exceptions.AuthenticationError()
    else:
        credentials = credentials.split(':')
        if len(credentials) != 2:
            raise exceptions.AuthenticationError()

    # Authenticate.
    r = requests.get(_GH_API_USER, auth=tuple(credentials))
    if r.status_code != 200:
        raise exceptions.AuthenticationError()

    return credentials[0]


def _authorize(gh_login):
    """Authorizes user against GitHub team membership api.

    """
    # Set authorization credentials.
    credentials = (os.getenv('CDF2CIM_WS_GITHUB_USER'),
                   os.getenv('CDF2CIM_WS_GITHUB_ACCESS_TOKEN'))

    # Authorize.
    url = _GH_API_TEAM_MEMBERSHIP.format(_GH_TEAM_ID, gh_login)
    r = requests.get(url, auth=credentials)
    if r.status_code != 200:
        raise exceptions.AuthorizationError()


def secure_request(handler):
    """Enforces request level security policy (if necesaary).

    :param utils.http.HTTPRequestHandler handler: An HTTP request handler.

    :raises: exceptions.AuthenticationError, exceptions.AuthorizationError

    """
    if handler.request.path.split("?")[0] != "/":
        _authorize(_authenticate(handler.request.headers['Authorization']))

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

from cdf2cim_ws.utils import config
from cdf2cim_ws.utils import exceptions



# GitHub user name used when applying security filter.
_GH_SYSTEM_USER = "esdoc-system-user"

# GitHub identifier of cdf2cim-publication team.
_GH_TEAM_ID = 2206031

# GitHub user API.
_GH_API_USER = "https://api.github.com/user"

# GitHub teams API.
_GH_API_TEAM_MEMBERSHIP = "https://api.github.com/teams/{}/memberships/{}"

# Set of whitelisted endpoints.
_WHITELISTED_ENDPOINTS = {
    '/',
    '/verify-authorization'
}


def authenticate(credentials):
    """Authenticates user credentials request against GitHub user api.

    :param tuple credentials: 2 member tuple (GitHub username, GitHub access token)

    :returns: GitHub username
    :rtype: str

    """
    r = requests.get(_GH_API_USER, auth=credentials)
    if r.status_code != 200:
        raise exceptions.AuthenticationError()

    return credentials[0]


def authorize(gh_login):
    """Authorizes user against GitHub team membership api.

    :param str gh_login: GitHub username

    """
    # Set system user gh credentials.
    credentials = (_GH_SYSTEM_USER, os.getenv('CDF2CIM_WS_GITHUB_ACCESS_TOKEN'))

    # Authorize.
    url = _GH_API_TEAM_MEMBERSHIP.format(_GH_TEAM_ID, gh_login)
    r = requests.get(url, auth=credentials)
    if r.status_code != 200:
        raise exceptions.AuthorizationError()


def _strip_credentials(http_header):
    """Strips passed credentials from HTTP header.

    """
    credentials = http_header.replace('Basic ', '')
    try:
        credentials = base64.b64decode(credentials)
    except TypeError:
        raise exceptions.AuthenticationError()
    else:
        credentials = credentials.split(':')
        if len(credentials) != 2:
            raise exceptions.AuthenticationError()

    return tuple(credentials)


def secure_request(handler):
    """Enforces request level security policy (if necesaary).

    :param utils.http.HTTPRequestHandler handler: An HTTP request handler.

    :raises: exceptions.AuthenticationError, exceptions.AuthorizationError

    """
    if config.apply_security_policy == False or \
       handler.request.path in _WHITELISTED_ENDPOINTS:
        return

    credentials = _strip_credentials(handler.request.headers['Authorization'])

    authorize(authenticate(credentials))

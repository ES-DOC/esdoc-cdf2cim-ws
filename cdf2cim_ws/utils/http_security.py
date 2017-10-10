# -*- coding: utf-8 -*-
"""
.. module:: utils.http_security.py
   :license: GPL/CeCIL
   :platform: Unix
   :synopsis: Request security filter.

.. moduleauthor:: Mark A. Greenslade <momipsl@ipsl.jussieu.fr>


"""
import base64

from pyesdoc.security import AuthenticationError
from pyesdoc.security import AuthorizationError
from pyesdoc.security import is_authenticated_user
from pyesdoc.security import is_team_member
from pyesdoc.security import strip_credentials

from cdf2cim_ws.utils import config



# GitHub identifier of cdf2cim-publication team.
_GH_TEAM_ID = 2206031

# Set of whitelisted endpoints.
_WHITELISTED_ENDPOINTS = {
    '/',
    '/verify',
    '/verify-authorization'
}


def authenticate(credentials):
    """Authenticates user credentials request against GitHub user api.

    :param tuple credentials: 2 member tuple (GitHub username, GitHub access token)

    :returns: GitHub username
    :rtype: str

    """
    user_id, access_token = credentials
    if not is_authenticated_user(user_id, access_token):
        raise AuthenticationError()

    return user_id


def authorize(user_id):
    """Authorizes user against GitHub team membership api.

    :param str user_id: GitHub username.

    """
    if not is_team_member(_GH_TEAM_ID, user_id):
        raise AuthorizationError()
    # TODO verify institute


def secure_request(handler):
    """Enforces request level security policy (if necesaary).

    :param utils.http.HTTPRequestHandler handler: An HTTP request handler.

    :raises: AuthenticationError, AuthorizationError

    """
    if config.apply_security_policy == False or \
       handler.request.path in _WHITELISTED_ENDPOINTS:
       return

    credentials = strip_credentials(handler.request.headers['Authorization'])
    authorize(authenticate(credentials))

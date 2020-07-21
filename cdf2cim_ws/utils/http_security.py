# -*- coding: utf-8 -*-
"""
.. module:: utils.http_security.py
   :license: GPL/CeCIL
   :platform: Unix
   :synopsis: Request security filter.

.. moduleauthor:: Mark A. Greenslade <momipsl@ipsl.jussieu.fr>


"""
from cdf2cim_ws.utils import config
from cdf2cim_ws.utils import logger
from cdf2cim_ws.utils import security



# GitHub team name.
_GH_TEAM = 'cdf2cim-publication'

# Set of whitelisted endpoints.
_WHITELISTED_ENDPOINTS = {
    '/',
    '/verify',
    '/verify-authorization'
}


def apply_policy(user_id, access_token):
    """Applies security policy.

    :param str user_id: GitHub username.
    :param str access_token: GitHub access token.
    :param str institute_id: Institute identifier, e.g. ipsl.

    """
    authenticate((user_id, access_token))
    authorize(user_id)


def authenticate(credentials):
    """Authenticates user credentials request against GitHub user api.

    :param tuple credentials: 2 member tuple (GitHub username, GitHub access token)

    :returns: GitHub username
    :rtype: str

    """
    security.authenticate_user(credentials)


def authorize(user_id):
    """Authorizes user against GitHub team membership api.

    :param str user_id: GitHub username.

    """
    logger.log_web('Authorizing: {} --> {}'.format(user_id, _GH_TEAM))
    security.authorize_user(_GH_TEAM, user_id)


def secure_request(handler):
    """Enforces request level security policy (if necessary).

    :param utils.http.HTTPRequestHandler handler: An HTTP request handler.

    """
    # Escape if endpoint is whitelisted.
    if handler.request.path in _WHITELISTED_ENDPOINTS:
        return

    # Set credentials - either from web-form or cli client.
    credentials = handler.request.headers['Authorization']

    # Strip credentials - i.e. destructure from b64 --> 2 member tuple.
    credentials = security.strip_credentials(credentials)

    # Authenticate.
    if config.apply_security_policy:
        logger.log_web('Authenticating: {}'.format(credentials[0]))
        authenticate(credentials)

    # Make user-id available downstream.
    handler.user_id = credentials[0]

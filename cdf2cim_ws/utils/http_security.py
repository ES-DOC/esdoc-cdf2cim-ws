# -*- coding: utf-8 -*-
"""
.. module:: utils.misc.py
   :license: GPL/CeCIL
   :platform: Unix
   :synopsis: Miscellaneous utility functions.

.. moduleauthor:: Guillaume Levavasseur <glipsl@ipsl.jussieu.fr>


"""
import base64
import json
import os

import requests

from cdf2cim_ws.utils import exceptions
from cdf2cim_ws.utils import constants



# Set of secured endpoints.
_SECURED_ENDPOINTS = {
    '/1/create',
}

# GitHub API - user within GitHub.
_GH_API_USER = "https://api.github.com/user"

# GitHub API - ES-DOC-OPS team membership endpoint.
_GH_API_TEAMS = "https://api.github.com/orgs/ES-DOC-OPS/teams?per_page=100"

# Bare minimum required OAuth scopes.
_REQUIRED_OAUTH_SCOPES = {"read:org"}


def _authenticate(gh_login, oauth_token):
    """Authenticate request against github oauth teams api.

    """
    # Set credentials to be used to authenticate user.
    credentials = (gh_login, oauth_token)

    # Delegate authentication to GitHub user API.
    r = requests.get(_GH_API_USER,
        headers={'Accept': 'application/json'},
        auth=credentials
        )
    if r.status_code != 200:
        raise exceptions.AuthenticationError()

    # Validate OAuth scope(s).
    scopes = set(r.headers['X-OAuth-Scopes'].split(", "))
    if _REQUIRED_OAUTH_SCOPES - scopes:
        raise exceptions.AuthenticationError()

    # Decode user information.
    user = json.loads(r.text)

    print user

    # Return minimal user information.
    return unicode(user['name'].strip()) or gh_login


def _authorize(user_teams):
    """Authorizes access by confirming that a user is a member of appropriate team.

    """
    # Set credentials to be used to pull down set of teams.
    credentials = (os.getenv('CDF2CIM_WS_GITHUB_USER'),
                   os.getenv('CDF2CIM_WS_GITHUB_ACCESS_TOKEN'))

    # Pull set of teams using GitHub organization team API.
    r = requests.get(_GH_API_TEAMS,
        headers={'Accept': 'application/json'},
        auth=credentials
        )
    if r.status_code != 200:
        raise exceptions.AuthorizationError()

    # Set supported teams.
    teams = set([i['name'] for i in json.loads(r.text)])
    teams = [i for i in teams if i.startswith(constants.CDF2CIM_PUBLICATION_GH_TEAM)]
    if team not in teams:
        raise exceptions.AuthorizationError()

    # Return team membership.
    return teams


def secure_request(handler):
    """Enforces request level security policy (if necesaary).

    :param utils.http.HTTPRequestHandler handler: An HTTP request handler.

    :raises: exceptions.AuthenticationError, exceptions.AuthorizationError

    """
    # Escape if not required.
    if not handler.request.path.split("?")[0] in _SECURED_ENDPOINTS:
        return

    # Validate request header.
    # TODO: push to standard header validation
    if 'Authorization' not in handler.request.headers:
        raise exceptions.AuthenticationError()

    # Extract user's GitHub OAuth personal access token from request.
    credentials = handler.request.headers['Authorization']
    credentials = credentials.replace('Basic ', '')
    credentials = base64.b64decode(credentials).split(':')
    gh_login, oauth_token = credentials

    # Authenticate the authorize.
    _authorize(_authenticate(gh_login, oauth_token))

# -*- coding: utf-8 -*-
"""
.. module:: utils.http_validator.py
   :license: GPL/CeCIL
   :platform: Unix
   :synopsis: HTTP request validation.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import json

import jsonschema

from cdf2cim_ws.utils import exceptions
from cdf2cim_ws.schemas import get_schema



def validate_request(handler):
    """Validates request against mapped JSON schemas.

    :param utils.http.HTTPRequestHandler handler: An HTTP request handler.

    :raises: exceptions.SecurityError, exceptions.InvalidJSONError

    """
    for func in {
        _validate_request_cookies,
        _validate_request_files,
        _validate_request_headers,
        _validate_request_params,
        _validate_request_body
        }:
        func(handler)


def _validate_request_cookies(handler):
    """Validates request cookies.

    """
    if len(handler.request.cookies) > 0:
        raise exceptions.RequestValidationException("Unexpected cookies")


def _validate_request_files(handler):
    """Validates request files.

    """
    if len(handler.request.files) > 0:
        raise exceptions.RequestValidationException("Unexpected file attachments")


def _validate_request_headers(handler):
    """Validates request headers against a JSON schema.

    """
    # Map request to schema.
    schema = get_schema('headers', handler.request.path)

    # Null case - escape.
    if schema is None:
        return

    # Validate request headers.
    _validate(handler, dict(handler.request.headers), schema)


def _validate_request_params(handler):
    """Validates request parameters against a JSON schema.

    """
    # Map request to schema.
    schema = get_schema('params', handler.request.path)

    # Null case.
    if schema is None:
        if handler.request.query_arguments:
            raise exceptions.RequestValidationException("Unexpected request url parameters.")

    # Validate request parameters.
    else:
        _validate(handler, handler.request.query_arguments, schema)


def _validate_request_body(handler):
    """Validates request body against a JSON schema.

    """
    # Map request to schema.
    schema = get_schema('body', handler.request.path)

    # Null case.
    if schema is None:
        if handler.request.body:
            raise exceptions.RequestValidationException("Unexpected request body.")

    # Validate request data.
    else:
        # ... decode request data.
        data = json.loads(handler.request.body)

        # ... validate request data against schema.
        _validate(handler, data, schema)

        # ... append valid data to request.
        handler.request.data = data


def _validate(handler, data, schema):
    """Validates data against a JSON schema.

    """
    try:
        jsonschema.validate(data, schema)
    except jsonschema.exceptions.ValidationError as json_errors:
        raise exceptions.InvalidJSONError(json_errors)

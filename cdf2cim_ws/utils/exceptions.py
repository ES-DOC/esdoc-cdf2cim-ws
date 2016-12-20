# -*- coding: utf-8 -*-

"""
.. module:: cdf2cim_ws.exceptions.py
   :platform: Unix
   :synopsis: Custom exceptions used in this module for better readability of code.

.. moduleauthor:: Guillaume Levavasseur <glipsl@ipsl.jussieu.fr>


"""
# Processing error HTTP response code.
_HTTP_RESPONSE_SERVER_ERROR = 500

# Request validation error HTTP response code.
_HTTP_RESPONSE_INVALID_REQUEST_ERROR = 400

# Request authentication error HTTP response code.
_HTTP_UNAUTHENTICATED_ERROR = 401

# Request authorization error HTTP response code.
_HTTP_UNAUTHORIZED_ERROR = 403


class WebServiceError(Exception):
    """Web service error wrapper.

    """
    def __init__(self, msg, response_code):
        """Instance constructor.

        """
        super(WebServiceError, self).__init__(msg)
        self.response_code = response_code


class SecurityError(WebServiceError):
    """Raised if a security issue arises.

    """
    def __init__(self, msg, response_code):
        """Instance constructor.

        """
        super(SecurityError, self).__init__(
            "SECURITY EXCEPTION :: {}".format(msg)
            )
        self.response_code = response_code


class AuthenticationError(SecurityError):
    """Raised when an authentication assertion fails.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(SecurityError, self).__init__(
            "AUTHENTICATION FAILED", _HTTP_UNAUTHENTICATED_ERROR
            )


class AuthorizationError(SecurityError):
    """Raised when an authorization assertion fails.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(SecurityError, self).__init__(
            "AUTHORIZATION FAILED", _HTTP_UNAUTHORIZED_ERROR
            )


class RequestValidationException(WebServiceError):
    """Base class for request validation exceptions.

    """
    def __init__(self, msg):
        """Instance constructor.

        """
        super(RequestValidationException, self).__init__(
            "VALIDATION EXCEPTION :: {}".format(msg), _HTTP_RESPONSE_INVALID_REQUEST_ERROR
            )


class InvalidJSONSchemaError(RequestValidationException):
    """Raised if the submitted HTTP POST data is invalid according to a JSON schema.

    """
    def __init__(self, json_errors):
        """Instance constructor.

        """
        super(InvalidJSONSchemaError, self).__init__(
            'ISSUE HAS INVALID JSON SCHEMA: \n{}'.format(json_errors))

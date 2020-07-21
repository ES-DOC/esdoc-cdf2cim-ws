# -*- coding: utf-8 -*-

"""
.. module:: cdf2cim_ws.exceptions.py
   :platform: Unix
   :synopsis: Custom exceptions used in this module for better readability of code.

.. moduleauthor:: Mark A. Greenslade <momipsl@ipsl.jussieu.fr>


"""
from cdf2cim_ws.utils import constants
from cdf2cim_ws.utils import security



class WebServiceError(Exception):
    """Web service error wrapper.

    """
    def __init__(self, msg, response_code):
        """Instance constructor.

        """
        super(WebServiceError, self).__init__(msg)
        self.response_code = response_code


class RequestValidationException(WebServiceError):
    """Base class for request validation exceptions.

    """
    def __init__(self, msg):
        """Instance constructor.

        """
        super(RequestValidationException, self).__init__(msg, constants.HTTP_RESPONSE_BAD_REQUEST_ERROR)


class InvalidJSONError(RequestValidationException):
    """Raised if the submitted issue post data is invalid according to a JSON schema.

    """
    def __init__(self, json_err):
        """Instance constructor.

        """
        msg = json_err.message.strip()
        try:
            self.field = json_err.path[0]
        except Exception as err:
            self.field = msg.split("'")[1]
        super(InvalidJSONError, self).__init__(msg)


# Map of managed error codes.
ERROR_CODES = {
    InvalidJSONError: 900,
    security.AuthenticationError: 990,
    security.AuthorizationError: 991,
}

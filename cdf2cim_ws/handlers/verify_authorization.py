# -*- coding: utf-8 -*-

"""
.. module:: handlers.verify_membership.py
   :license: GPL/CeCIL
   :platform: Unix
   :synopsis: ES-DOC CDF2CIM - verify GitHub team membership endpoint.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import tornado

from cdf2cim_ws.utils import config
from cdf2cim_ws.utils.http import process_request
from cdf2cim_ws.utils.http_security import apply_policy



# Query parameter names.
_PARAM_LOGIN = 'login'
_PARAM_TOKEN = 'token'


class VerifyAuthorizationRequestHandler(tornado.web.RequestHandler):
    """Authorization request handler.

    """
    def get(self):
        """HTTP GET handler.

        """
        def _verify():
            """Verifies membership.

            """
            if config.apply_security_policy == True:
                apply_policy(
                    self.get_argument(_PARAM_LOGIN),
                    self.get_argument(_PARAM_TOKEN)
                    )


        def _set_output():
            """Sets response to be returned to client.

            """
            self.output = {
                'message': 'User allowed to publish cdf2cim'
            }


        # Process request.
        process_request(self, [
            _verify,
            _set_output
            ])

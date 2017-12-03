# -*- coding: utf-8 -*-

"""
.. module:: handlers.verify_membership.py
   :license: GPL/CeCIL
   :platform: Unix
   :synopsis: ES-DOC CDF2CIM - verify GitHub team membership endpoint.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import datetime as dt
import tornado

import cdf2cim_ws
from cdf2cim_ws.utils import io_manager
from cdf2cim_ws.utils.http import process_request
from cdf2cim_ws.utils.http_security import authenticate



# Query parameter names.
_PARAM_HASH_ID = 'hashid'


class VerifyRequestHandler(tornado.web.RequestHandler):
    """Verifies whether a file has been posted or not.

    """
    def get(self):
        """HTTP GET handler.

        """
        def _verify():
            """Verifies membership.

            """
            self.file_exists = io_manager.file_exists(self.get_argument(_PARAM_HASH_ID))


        def _set_output():
            """Sets response to be returned to client.

            """
            if self.file_exists == True:
                self.output = {
                    "hashid": self.get_argument(_PARAM_HASH_ID),
                    "message": "ES-DOC CDF2CIM cdf2cim file exists",
                    "version": cdf2cim_ws.__version__
                }
            else:
                self.set_status(404)


        # Process request.
        process_request(self, [
            _verify,
            _set_output
            ])

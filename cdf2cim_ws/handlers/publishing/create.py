# -*- coding: utf-8 -*-

"""
.. module:: handlers.create.py
   :license: GPL/CeCIL
   :platform: Unix
   :synopsis: ES-DOC CDF2CIM - create issue endpoint.

.. module author:: Mark A. Greenslade <momipsl@ipsl.jussieu.fr>


"""
import tornado

from cdf2cim_ws.utils.http import process_request



class CreateRequestHandler(tornado.web.RequestHandler):
    """Create CDF2CIM entry request handler.

    """
    def post(self):
        """HTTP POST handler.

        """
        def _set_output():
            """Sets response output.

            """
            self.output = {
                "message": "CDF2CIM-WS security check OK"
            }


        # Process request.
        process_request(self, [
            _set_output,
            ])

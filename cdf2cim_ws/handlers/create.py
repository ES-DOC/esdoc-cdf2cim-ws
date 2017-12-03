# -*- coding: utf-8 -*-

"""
.. module:: handlers.cmip6_simulation.py.py
   :license: GPL/CeCIL
   :platform: Unix
   :synopsis: ES-DOC CDF2CIM - CMIP6 simulation publication handler.

.. module author:: Mark A. Greenslade <momipsl@ipsl.jussieu.fr>


"""
import tornado

from cdf2cim_ws.utils import io_manager
from cdf2cim_ws.utils.http import process_request



class CreateRequestHandler(tornado.web.RequestHandler):
    """Creates a cdf2cim file.

    """
    def post(self):
        """HTTP POST handler.

        """
        def _validate_hashid():
            """Validate hash identifier.

            """
            # TODO - perform same hash compute as on client
            pass


        def _write():
            """Writes cdf2cim content to file system.

            """
            io_manager.write(self.request.data)


        def _set_output():
            """Sets response output.

            """
            self.output = {
                "message": "CDF2CIM-WS: cdf2cim content written to file system"
            }


        # Process request.
        process_request(self, [
            _validate_hashid,
            _write,
            _set_output,
            ])

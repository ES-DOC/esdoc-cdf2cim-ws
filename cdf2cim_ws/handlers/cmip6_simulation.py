# -*- coding: utf-8 -*-

"""
.. module:: handlers.cmip6_simulation.py.py
   :license: GPL/CeCIL
   :platform: Unix
   :synopsis: ES-DOC CDF2CIM - CMIP6 simulation publication handler.

.. module author:: Mark A. Greenslade <momipsl@ipsl.jussieu.fr>


"""
import tornado

from cdf2cim_ws.utils.http import process_request



class CMIP6SimulationRequestHandler(tornado.web.RequestHandler):
    """CMIP5 simulation publication request handler.

    """
    def post(self):
        """HTTP POST handler.

        """
        def _set_output():
            """Sets response output.

            """
            self.output = {
                "message": "CDF2CIM-WS: TODO CMIP6 cdf2cim"
            }


        # Process request.
        process_request(self, [
            _set_output,
            ])

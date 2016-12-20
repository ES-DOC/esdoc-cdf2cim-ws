# -*- coding: utf-8 -*-

"""
.. module:: handlers.create.py
   :license: GPL/CeCIL
   :platform: Unix
   :synopsis: ES-DOC CDF2CIM - create issue endpoint.

.. module author:: Mark A. Greenslade <momipsl@ipsl.jussieu.fr>


"""
import tornado

from cdf2cim_ws.utils import constants
from cdf2cim_ws.utils.constants_json import JF_INSTITUTION_ID
from cdf2cim_ws.utils import exceptions
from cdf2cim_ws.utils.http import process_request



class CreateRequestHandler(tornado.web.RequestHandler):
    """Create CDF2CIM entry request handler.

    """
    def post(self):
        """HTTP POST handler.

        """
        def _validate_user_access():
            """Validates user's institutional access rights.

            """
            # Super & insitutional users have access.
            for team in sorted(self.user_teams):
                if team == constants.ERRATA_GH_TEAM:
                    return
                if team.split("-")[-1] == self.request.data[JF_INSTITUTION_ID].lower():
                    return

            # User has no access rights to this particular issue.
            raise exceptions.AuthorizationError()


        # Process request.
        process_request(self, [
            _validate_user_access,
            ])

# -*- coding: utf-8 -*-
"""

.. module:: app.py
   :license: GPL/CeCIL
   :platform: Unix
   :synopsis: ES-DOC CDF2CIM - web-service entry point.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import tornado.web

from cdf2cim_ws import handlers
from cdf2cim_ws import schemas
from cdf2cim_ws.utils import config
from cdf2cim_ws.utils.logger import log_web as log



def _get_app_endpoints():
    """Returns map of application endpoints to handlers.

    """
    return {
        (r'/', handlers.HeartbeatRequestHandler),
        (r'/verify-authorization', handlers.VerifyAuthorizationRequestHandler),
        (r'/1/cmip5', handlers.CMIP5SimulationRequestHandler),
        (r'/1/cmip6', handlers.CMIP6SimulationRequestHandler)
    }


def _get_app_settings():
    """Returns app settings.

    """
    return {
        "cookie_secret": config.cookie_secret,
        "compress_response": True
    }


def _get_app():
    """Returns application instance.

    """
    # Get set of supported endpoints.
    endpoints = _get_app_endpoints()
    log("Endpoint to handler mappings:")
    for url, handler in sorted(endpoints, key=lambda i: i[0]):
        log("{0} ---> {1}".format(url, str(handler).split(".")[-1][0:-2]))

    # Load endpoints.
    schemas.init([i[0] for i in endpoints])

    return tornado.web.Application(endpoints,
                                   debug=True,
                                   **_get_app_settings())


def run():
    """Runs web service.

    """
    # Initialize application.
    log("Initializing")
    app = _get_app()

    # Open port.
    app.listen(config.port)
    log("Ready")

    # Start processing requests.
    tornado.ioloop.IOLoop.instance().start()


def stop():
    """Stops web service.

    """
    ioloop = tornado.ioloop.IOLoop.instance()
    ioloop.add_callback(lambda x: x.stop(), ioloop)


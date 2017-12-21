# -*- coding: utf-8 -*-
"""

.. module:: constants.py
   :license: GPL/CeCIL
   :platform: Unix
   :synopsis: ES-DOC CDF2CIM - web-service constants.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import os



# HTTP CORS header.
HTTP_HEADER_Access_Control_Allow_Origin = "Access-Control-Allow-Origin"

# Processing error HTTP response codes.
HTTP_RESPONSE_BAD_REQUEST_ERROR = 400
HTTP_RESPONSE_SERVER_ERROR = 500

# I/O directory.
IO_DIR = os.getenv('CDF2CIM_ARCHIVE_HOME')
IO_DIR = os.path.join(IO_DIR, 'data')

# JSON field names.
JF_HASHID = '_hashid'

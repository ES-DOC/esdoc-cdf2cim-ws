# -*- coding: utf-8 -*-
"""
.. module:: cdf2cim_ws.__init__.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Package initializer.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>

"""
__title__ = 'cdf2cim web service'
__version__ = '0.1.0.0'
__author__ = 'ES-DOC'
__license__ = 'GPL'
__copyright__ = 'Copyright 2016: IPSL'

from cdf2cim_ws.app import run
from cdf2cim_ws.app import stop

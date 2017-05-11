# -*- coding: utf-8 -*-

"""
.. module:: utils.io_manager.py
   :license: GPL/CeCIL
   :platform: Unix
   :synopsis: ES-DOC CDF2CIM - I/O manager.

.. module author:: Mark A. Greenslade <momipsl@ipsl.jussieu.fr>


"""
import collections
import json
import os

from cdf2cim_ws.utils.constants import IO_DIR
from cdf2cim_ws.utils.logger import log_web as log



def write(metadata):
    """Write metadata to file system for subsequent processing.

    """
    # Set output directory.
    dpath = IO_DIR
    dpath = os.path.join(dpath, metadata['mip_era'].lower())
    dpath = os.path.join(dpath, metadata['institution_id'].lower())
    dpath = os.path.join(dpath, metadata['source_id'].lower())
    dpath = os.path.join(dpath, metadata['experiment_id'].lower())
    fpath = os.path.join(dpath, "{}.json".format(metadata['_hash_id']))

    # Set output.
    output = collections.OrderedDict()
    for k in sorted(metadata):
        output[k] = metadata[k]

    # Write to file system.
    if not os.path.isdir(dpath):
        os.makedirs(dpath)
    with open(fpath, 'w') as fstream:
        fstream.write(json.dumps(output, indent=4))

    log("cdf2cim file written to: {}".format(fpath))

    return fpath

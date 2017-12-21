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
    # Set output data.
    output = collections.OrderedDict()
    for k in sorted(metadata):
        output[k] = metadata[k]

    # Set output path.
    path = IO_DIR
    path = os.path.join(path, metadata['mip_era'].lower())
    path = os.path.join(path, metadata['institution_id'].lower())
    path = os.path.join(path, metadata['source_id'].lower())
    path = os.path.join(path, metadata['experiment_id'].lower())
    if not os.path.isdir(path):
        os.makedirs(path)
    path = os.path.join(path, "{}.json".format(metadata['_hash_id']))

    # Write.
    with open(path, 'w') as fstream:
        fstream.write(json.dumps(output, indent=4))

    log("cdf2cim file written to: {}".format(path))

    return path


def file_exists(hash_id):
    """Returns flag indicating whether a file with a matching hash identifier exists or not.

    """
    fname = "{}.json".format(hash_id)
    for files in [i[2] for i in os.walk(IO_DIR, False) if len(i[2]) > 0]:
        if fname in files:
            return True

    return False
# -*- coding: utf-8 -*-
"""
.. module:: utils.convertor.py
   :license: GPL/CeCIL
   :platform: Unix
   :synopsis: Conversion utility functions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import collections
import datetime
import json
import re
import time

# Set of types to be ignored when jsonifying.
_IGNOREABLE = (int, float, type(None), str)

# Values considered to be abbreviations.
_ABBREVIATIONS = ("id", "uid", "uuid")

# Default separator.
_DEFAULT_SEPARATOR = "_"

# Set of db coumns that are ignored when converting db entity instances.
_IGNORED_DB_COLUMNS = {'id', 'row_create_date', 'row_update_date'}

# Default dictionary key convertor.
_DEFAULT_KEY_CONVERTOR = lambda k: str(k)



def to_dict(data, key_convertor=_DEFAULT_KEY_CONVERTOR):
    """Converts input data to a dictionary.

    :param object data: Data to be converted.
    :param func key_convertor: Dictionary key formatter.

    :returns: Converted data.
    :rtype: object

    """
    # Ignoreable types.
    if isinstance(data, _IGNOREABLE):
        return data

    # datetime type.
    elif isinstance(data, datetime.datetime):
        return '{}+00:00'.format(str(data)[:19])

    # Dictionaries.
    elif isinstance(data, collections.abc.Mapping):
        return { key_convertor(k): to_dict(v, key_convertor) for k, v in iter(data.items()) }

    # Collections.
    elif isinstance(data, collections.abc.Iterable):
        return [to_dict(i, key_convertor) for i in data]

    else:
        return data


def to_namedtuple(obj, key_convertor=_DEFAULT_KEY_CONVERTOR):
    """Converts a dictionary to a named tuple.

    :param dict obj: Dictionary for conversion.
    :param func key_convertor: Dictionary key convertor.

    :returns: A named tuple.
    :rtype: namedtuple

    """
    obj = to_dict(obj, key_convertor)
    # Convert sub-dictionaries.
    for k, v in obj.items():
        if isinstance(v, dict):
            obj[k] = to_namedtuple(v, key_convertor)

    return collections.namedtuple('_Class', obj.keys())(**obj)


def to_json(data):
    """Converts input dictionary to json.

    :param dict data: Data in dictionary format.
    :param bool sort_keys: Flag indicating whether the dictionary keys will be sorted.

    :returns: JSON encoded string.
    :rtype: str

    """
    return json.dumps(to_dict(data, key_convertor=to_camel_case))


def json_file_to_dict(fpath, key_convertor=_DEFAULT_KEY_CONVERTOR):
    """Converts a json file to a dictionary.

    :param str fpath: A json file path.
    :param func key_convertor: Dictionary key convertor.

    :returns: A dictionary.
    :rtype: dict

    """
    with open(fpath, 'r') as fstream:
        fdata = json.loads(fstream.read())

    return to_dict(fdata, key_convertor)


def json_file_to_namedtuple(fpath, key_convertor=_DEFAULT_KEY_CONVERTOR):
    """Converts a json file to a namedtuple.

    :param str fpath: A json file path.
    :param func key_convertor: Dictionary key convertor.

    :returns: A namedtuple.
    :rtype: namedtuple

    """
    return to_namedtuple(json_file_to_dict(fpath, key_convertor))


def to_pascal_case(target, separator=_DEFAULT_SEPARATOR):
    """Converts a string to pascal case.

    :param str target: A string to be converted.
    :param str separator: A separator used to split target string into parts.

    :returns: The target string converted to pascal case.
    :rtype: str

    """
    result = ''
    if target is not None and len(target):
        if target[0:len(separator)] == separator:
            result = separator
        for text in target.split(separator):
            if text.lower() in _ABBREVIATIONS:
                result += text.upper()
            elif (len(text) > 0):
                result += text[0].upper()
                if (len(text) > 1):
                    result += text[1:]
    return result


def to_camel_case(target, separator=_DEFAULT_SEPARATOR):
    """Converts a string to camel case.

    :param str target: A string to be converted.
    :param str separator: A separator used to split target string into parts.

    :returns: The target string converted to camel case.
    :rtype: str

    """
    result = ''
    if target is not None and len(target):
        text = to_pascal_case(target, separator)
        # Preserve initial separator
        if text[0:len(separator)] == separator:
            result += separator
            text = text[len(separator):]

        # Lower case abbreviations.
        if text.lower() in _ABBREVIATIONS:
            result += text.lower()

        # Lower case initial character.
        elif len(text):
            result += text[0].lower()
            result += text[1:]
    return result

# -*- coding: utf-8 -*-
"""
Module for the creation of setting objects from yaml files
"""
from os import path
import numbers

# Avoid import error during install
try:
    import yaml
except ImportError:
    pass


def from_file(filename):
    """
    Loads a yaml file into an object and returns it
    """
    try:
        with open(filename) as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as exception:
        print('Exception: {}\n'.format(exception))


def update(default_obj, custom_obj):
    """
    Recursively updates data objects, according to the custom settings
    """
    # if simple basic type, return the custom object
    if any((
        isinstance(custom_obj, numbers.Number),
        isinstance(custom_obj, str),
        isinstance(custom_obj, bytes)
    )):
        return custom_obj
    # if mapping type, update every value from the mapping
    try:
        for key, value in custom_obj.items():
            default_value = default_obj.get(key)
            default_obj.update(((key, update(default_value, value)),))
    except Exception as exception:
        print('Exception {}\n'.format(exception))
    return default_obj


def get_settings(setting_path):
    """
    Loads settings from yaml files in a given folder
    default.yaml contains default settings, this file is in SCM (git, ...)
    custom.yaml contains local custom settings which are not in SCM
    """
    default_settings = from_file(path.join(setting_path, 'default.yaml'))
    custom_settings = from_file(path.join(setting_path, 'custom.yaml'))

    return update(default_settings, custom_settings)

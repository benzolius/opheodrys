# -*- coding: UTF-8 -*-
import re
from codecs import open
from os import path

from setuptools import setup

import opheodrys

__author__ = 'benzolius@yahoo.com'


with open('README.md', encoding='utf-8') as file_:
    long_description = file_.read()


with open('requirements.txt', encoding='utf-8') as file_:
    requirements = file_.read().splitlines()


setup(
    name='opheodrys',

    version=opheodrys.__version__,

    description='Flexible configuration system for Python projects',
    long_description=long_description,

    url='https://github.com/benzolius/opheodrys',

    author='Zoltan Benedek',
    author_email='benzolius@yahoo.com',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    packages=['opheodrys'],
    package_dir={'opheodrys': 'opheodrys'},

    install_requires=requirements,

    zip_safe=False,
)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = 'CustomPrint',
    packages = find_packages(
        include=['CustomPrint.py'],
        exclude=['*.txt', '*.md']
    ),
    version = '0.0.2',
    license = "GNU General Public License v3.0",
    description = 'CustomPrint - Python Library Providing Functions for customized print functions.',
    long_description=read('README.md'),
    long_description_content_type="text/markdown",
    author = 'Rodney Shupe',
    author_email = 'rodney@shupe.ca',
    url = 'https://github.com/rodneyshupe/CustomPrint',
    keywords = ['python', 'module', 'library', 'output'],
    classifiers = [
        "Programming Language :: Python :: 3",
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)

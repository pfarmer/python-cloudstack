#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name='cloudstack',
    version='0.1',
    description='A basic cloudstack API library',
    author='Peter Farmer',
    author_email='pfarmer@gmail.com',
    packages=['cloudstack'],
    install_requires=['requests'],
)

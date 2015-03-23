#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name="jenkins-test",
    version="0.1.0",
    author="Simon Castillo",
    author_email="scastb@gmail.com",
    packages=[
        "jenkins-test",
    ],
    include_package_data=True,
    install_requires=[
        "Django==1.7.6",
    ],
    zip_safe=False,
    scripts=["jenkins-test/manage.py"],
)

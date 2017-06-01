#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='oktki',
    version='0.1',
    description='Python wikidoc system',
    author='Gavin Stark',
    author_email='gstark31897@gmail.com',
    url='',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['flask', 'flask-bootstrap'],
)

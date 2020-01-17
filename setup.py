# -*- coding: utf-8 -*-
# Copyright (c) 2018 by Alberto Vara <albertovara@paradigmadigital.com>
import codecs
import os

import json
from setuptools import setup, find_packages

if os.path.exists('README.md'):
    long_description = codecs.open('README.md', 'r', 'utf-8').read()
else:
    long_description = ''



install_requires = []
tests_require = []
if os.path.exists('Pipfile.lock'):
    with open('Pipfile.lock') as fd:
        lock_data = json.load(fd)
        install_requires = [
            package_name + package_data['version']
            for package_name, package_data in lock_data['default'].items()
        ]
        tests_require = [
            package_name + package_data['version']
            for package_name, package_data in lock_data['develop'].items()
        ]

setup(
    name="django-scaffold",
    version="0.0.1",
    author="Alberto Vara",
    author_email="",
    description="Example REST Python Microservices with Django",
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Flask',
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    license="License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    platforms=["any"],
    keywords="",
    url='https://github.com/python-microservices/microservices-django-scaffold',
    packages=find_packages(),
    install_requires=install_requires,
    tests_require=tests_require,
    include_package_data=True,
    zip_safe=True,
)

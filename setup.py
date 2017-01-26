#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import os
from setuptools import setup

setup(
    name='nibelis-dl',
    version='1.0.0',
    description='Download pay slips from Nibelis website',
    url='https://github.com/benoitryder/nibelis-dl',
    author='Benoît Ryder',
    author_email='benoit@ryder.fr',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    py_modules=['nibelis_dl'],
    install_requires=['beautifulsoup4', 'requests', 'html5lib'],
    entry_points={
        'console_scripts': [
            'nibelis-dl = nibelis_dl:main',
        ]
    }
)


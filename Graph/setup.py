#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 10:36:21 2024

@author: cornelius
"""

from setuptools import setup, find_packages

setup(
    name='Graph',                # Name des Pakets
    version='0.1',                      # Version
    packages=find_packages(),           # Automatisches Finden der Pakete
    install_requires=[],                # Abhängigkeiten (falls vorhanden)
    description='Graph',
    author='Cornelius Schätz',
    author_email='schaetzcornelius@gmail.com',
    url='https://github.com/cornelius31415/ALGORITHMS-DATASTRUCTURES', # Optional, wenn das Projekt online gehostet wird
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)

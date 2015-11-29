#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Flake8 putty setup module."""
from __future__ import unicode_literals, with_statement

from setuptools import setup


def get_version(fname='flake8_putty/__init__.py'):
    """Get __version__ from package __init__."""
    with open(fname) as f:
        for line in f:
            if line.startswith('__version__'):
                return eval(line.split('=')[-1])


def get_long_description():
    """Load README.rst."""
    descr = []
    for fname in ('README.rst',):
        with open(fname) as f:
            descr.append(f.read())
    return '\n\n'.join(descr)


setup(
    name='flake8-putty',
    version=get_version(),
    description='Apply a bit of putty to flake8.',
    long_description=get_long_description(),
    keywords='flake8 pep8 putty',
    author='John Vandenberg',
    author_email='jayvdb@gmail.com',
    url='https://github.com/jayvdb/flake8-putty',
    install_requires=[
        'flake8>=2.4.1',
    ],
    license='MIT',
    packages=[str('flake8_putty')],
    zip_safe=False,
    entry_points={
        'flake8.extension': [
            'flake8_putty = flake8_putty:PuttyExtension',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Quality Assurance',
    ],
)
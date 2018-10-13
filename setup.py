#!/usr/bin/env python
import os

from setuptools import setup, find_packages

def read (filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()

setup(
    name='Block_Fund_Trading',
    version='1.1',
    packages= find_packages(),
    description='ICO-python-trading',
    url='',
    author='Maarten Elgar',
    author_email='maartenelgar12@gmail.com',
    install_requires=['requests', 'six', 'Twisted', 'pyOpenSSL', 'autobahn', 'service-identity', 'dateparser', 'urllib3', 'chardet', 'certifi', 'cryptography', 'pandas', 'numpy', 'sys' ],
    keywords='',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)

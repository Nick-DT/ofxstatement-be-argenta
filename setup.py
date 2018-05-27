#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from setuptools import find_packages
from distutils.core import setup

version = '0.0.3'
with open('README.rst', encoding = "utf-8") as f:
    long_description = f.read()

setup(name='ofxstatement-be-argenta',
      version=version,
      author='Wout Br',
      author_email='35967233+woutbr@users.noreply.github.com ',
      url='https://github.com/woutbr/ofxstatement-be-argenta',
      description=('ofxstatement plugin for Argenta'),
      long_description=long_description,
      license='MIT',
      keywords=['ofx', 'ofxstatement', 'argenta'],
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Programming Language :: Python :: 3',
          'Natural Language :: English',
          'Topic :: Office/Business :: Financial :: Accounting',
          'Topic :: Utilities',
          'Environment :: Console',
          'Operating System :: OS Independent'
      ],
      packages=['ofxstatement', 'ofxstatement.plugins'],
      namespace_packages=['ofxstatement', 'ofxstatement.plugins'],
      entry_points={
          'ofxstatement': ['argenta = ofxstatement.plugins.argenta:ArgentaPlugin']
      },
      install_requires=['ofxstatement', 'openpyxl'],
      test_suite='ofxstatement.plugins.tests',
      include_package_data=True,
      zip_safe=True
      )

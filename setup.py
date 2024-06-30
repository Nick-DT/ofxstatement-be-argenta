#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from setuptools import find_packages
from distutils.core import setup

version = '1.0.6'
with open('README.rst', encoding = "utf-8") as f:
    long_description = f.read()

setup(name='ofxstatement-be-argenta',
      version=version,
      author="Nicolas Dt",
      author_email="6697462+Nick-DT@users.noreply.github.com",
      url="https://github.com/Nick-DT/ofxstatement-be-bnp",
      description=('ofxstatement plugin for Argenta, updated for french version'),
      long_description=long_description,
      long_description_content_type='text/x-rst',
      license='MIT',
      keywords=['ofx', 'ofxstatement', 'argenta'],
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Programming Language :: Python :: 3',
          'Natural Language :: English',
          'Topic :: Office/Business :: Financial :: Accounting',
          'Topic :: Utilities',
          'Environment :: Console',
          'Operating System :: OS Independent',
          'License :: OSI Approved :: MIT License',
      ],
      packages=find_packages(),
      namespace_packages=['ofxstatement', 'ofxstatement.plugins'],
      entry_points={
          'ofxstatement': ['argenta = ofxstatement.plugins.argenta:ArgentaPlugin'],
          'console_scripts': ['ofx-argenta-convert = ofxstatement_be_argenta.convert:convert']
      },
      install_requires=[
          'ofxstatement>=0.6.1',
          'openpyxl>=2.6.2',
          'click>=6.7'
      ],
      test_suite='ofxstatement.plugins.tests',
      include_package_data=True,
      zip_safe=True
      )

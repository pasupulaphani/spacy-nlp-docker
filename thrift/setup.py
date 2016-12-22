#!/usr/bin/env python

from setuptools import setup

setup(name='spacy-thrift',
      version='0.0.2',
      description='spaCy using Thrift',
      keywords='natural language processing',
      classifiers=[
          "License :: OSI Approved :: MIT License",
          "Topic :: Text Processing",
      ],
      packages=['spacyThrift'],
      install_requires=["thrift", "spacy"])

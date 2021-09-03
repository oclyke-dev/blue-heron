#!/usr/bin/env python3

from setuptools import setup

setup(
  name='blue_heron',
  version='0.0.0',
  packages=[
    'blue_heron',
    'blue_heron.test',
  ],
  scripts=[
    'blue_heron/bin/hello.py',
  ],
  package_data={
    'blue_heron': [
      'data/example_data.txt',
    ],
  },
)

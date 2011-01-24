#!/usr/bin/env python
from setuptools import setup


setup(name='quickdiagrams',
  version='0.2',
  description='A text-to-class_diagram conversion tool.',
  author='Hugo Ruscitti',
  author_email='hugoruscitti@gmail.com',
  packages=['quickdiagrams', 'quickclassdiagrams.gtkclient'],
  scripts=['bin/quickclassdiagram'],
  )

#!/usr/bin/env python
from setuptools import setup

# Put here required packages or
# Uncomment one or more lines below in the install_requires section
# for the specific client drivers/modules your application needs.
packages = [
            'flask',
#            'flask-assets',
            'flask-babel',
            'lettuce'
           ]

setup(name='Vasco', version='1.0',
      description='Vasco travel manegement platform',
      author='Maksym Borodin', author_email='borodin.maksym@gmail.com',
      url='https://pypi.python.org/pypi',
      install_requires=packages,
     )

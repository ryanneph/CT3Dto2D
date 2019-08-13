#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='CT3Dto2D',
      version='1.0',
      description='Utility for converting a CT volume from a single 3D dicom file to the standard set of 2D dicom slice files',
      author='Ryan Neph',
      author_email='neph320@gmail.com',
      url='https://github.com/ryanneph/CT3Dto2D',
      packages=find_packages(),
      entry_points={
          'console_scripts': [
              'ct3dto2d = ct3dto2d.__main__:main'
          ],
      },
      install_requires=[
          'numpy',
          'pydicom',
          'rttypes @ git+http://github.com/ryanneph/rttypes.git@v1.0',
      ]
      )

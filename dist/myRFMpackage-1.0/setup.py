#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 13:34:10 2017

@author: sylviaschumacher
"""
##%%
#from distutils.core import setup
#setup(name='myRFMpackage',
#      version='1.0',
#      py_modules=['myRFMpackage'],
#      zip_safe=False
#      )
#%%

    
from setuptools import setup
def readme():
    with open('README.rst') as f:
        return f.read()
#from distutils.core import setup
setup(name='myRFMpackage',
      version='1.0',
      #py_modules=['myRFMpackage.calculateRFM'],
      zip_safe=False,
      install_requires=['pandas','numpy'],   
      packages=['myRFMpackage'],
      )
#
#%%
#setup(name='myRFMpackage',
#      description='What the package does',     
#      version='1.0',
#      #py_modules=['myRFMpackage.calculateRFM'],
#      install_requires=['pandas','numpy'],
#      author='Sylvia Schumacher')
#%%
#import myRFMpackage
#%%
#myRFMpackage.joke()
#%%
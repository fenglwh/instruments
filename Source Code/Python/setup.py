#!/usr/bin/python
# coding:utf-8
__Author__ = 'Adair.l'
from setuptools import setup, find_packages
with open("README.md", "r") as fh:
    long_description = fh.read()
setup(
    name='labinstrument',
    version        = '0.0.9',
    description='''This is a package for Communication lab instrument romote control''',
    long_description=long_description,
    author='adair',
    author_email='adair@byadair.com',
    maintainer='adair',
    maintainer_email='adair@byadair.com',
    license='GPL or contact me',
    packages=find_packages(),
    platforms=["all"],
    url='not prepared yet',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPL License",
        "Operating System :: OS Independent",
    ],
)

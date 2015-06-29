# -*- coding: utf-8 -*-
__author__ = 'yueg'

from setuptools import setup, find_packages

setup(
    name = 'mySpider',
    version='1.0',
    packages=find_packages(),
    entry_points={'scrapy': ['settings = fun.settings']}, requires=['requests', 'scrapy']
)

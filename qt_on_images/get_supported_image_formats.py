#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
get PySide supported image formats

If it doesn't contains 'jpeg'/'jpg', you have to re-install jpeg/openjpeg and qt packages

    brew install jpeg
    brew install openjpeg
    brew install qt

Tested environment:
    Mac OS X 10.6.8
"""

from PySide import QtGui

fmts = [str(i) for i in QtGui.QImageReader.supportedImageFormats()]
print fmts
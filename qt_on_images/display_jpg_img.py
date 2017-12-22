#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
display jpeg image

Tested environment:
    Mac OS X 10.6.8
"""

import os
import sys

from PySide import QtGui

PWD = os.path.dirname(os.path.realpath(__file__))
parent_path = os.path.dirname(PWD)
IM_RES_PATH = os.path.join(os.path.dirname(parent_path), "image_resources")


file_path = os.path.join(IM_RES_PATH, "captcha.jpg")


app = QtGui.QApplication(sys.argv)

x, y, w, h = 100, 100, 200, 200
label = QtGui.QLabel()
label.setGeometry(x, y, w, h)
pixmap = QtGui.QPixmap(file_path)
label.setPixmap(pixmap)
label.move(10, 10)
label.show()

sys.exit(app.exec_())
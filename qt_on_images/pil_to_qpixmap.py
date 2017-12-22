#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
QPixmap load image by PIL, pil2qpixmap

Tested environment:
    Mac OS X 10.6.8

References

 - http://stackoverflow.com/questions/6756820/python-pil-image-tostring
 - http://qt-project.org/forums/viewthread/5866
"""
import os
import sys

from PIL import Image
from PySide import QtGui


PWD = os.path.dirname(os.path.realpath(__file__))
parent_path = os.path.dirname(PWD)
IM_RES_PATH = os.path.join(os.path.dirname(parent_path), "image_resources")
file_path = os.path.join(IM_RES_PATH, "captcha.jpg")


def pil2pixmap(file_path):
    im = Image.open(fp = file_path)
    if im.mode == "RGB":
        pass
    elif im.mode == "L":
        im = im.convert("RGBA")
    data = im.tostring('raw', "RGBA")
    qim = QtGui.QImage(data, im.size[0], im.size[1], QtGui.QImage.Format_ARGB32)
    pixmap = QtGui.QPixmap.fromImage(qim)
    return pixmap


app = QtGui.QApplication(sys.argv)

x, y, w, h = 100, 100, 200, 200
label = QtGui.QLabel()
label.setGeometry(x, y, w, h)

pixmap = pil2pixmap(file_path)
label.setPixmap(pixmap)

label.move(10, 10)
label.show()

sys.exit(app.exec_())
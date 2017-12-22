#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
QPixmap imageConversionFlags demo

Tested environment:
    Mac OS X 10.6.8
    
"""
import sys

try:
    from PySide import QtCore
    from PySide import QtGui
except ImportError:
    from PyQt4 import QtCore
    from PyQt4 import QtGui


class Demo(QtGui.QWidget):
    def __init__(self):
        super(Demo, self).__init__()

        x, y, w, h = 500, 200, 300, 400
        self.setGeometry(x, y, w, h)

        path = "captcha.jpg"
        pix = QtGui.QPixmap(path, flags = QtCore.Qt.MonoOnly)

        label = QtGui.QLabel("foo", self)
        label.setPixmap(pix)
        label.move(10, 10)


    def show_and_raise(self):
        self.show()
        self.raise_()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    demo = Demo()
    demo.show_and_raise()

    sys.exit(app.exec_())
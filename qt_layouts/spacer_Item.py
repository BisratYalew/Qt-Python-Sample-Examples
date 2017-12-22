#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
QSpacerItem demo

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


class Demo(QtGui.QDialog):
    def __init__(self):
        super(Demo, self).__init__()

        x, y, w, h = 500, 200, 300, 400
        self.setGeometry(x, y, w, h)
        
        hbox = QtGui.QHBoxLayout()
        
        a_btn = QtGui.QPushButton('a')
        hbox.addWidget(a_btn)

        hbox.addSpacerItem(QtGui.QSpacerItem(100, 50))

        b_btn = QtGui.QPushButton('b')
        hbox.addWidget(b_btn)

        style = "QPushButton { border: 3px solid red }; "
        self.setStyleSheet(style)
                
        self.setLayout(hbox)
        
    def show_and_raise(self):
        self.show()
        self.raise_()

        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    demo = Demo()
    demo.show()

    app.exec_()


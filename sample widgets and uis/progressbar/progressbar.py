#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

try:
    from PySide import QtCore
    from PySide import QtGui
except ImportError:
    from PyQt4 import QtCore
    from PyQt4 import QtGui



class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()

        self.pbar = QtGui.QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)
        self.pbar.setMaximum(0)
        self.pbar.setMinimum(0)
        self.show()

if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    assert ex != None
    app.exec_()
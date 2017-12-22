#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
popup multi levels menu by right click

Tested environment:
    Mac OS X 10.6.8

http://developer.qt.nokia.com/doc/qt-4.8/qmenu.html#details
http://diotavelli.net/PyQtWiki/Handling%20context%20menus
"""
import sys

try:
    from PySide import QtCore
    from PySide import QtGui
except ImportError:
    from PyQt4 import QtCore
    from PyQt4 import QtGui


class Demo(QtGui.QMainWindow):
    def __init__(self):
        super(Demo, self).__init__()

        x, y, w, h = 500, 200, 300, 400
        self.setGeometry(x, y, w, h)

        self.popup_menu = QtGui.QMenu(self)

        # sub-menu
        self.sub_menu = self.popup_menu.addMenu("sub-menu")
        print "sub_menu:", self.sub_menu

        self.item_add_act = QtGui.QAction("Add", self)
        self.item_add_act.triggered.connect(self.add_cb)
        self.sub_menu.addAction(self.item_add_act)

    def add_cb(self):
        print "add callback"

    def contextMenuEvent(self, event):
        point = self.mapToGlobal(event.pos())
        act = self.popup_menu.exec_(point)

        if act == self.item_add_act:
            print "item add clicked"

        return super(Demo, self).contextMenuEvent(event)

    def show_and_raise(self):
        self.show()
        self.raise_()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    demo = Demo()
    demo.show_and_raise()

    sys.exit(app.exec_())
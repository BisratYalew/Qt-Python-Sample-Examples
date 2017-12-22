#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
popup menu by right click

Tested environment:
    Mac OS X 10.6.8

http://developer.qt.nokia.com/doc/qt-4.8/qmenu.html#details
http://diotavelli.net/PyQtWiki/Handling%20context%20menus
"""
import sys

try:
    from PySide import QtCore, QtGui
except ImportError:
    from PyQt4 import QtCore, QtGui


class Demo(QtGui.QMainWindow):
    def __init__(self):
        super(Demo, self).__init__()

        x, y, w, h = 500, 200, 300, 400
        self.setGeometry(x, y, w, h)


        self.popup_menu = QtGui.QMenu(self)

        # menu item
        self.item_add_act = QtGui.QAction("Add", self)
        self.item_add_act.triggered.connect(self.add_cb)
        self.popup_menu.addAction(self.item_add_act)

        self.item_delete_act = QtGui.QAction("Delete", self)
        self.item_delete_act.triggered.connect(self.delete_cb)
        self.popup_menu.addAction(self.item_delete_act)

        self.popup_menu.addSeparator()

        self.item_rename_act = QtGui.QAction("Rename", self)
        self.item_rename_act.triggered.connect(self.rename_cb)
        self.popup_menu.addAction(self.item_rename_act)

    def add_cb(self):
        print "add callback"

    def delete_cb(self):
        print "delete callback"

    def rename_cb(self):
        print "rename callback"

    def contextMenuEvent(self, event):
        point = self.mapToGlobal(event.pos())
        act = self.popup_menu.exec_(point)

        if act == self.item_add_act:
            print "item add clicked"
        elif act == self.item_delete_act:
            print "item delete clicked"
        elif act == self.item_rename_act:
            print "item rename clicked"

        return super(Demo, self).contextMenuEvent(event)

    def show_and_raise(self):
        self.show()
        self.raise_()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    demo = Demo()
    demo.show_and_raise()

    sys.exit(app.exec_())
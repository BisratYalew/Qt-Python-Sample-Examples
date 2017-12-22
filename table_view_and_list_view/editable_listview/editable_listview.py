#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
editable item in QListView

Tested environment:
    Mac OS X 10.6.8

http://developer.qt.nokia.com/doc/qt-4.7/qabstractlistmodel.html
"""
import sys

try:
    from PySide import QtCore
    from PySide import QtGui
except ImportError:
    from PyQt4 import QtCore
    from PyQt4 import QtGui

    

class ListModel(QtCore.QAbstractListModel):
    def __init__(self, data_items):
        super(ListModel, self).__init__()
        self.data_items = data_items

    def rowCount(self, parent):
        return len(self.data_items)

    def data(self, index, role = QtCore.Qt.DisplayRole):
        if not index.isValid():
            return None

        name = self.data_items[index.row()]
        if role == QtCore.Qt.DisplayRole:
            return name

        return None

    def flags(self, index):
        return QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

    def setData(self, index, value, role):
        if role == QtCore.Qt.EditRole:
            row = index.row()
            self.data_items[row] = value

        return super(ListModel, self).setData(index, value, role)


class Demo(QtGui.QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        
        x, y, w, h = 500, 200, 300, 400
        self.setGeometry(x, y, w, h)

        self.list_view = QtGui.QListView(self)
        x, y, w, h = 5, 5, 290, 250
        self.list_view.setGeometry(x, y, w, h)

        data_sources = ['a', 'b', 'c']
        list_model = ListModel(data_sources)
        self.list_view.setModel(list_model)

    def show_and_raise(self):
        self.show()
        self.raise_()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    demo = Demo()
    demo.show_and_raise()

    sys.exit(app.exec_())
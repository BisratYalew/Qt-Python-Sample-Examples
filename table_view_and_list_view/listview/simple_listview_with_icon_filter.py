#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
Custom QListView


This script demonstrates

 - custom icon for item
 - change item data at runtime

Tested environment:
    Mac OS X 10.6.8

Docs
 - http://www.pyside.org/docs/pyside/PySide/QtGui/QAbstractItemView.html
 - http://www.pyside.org/docs/pyside/PySide/QtGui/QListView.html
 - http://doc.qt.nokia.com/latest/model-view-programming.html
"""
import glob
import os
import sys

#try:
#    from PySide import QtCore
#    from PySide import QtGui
#except ImportError:
#    from PyQt4 import QtCore
#    from PyQt4 import QtGui

from PyQt4 import QtCore
from PyQt4 import QtGui


class ListModel(QtCore.QAbstractListModel):
    def __init__(self, os_list):
        super(ListModel, self).__init__()
        self.os_list = os_list

    def rowCount(self, parent):
#        print ">>> rowCount"
#        print 'parent:', parent,
#        print ', row:', parent.row(),
#        print ', column:', parent.column(),
#        print ', internalPointer:', parent.internalPointer()
        
        return len(self.os_list)

    def data(self, index, role = QtCore.Qt.DisplayRole):
#        print ">>> data"
#        print 'isValid:', index.isValid(),
#        print ', row:', index.row(),
#        print ', column:', index.column(),
#        print ', is Qt.DisplayRole:', role == QtCore.Qt.DisplayRole

        if not index.isValid():
            return None

        os_name, os_logo_path = self.os_list[index.row()]
        if role == QtCore.Qt.DisplayRole:
            return os_name
        elif role == QtCore.Qt.DecorationRole:
            return QtGui.QIcon(os_logo_path)

        return None


def create_data_source():
    logos = glob.glob('*.png')
    return [(os.path.splitext(i)[0], i) for i in logos]


class Demo(QtGui.QWidget):
    def __init__(self):
        super(Demo, self).__init__()

        x, y, w, h = 500, 200, 300, 400
        self.setGeometry(x, y, w, h)


        self.list_view = QtGui.QListView(self)
        x, y, w, h = 5, 5, 290, 250
        self.list_view.setGeometry(x, y, w, h)

        self.data_sources = create_data_source()
        list_model = ListModel(self.data_sources)
        self.list_view.setModel(list_model)

        # size
        self.list_view.setIconSize(QtCore.QSize(50, 50))
        self.list_view.setSpacing(5)
        self.list_view.setUniformItemSizes(True)

        # view
#        self.list_view.setViewMode(QtGui.QListView.IconMode)

        # interactive
        self.list_view.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)

        # more advanced controlling on selection
#        self.selection_model = self.list_view.selectionModel()
#        self.selection_model.currentChanged.connect(self._selection_model_currentChanged)


        self.lineedit = QtGui.QLineEdit(self)
        self.lineedit.move(5, 260)
        self.lineedit.textEdited.connect(self._lineedit_textEdited)


    def _lineedit_textEdited(self, text):
        if not text:
            self.list_view.clearSelection()
        else:
            self.list_view.keyboardSearch(text)
            idx = self.list_view.currentIndex()
            if idx.isValid():
                if len(self.data_sources) - 1 >= idx.row():
                    self.data_sources.pop(idx.row())
                    self.list_view.update()

    def show_and_raise(self):
        self.show()
        self.raise_()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    demo = Demo()
    demo.show_and_raise()

    sys.exit(app.exec_())
#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
Custom QListView

This script demonstrates

 - DND item
 - sort item

Tested environment:
    Mac OS X 10.6.8

Docs

 - http://doc.qt.nokia.com/latest/model-view-programming.html#using-drag-and-drop-with-item-views

 - Qt - QAbstractItemView, PySide - QListView
 - Qt - QAbstractItemModel, PySide - QAbstractItemModel
"""
import glob
import os
import sys

try:
    from PySide import QtCore
    from PySide import QtGui
except ImportError:
    from PyQt4 import QtCore
    from PyQt4 import QtGui


class ListModel(QtCore.QAbstractListModel):
    def __init__(self, os_list):
        super(ListModel, self).__init__()
        self.os_list = os_list

    def rowCount(self, parent):
        return len(self.os_list)

    def data(self, index, role = QtCore.Qt.DisplayRole):
        if not index.isValid():
            return None

        os_name, os_logo_path = self.os_list[index.row()]
        if role == QtCore.Qt.DisplayRole:
            return os_name
        elif role == QtCore.Qt.DecorationRole:
            return QtGui.QIcon(os_logo_path)

        return None

    def flags(self, idx):
        if idx.isValid():
            return QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsDropEnabled |\
                   QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
        else:
            return QtCore.Qt.ItemIsDropEnabled |\
                   QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled

    def supportedDropActions(self):
        return QtCore.Qt.MoveAction

    def mimeData(self, idxes):
        # NOTE: create mime data from ancestor method for fixed crash bug on PySide
        mime_data = super(ListModel, self).mimeData(idxes)

        encoded_data = ""

        for idx in idxes:
            if idx.isValid():
                encoded_data += '\r\n' + self.data(idx, role = QtCore.Qt.DisplayRole)

        mime_data.setData('text/plain', encoded_data)

        return mime_data



class ListView(QtGui.QListView):
    def __init__(self, parent=None):
        super(ListView, self).__init__(parent)

        self.data_sources = create_data_source()
        list_model = ListModel(self.data_sources)
        self.setModel(list_model)

        # size
        self.setIconSize(QtCore.QSize(50, 50))
        self.setSpacing(5)
        self.setUniformItemSizes(True)

        # view
        self.setDropIndicatorShown(True)

        # interactive in DND mode
        self.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.setDragDropMode(QtGui.QAbstractItemView.DragDrop)
        self.setDragEnabled(True)
        self.setAcceptDrops(True)

    def dropEvent(self, evt):
        mime_data = evt.mimeData()

        if mime_data.hasFormat('text/plain'):
            buf = mime_data.data('text/plain')
            print 'pos:', evt.pos()
            print "source == self:", evt.source() == self
            print 'mime data:', repr(buf)

        return super(ListView, self).dropEvent(evt)


def create_data_source():
    logos = glob.glob('*.png')
    return [(os.path.splitext(i)[0], i) for i in logos]


class Demo(QtGui.QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        x, y, w, h = 500, 200, 300, 400
        self.setGeometry(x, y, w, h)


        self.list_view = ListView(self)
        x, y, w, h = 5, 5, 290, 250
        self.list_view.setGeometry(x, y, w, h)

    def show_and_raise(self):
        self.show()
        self.raise_()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    demo = Demo()
    demo.show_and_raise()

    sys.exit(app.exec_())
#!/usr/bin/env python
"""
demo template

Tested environment:
    Mac OS X 10.6.8
"""
import os, sys
from PySide import QtCore, QtGui

PWD = os.path.dirname(os.path.realpath(__file__))
img_res_prefix = os.path.join(os.path.dirname(PWD), "image_resources")

files = [
    os.path.join(img_res_prefix, "Mac.png"),
    os.path.join(img_res_prefix, "Ubuntu.png"),
    ]
g_cursor = 0

def get_next_img_file_path():
    global g_cursor
    g_cursor += 1
    if g_cursor == 2:
        g_cursor = 0
    return files[g_cursor]

class Demo(QtGui.QWidget):
    def __init__(self):
        super(Demo, self).__init__()

        x, y, w, h = 500, 200, 400, 400
        self.setGeometry(x, y, w, h)
        self.setStyleSheet("QLabel { border: 1px solid red; }")

        self.label = QtGui.QLabel("hello", self)
        self.label.move(20, 20)

        self.btn = QtGui.QPushButton("switch without adjusting size", self)
        self.btn.clicked.connect(self._btn_cb)
        self.btn.move(50, 300)

        self.btn_adjust = QtGui.QPushButton("switch with adjusting size", self)
        self.btn_adjust.clicked.connect(self._btn_adjust_cb)
        self.btn_adjust.move(50, 350)

    def _btn_cb(self, *args, **kwargs):
        pix = QtGui.QPixmap(get_next_img_file_path())

        print "QPixmap size = ", pix.size()
        print "QLabel size = ", self.label.size()
        self.label.setPixmap(pix)
        print "QLabel size (setPixmap called) = ", self.label.size()

    def _btn_adjust_cb(self, *args, **kwargs):
        pix = QtGui.QPixmap(get_next_img_file_path())

        print "QPixmap size = ", pix.size()
        print "QLabel size = ", self.label.size()
        self.label.setPixmap(pix)
        self.label.adjustSize()
        print "QLabel size (setPixmap && adjustSize called) = ", self.label.size()

    def show_and_raise(self):
        self.show()
        self.raise_()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    demo = Demo()
    demo.show_and_raise()

    sys.exit(app.exec_())

"""
Qt Style Sheet
"""
import sys
from PySide import QtGui

app = QtGui.QApplication(sys.argv)

win = QtGui.QWidget()
x, y, w, h = 100, 100, 200, 50
win.setGeometry(x, y, w, h)

label = QtGui.QLabel("hello", win)
label.move(10, 10)


css = "QLabel { border: 1px solid red; color: blue; }"
win.setStyleSheet(css)

win.show()
win.raise_()

sys.exit(app.exec_())
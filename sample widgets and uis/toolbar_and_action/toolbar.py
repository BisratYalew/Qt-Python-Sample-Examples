#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
QToolBar and QAction demo

Tested environment:
    Mac OS X 10.6.8


http://doc.qt.nokia.com/latest/qaction.html
http://www.pyside.org/docs/pyside/PySide/QtGui/QToolBar.html
http://www.pyside.org/docs/pyside/PySide/QtGui/QAction.html
http://www.devbean.info/2011/08/native-style-qt-8/

"""
import sys

try:
    from PySide import QtCore
    from PySide import QtGui
except ImportError:
    from PyQt4 import QtCore
    from PyQt4 import QtGui

def config_theme_path():
    if sys.platform != "darwin":
        return

    theme_name = str(QtGui.QIcon.themeName())

    if theme_name != "Oxygen":
        QtGui.QIcon.setThemeName("Oxygen")


    search_paths = list(QtGui.QIcon.themeSearchPaths())

    custom_path = "/opt/local/share/icons"
    if custom_path not in search_paths:
        search_paths.append(custom_path)

    QtGui.QIcon.setThemeSearchPaths(search_paths)


class Demo(QtGui.QMainWindow):
    def __init__(self):
        super(Demo, self).__init__()
        x, y, w, h = 500, 200, 300, 400
        self.setGeometry(x, y, w, h)
        self.setUnifiedTitleAndToolBarOnMac(True)

        config_theme_path()
        icon = QtGui.QIcon.fromTheme('application-exit')

        exit_a = QtGui.QAction(icon, 'Exit', self)
        exit_a.setShortcut('Ctrl+Q')
#        self.connect(exit_a, QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()'))
        exit_a.triggered.connect(self.close)


        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exit_a)

        self._toolbar = toolbar

    def show_and_raise(self):
        self.show()
        self.raise_()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    demo = Demo()
    demo.show_and_raise()

    sys.exit(app.exec_())
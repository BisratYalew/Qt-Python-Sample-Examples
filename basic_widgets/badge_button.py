#!/usr/bin/env python
"""
Qt Notification Badge

References

 - http://th30z.blogspot.com/2008/10/cocoa-notification-badge_127.html
 - http://khertan.net/blog/qbadgebutton_a_qpushbutton_with_a_badge_counter

origin version it here
http://khertan.net/blog/qbadgebutton_a_qpushbutton_with_a_badge_counter
"""
import sys

try:
    from PySide import QtGui, QtCore
except ImportError:
    from PyQt4 import QtGui, QtCore
    
 
class QBadgeButton(QtGui.QPushButton): 
    def __init__(self, icon = None, text = None, parent = None):
        if icon:
            QtGui.QPushButton.__init__(self, icon, text, parent)
        elif text:
            QtGui.QPushButton.__init__(self, text, parent)
        else:
            QtGui.QPushButton.__init__(self, parent)
 
        self.badge_counter = 0
        self.badge_size = 50
 
        self.redGradient = QtGui.QRadialGradient(0.0, 0.0, 17.0, self.badge_size - 3, self.badge_size - 3);
        self.redGradient.setColorAt(0.0, QtGui.QColor(0xe0, 0x84, 0x9b));
        self.redGradient.setColorAt(0.5, QtGui.QColor(0xe9, 0x34, 0x43));
        self.redGradient.setColorAt(1.0, QtGui.QColor(0xdc, 0x0c, 0x00));
 
    def setSize(self, size):
        self.badge_size = size
 
    def setCounter(self, counter):
        self.badge_counter = counter
        self.update()
 
    def paintEvent(self, event):
        QtGui.QPushButton.paintEvent(self, event)
        p = QtGui.QPainter(self)
        p.setRenderHint(QtGui.QPainter.TextAntialiasing)
        p.setRenderHint(QtGui.QPainter.Antialiasing)
 
        if self.badge_counter > 0:
            point = self.rect().topRight()
            self.drawBadge(p,
                           point.x()-self.badge_size - 1,
                           point.y() + 1,
                           self.badge_size,
                           str(self.badge_counter),
                           QtGui.QBrush(self.redGradient))
 
    def fillEllipse(self, painter, x, y, size, brush):
        path = QtGui.QPainterPath()
        path.addEllipse(x, y, size, size);
        painter.fillPath(path, brush);
 
    def drawBadge(self, painter, x, y, size, text, brush):
        painter.setFont(QtGui.QFont(painter.font().family(), 11, QtGui.QFont.Bold))
 
        while ((size - painter.fontMetrics().width(text)) < 10):
            pointSize = painter.font().pointSize() - 1
            weight = QtGui.QFont.Normal if (pointSize < 8) else QtGui.QFont.Bold
            painter.setFont(QtGui.QFont(painter.font().family(), painter.font().pointSize() - 1, weight))
 
        shadowColor = QtGui.QColor(0, 0, 0, size)
        self.fillEllipse(painter, x + 1, y, size, shadowColor)
        self.fillEllipse(painter, x - 1, y, size, shadowColor)
        self.fillEllipse(painter, x, y + 1, size, shadowColor)
        self.fillEllipse(painter, x, y - 1, size, shadowColor)
 
        painter.setPen(QtGui.QPen(QtCore.Qt.white, 2));
        self.fillEllipse(painter, x, y, size - 3, brush)
        painter.drawEllipse(x, y, size - 3, size - 3)
 
        painter.setPen(QtGui.QPen(QtCore.Qt.white, 1));
        painter.drawText(x, y, size - 2, size - 2, QtCore.Qt.AlignCenter, text);
 
        
class QToolBadgeButton(QtGui.QToolButton):
    def __init__(self, parent = None):
        QtGui.QToolButton.__init__(self, parent)
 
        self.badge_counter = 0
        self.badge_size = 25
 
        self.redGradient = QtGui.QRadialGradient(0.0, 0.0, 17.0, self.badge_size - 3, self.badge_size - 3);
        self.redGradient.setColorAt(0.0, QtGui.QColor(0xe0, 0x84, 0x9b));
        self.redGradient.setColorAt(0.5, QtGui.QColor(0xe9, 0x34, 0x43));
        self.redGradient.setColorAt(1.0, QtGui.QColor(0xdc, 0x0c, 0x00));
 
    def setSize(self, size):
        self.badge_size = size
 
    def setCounter(self, counter):
        self.badge_counter = counter
 
    def paintEvent(self, event):
        QtGui.QToolButton.paintEvent(self, event)
        p = QtGui.QPainter(self)
        p.setRenderHint(QtGui.QPainter.TextAntialiasing)
        p.setRenderHint(QtGui.QPainter.Antialiasing)
        if self.badge_counter > 0:
            point = self.rect().topRight()
            self.drawBadge(p,
                           point.x()-self.badge_size, point.y(),
                           self.badge_size,
                           str(self.badge_counter),
                           QtGui.QBrush(self.redGradient))
 
    def fillEllipse(self, painter, x, y, size, brush):
        path = QtGui.QPainterPath()
        path.addEllipse(x, y, size, size);
        painter.fillPath(path, brush);
 
    def drawBadge(self, painter, x, y, size, text, brush):
        painter.setFont(QtGui.QFont(painter.font().family(), 11, QtGui.QFont.Bold))
 
        while ((size - painter.fontMetrics().width(text)) < 10):
            pointSize = painter.font().pointSize() - 1
            weight = QtGui.QFont.Normal if (pointSize < 8) else QtGui.QFont.Bold
            painter.setFont(QtGui.QFont(painter.font().family(), painter.font().pointSize() - 1, weight))
 
        shadowColor = QtGui.QColor(0, 0, 0, size)
        self.fillEllipse(painter, x + 1, y, size, shadowColor)
        self.fillEllipse(painter, x - 1, y, size, shadowColor)
        self.fillEllipse(painter, x, y + 1, size, shadowColor)
        self.fillEllipse(painter, x, y - 1, size, shadowColor)
 
        painter.setPen(QtGui.QPen(QtCore.Qt.white, 2));
        self.fillEllipse(painter, x, y, size - 3, brush)
        painter.drawEllipse(x, y, size - 2, size - 2)
 
        painter.setPen(QtGui.QPen(QtCore.Qt.white, 1));
        painter.drawText(x, y, size - 2, size - 2, QtCore.Qt.AlignCenter, text);
 
        
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    win = QtGui.QMainWindow()
 
    toolbar = QtGui.QToolBar('Toolbar')
    win.addToolBar(QtCore.Qt.BottomToolBarArea, toolbar)
    b = QToolBadgeButton(win)
    b.setText("test")
    b.setCounter(22)
    toolbar.addWidget(b)
 
    w = QBadgeButton(parent=win)
    w.setText("test")
    w.setCounter(22)
    win.setCentralWidget(w)
    win.show()
 
    sys.exit(app.exec_())

#!/usr/bin/python
# -*- coding: utf-8 -*-
import hashlib
import os
import sys
import datetime
import tempfile

from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4 import QtWebKit
from PyQt4 import QtNetwork


PWD = os.path.dirname(os.path.realpath(__file__))

fn = os.path.basename(os.path.splitext(__file__)[0])
PATH_TEMP = os.path.join(tempfile.gettempdir(), fn)
if not os.path.exists(PATH_TEMP):
    os.makedirs(PATH_TEMP)


def to_uni(obj):
    if isinstance(obj, bytes):
        try:
            return obj.decode('utf-8')
        except UnicodeDecodeError:
            return obj.decode('gbk')
    elif isinstance(obj, (int, long)):
        return unicode(obj)
    elif isinstance(obj, (datetime.date, datetime.datetime)):
        return unicode(obj)
    else:
        return obj

def to_str(obj):
    if isinstance(obj, unicode):
        return obj.encode('utf-8')
    else:
        return obj


class App(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(App, self).__init__(parent)

        x, y, w, h = 500, 200, 1024, 768
        self.setGeometry(x, y, w, h)
        self.setFixedSize(w, h)

        self.url_lineedit = QtGui.QLineEdit(self)
        self.url_lineedit.setGeometry(0, 0, 900, 22)
        self.connect(self.url_lineedit, QtCore.SIGNAL('returnPressed()'), self.url_returnPressed)

        self.progressbar = QtGui.QProgressBar(self)
        self.progressbar.setGeometry(900, 0, 124, 22)
        self.progressbar.setMinimum(0)
        self.progressbar.setMaximum(100)

        self.webview = QtWebKit.QWebView(self)
        qsettings = self.webview.settings()
        qsettings.setAttribute(QtWebKit.QWebSettings.DeveloperExtrasEnabled, True)

        self.inspector = QtWebKit.QWebInspector(self)
        self.inspector.setPage(self.webview.page())
        self.inspector.setGeometry(0, h - 200, w, 200)
        self.inspector.setVisible(True)

        self.webview.setGeometry(0, 22, w, h - 200)
        self.connect(self.webview, QtCore.SIGNAL("loadStarted()"), self.webview_loadStarted)
        self.connect(self.webview, QtCore.SIGNAL("loadFinished(bool)"), self.webview_loadFinished)
        self.connect(self.webview, QtCore.SIGNAL('loadProgress(int)'), self.webview_loadProgress)

        cache =  QtNetwork.QNetworkDiskCache()
        dir = QtGui.QDesktopServices.storageLocation(QtGui.QDesktopServices.CacheLocation)
        cache.setCacheDirectory(dir)
        self.am = self.webview.page().networkAccessManager()
        self.am.setCache(cache)

        self.cj = QtNetwork.QNetworkCookieJar()
        self.am.setCookieJar(self.cj)

        self._portal_url = "http://www.baidu.com/"
        self.url_lineedit.setText(self._portal_url)
        self.webview.load(QtCore.QUrl(self._portal_url))

        self.url_lineedit.setFocus()
        self.setup_global_shortcuts()

    @property
    def url(self):
        s = str(self.url_lineedit.text()).strip()
        if not s.startswith('http'):
            return 'http://' + s
        return s

    @property
    def entry_body(self):
        frame = self.webview.page().mainFrame()
        return to_uni(str(frame.toHtml().toUtf8()))

    def setup_global_shortcuts(self):
        show_debug_option_kseq = "Ctrl+L"
        key_seq = QtGui.QKeySequence(show_debug_option_kseq)

        act = QtGui.QAction(self)
        act.setShortcut(key_seq)

        self.addAction(act)
        act.triggered.connect(self._url_lineedit_get_focus)

    def _url_lineedit_get_focus(self):
        self.url_lineedit.setFocus()
        self.url_lineedit.setSelection(0, len(self.url))

    def show_and_raise(self):
        self.show()
        self.raise_()

    def url_returnPressed(self):
        self.webview.load(QtCore.QUrl(self.url))

    def webview_loadProgress(self, progress):
        self.progressbar.setValue(progress)

    def webview_loadStarted(self):
        print 'webview_loadStarted'
        self.progressbar.setValue(0)

    def webview_loadFinished(self, result):
        print 'webview_loadFinished', result
        if result:
            save_to = os.path.join(PATH_TEMP, hashlib.sha1(self.url).hexdigest())
            with open(save_to, 'w') as f:
                print 'entry body write into %s' % save_to
                f.write(to_str(self.entry_body))

            # wget http://code.jquery.com/jquery-2.1.1.min.js
            path_jq = os.path.join(PWD, 'jquery-2.1.1.min.js')
            js_code = file(path_jq).read()
            mainFrame = self.webview.page().mainFrame()

            print mainFrame
            for frame in mainFrame.childFrames():
                print frame

            js_code = """$(document).ready(function(){
$('head').after('<b>hello jquery!</b>');
            });
            """
            mainFrame.evaluateJavaScript(js_code)



if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    demo = App()
    demo.show_and_raise()
    sys.exit(app.exec_())
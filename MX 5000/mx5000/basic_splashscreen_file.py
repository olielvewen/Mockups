#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# splashcreen - A splashscreen for mes projets initialement pour openshotqt
# Copyright (c) 2019 Olivier Girard <olivier@openshot.org>
#
# MX 5000 is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# MX 5000 is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import os

from PyQt5.QtWidgets import QApplication, QSplashScreen
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QObject, QTimer,Qt

# class SplashScreen(QObject):
#
#     def __init__(self, parent=None):
#
#         super(SplashScreen, self).__init__(parent)
#
#     # def show(self):
#
#         app = QApplication([])
#         app.setQuitOnLastWindowClosed(False)
#
#         self.timer = QTimer()
#         self.timer.setInterval(5000)
#         self.timer.setSingleShot(True)
#         self.timer.start()
#
#         splashscreen_path = os.path.join(os.path.dirname(__file__), "images/splash.png")
#
#         self.splashscreen = QSplashScreen()
#         self.splashscreen.setPixmap(QPixmap(splashscreen_path))
#         self.updateSplash()
#         self.splashscreen.show()

    # self.showSplash()

        # return app.exec_()

    # if self.timer.isActive():
    #     self.timer.timeout(int).connect(self.loadQuickstart)
    # else:
    #     application.exec_()

    # def showSplash(self):
    #     self.splashscreen = QSplashScreen()
    #     self.splashscreen.setPixmap(QPixmap(splash.png))
    #     self.splashscreen.show()


# def updateSplash(self):
#     self.splashscreen.showMessage(self.tr("Starting + app_name + app_version"),
#                                   Qt.AlignRight | Qt.AlignBotton | Qt.White)
#     self.splashscreen.showMessage(self.tr("Loading Libopenshot-audio"), Qt.AlignRight | Qt.AlignBotton | Qt.White)
#     self.splashscreen.showMessage(self.tr("Loading Libopenshot"), Qt.AlignRight | Qt.AlignBotton | Qt.White)
#     self.splashscreen.showMessage(self.tr("Loading Kviso"), Qt.AlignRight | Qt.AlignBotton | Qt.White)

    # def loadQuickstart(self):
    #
    #     self.windo = KvIso()
    #     self.windo.show()
    #     self.splashscreen.finish(self.windo)
    #     return application.exec_()

app_name = "mx5000"
app_version = "0.15"

if __name__ == "__main__":

    app = QApplication([])

    splashscreen_path = os.path.join(os.path.dirname(__file__), "images/splash.png")
    splashscreen = QSplashScreen()
    splashscreen.setPixmap(QPixmap(splashscreen_path))
    timer = QTimer()
    timer.setInterval(5000)
    # timer.setSingleShot(True)
    timer.start()
    splashscreen.show()
    if timer.isActive():
        splashscreen.showMessage(("Starting + app_name + app_version"), Qt.AlignRight | Qt.AlignBottom, Qt.white)
        splashscreen.showMessage(("Loading Libopenshot-audio"), Qt.AlignRight | Qt.AlignBottom, Qt.white)
        splashscreen.showMessage(("Loading Libopenshot"), Qt.AlignRight | Qt.AlignBottom, Qt.white)
        splashscreen.showMessage(("Loading Kviso"), Qt.AlignRight | Qt.AlignBottom, Qt.white)
    app.processEvents()
    app.exec_()

    # self.updateSplash()
    # splashscreen.finish()
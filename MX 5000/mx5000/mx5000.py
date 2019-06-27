#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# MX 5000 - A Tool for MX 5000 Keyboard using MX5000tools
# Copyright (c) 2017 Olivier Girard <olivier@openshot.org>
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
import sys
import configparser
from functools import partial

from PyQt5.QtCore import QSettings, QRect, QTimer
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox
from PyQt5.QtGui import *

from ui.mx5000ui import Ui_MX5000
from images import mx5000ressources_rc
from credits import Credits


app_name = "MX 5000"
app_version = "0.15"
app_author = "Olivier Girard"
app_email = "olivier@openshot.org"

# check if we are on a Linux system either exit
if os.name != "posix":
    print("You are not under a Linux system")
    sys.exit(2)

# check if the hidden project folder is created by default, if not it is created
HOME_PATH = os.path.expanduser("~")
USER_PATH = os.path.join(HOME_PATH, ".mx5000")
if not os.path.exists(USER_PATH):
    os.mkdir(USER_PATH)
# configFolder = os.path.join(QDir.homePath(), ".mx5000")
# configFile = os.path.join(QDir.homePath(), ".mx5000/config.conf")
# configLog = os.path.join(QDir.homePath(), ".mx5000/logfile")

config_path = os.path.join(USER_PATH, "config.ini")
# settings = QSettings()
# config = configparser.ConfigParser()
# config['DEFAULT'] = {'path_keyboard': "/dev/hiddev0",
#                      'keyboard_name': "Whatever",
#                      'server_type': "self.ui.rdbimap.setChecked(True)",
#                      'server_adress': "self.ui.lneserveradress.setText(imap.yourserver.com)",
#                      'username': 'username',
#                      'password': "cnffjbep",
#                      'time_to_check': '10',
#                      'keyboard_beep': '1',
#                      'play_sound': '1',
#                      'sound_directory': "/home/user/.mx5000/notify.ogg"}
# if not os.path.isfile("config"):
# os.mkdir(USER_PATH)
# with open('config.ini', 'w') as configfile:
#     config.write(configfile)


class Mx5000(QDialog):
    def __init__(self, parent=None):
        super(Mx5000, self).__init__(parent)

        self.setupUi()
        self.connectActions()
        self.dirty = True

    # ===================================================================================================================
    def setupUi(self):

        self.ui = Ui_MX5000()
        self.ui.setupUi(self)
        self.ui.rdbimap.setChecked(True)
        self.ui.chkmakebeep.setChecked(True)
        self.ui.chkplaysound.setChecked(True)

        # with open('licence.txt', 'r') as my_license:
        #     text = my_license.read()
        #     self.ui.textBrowser.setPlainText(text)

    # ===================================================================================================================
    def connectActions(self):

        self.ui.btnchecknowmails.clicked.connect(self.checkNowMails)
        self.ui.btnclearlog.clicked.connect(self.logMessages)
        self.ui.btnresetkeyboard.clicked.connect(self.resetKeyboard)
        # self.ui.btnapply.clicked.connect(self.applySettings)
        self.ui.chkmakebeep.toggled.connect(self.updatecheckboxes)

    # ===================================================================================================================

    def closeEvent(self, event):

        if self.okToContinue():
            self.writeSettings()
            event.accept()
        else:
            event.ignore()

    # ===================================================================================================================

    def loadSettings(self):

        settings = QSettings("Exemple app", "MX5000")
        geometry = settings.value("geometry", QRect(200, 200, 615, 800))
        self.setGeometry(geometry)

    def showEvent(self, event):
    	self.loadSettings()
    	super(Mx5000, self).showEvent(event)

    # ===================================================================================================================

    def writeSettings(self):
        settings = QSettings("Exemple app", "MX5000")
        settings.setValue("geometry", self.geometry())

    # ===================================================================================================================

    def okToContinue(self):

        if self.dirty:
            reply = QMessageBox.question(
                self,
                self.tr("MX 5000"),
                self.tr("Did you want to close the application ?"),
                QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel,
            )
            return reply == QMessageBox.Yes
        return True

    # ===================================================================================================================

    # ===================================================================================================================

    # #===================================================================================================================
    def applySettings(self):

        # self.writeSettings()
        pass

    # ===================================================================================================================
    def checkNowMails(self):

        # pass
        dialog = Credits(self)
        if dialog.exec_():
            self.show()
            # self.Credits.showAuthors()
            # self.Credits.showLicense()
            # self.Credits.showDocumenters()
            # self.Credits.showTranslators()

    # ===================================================================================================================
    def logMessages(self):

        # pass
        with open("licence.txt", "r") as my_licence:
            text = my_licence.read()
            # The Python way
            # self.ui.textBrowser.append(text)
            # The Qt way
            self.ui.textBrowser.setPlainText(text)

    # ===================================================================================================================
    def resetKeyboard(self):

        pass

    # ===================================================================================================================
    def updatecheckboxes(self):

        pass

    # ===================================================================================================================


if __name__ == "__main__":
    application = QApplication(sys.argv)
    # nor use the name of class as name of variable
    w = Mx5000()
    w.show()
    sys.exit(application.exec_())

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @file
 @brief This file contains the Q dialog (i.e A tool for )
 @author Olivier Girard <olivier@openshot.org>

 @section LICENSE

 Copyright (c) 2015 Q Team. This file is part of
 QDvGrab (http://www.qdvgrab.org), an open-source project
 dedicated to delivering high quality video editing and animation solutions
 to the world.

 QDvGrab is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.

 QDvGrab is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.

 You should have received a copy of the GNU General Public License
 along with QDVgrab.  If not, see <http://www.gnu.org/licenses/>.
 """

# Used for system
import sys
#Used for functions
import os
#Need for path
import os.path
#Need for find library
import shutil
#Need for create command line
import subprocess
import time
#Used to run the web browser by default
import webbrowser
#need for display gui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
#Used for call ui files
from kvisoui import Ui_kvisodialog
# import SplashScreen

# class SplashScreen(QSplashScreen):

    # def __init__(self, parent=None):

        # super(SplashScreen, self).__init__(parent)

    # def showSplash(self):

        # self.timer = QTimer()
        # self.timer.setInterval(6000)
        # self.timer.setSingleShot(True)
        # self.timer.start(KvIso)

        # self.splashscreen = QSplashScreen()
        # self.splashscreen.setPixmap(QPixmap(splash.png))
        # self.splashscreen.show()

        # self.splashscreen.showMessage(self.tr("Starting + app_name + app_version"), QtCore.Qt.AlignRight | QtCore.Qt.AlignBotton | QtCore.Qt.White)
        # self.splashscreen.showMessage(self.tr("Loading Libopenshot-audio"), QtCore.Qt.AlignRight | QtCore.Qt.AlignBotton | QtCore.Qt.White)
        # self.splashscreen.showMessage(self.tr("Loading Libopenshot"), QtCore.Qt.AlignRight | QtCore.Qt.AlignBotton | QtCore.Qt.White)
        # self.splashscreen.showMessage(self.tr("Loading Kviso"), QtCore.Qt.AlignRight | QtCore.Qt.AlignBotton | QtCore.Qt.White)

        # if self.timer.isActive():
        #     self.timer.timeout.connect(self.loadQuickstart)
        # else:
        #     self.loadQuickstart()
        #     return

    # def loadQuickstart(self):

        # self.splashscreen.finish(KvIso)
        # KvIso = KvIso()
        # KvIso.show()
        # application.exec_()


class KvIso(QDialog):

    def __init__(self, parent=None):
        super(KvIso, self).__init__(parent)
        # self.SplashScreen.loadQuickstart()
        self.createWidgets()
        self.setupUi()
        self.connectActions()

        self.readStdErr = ""
        self.readStdOut = ""

        self.count = 0

    # ===================================================================================================================
    def createWidgets(self):

        self.ui = Ui_kvisodialog()
        self.ui.setupUi(self)
        # self.ui.updateUi()

    # ===================================================================================================================
    def setupUi(self):

        self.ui.chkvideofile.setEnabled(False)
        self.ui.chkimageiso.setEnabled(False)
        self.ui.lnenamedvd.setEnabled(False)
        self.ui.btncancel.setEnabled(False)
        self.ui.textEdit.setReadOnly(True)
        # self.ui.textEdit.setLineWrapMode(QTextEdit.NoWrap)
        # self.ui.textEdit.toPlaintText()

    # def updateUi(self):
    #     pass

    # ===================================================================================================================
    def connectActions(self):

        self.ui.btnquit.clicked.connect(self.close)
        self.ui.btnhelp.clicked.connect(self.help)
        self.ui.btnchoosevideofile.clicked.connect(self.choosevideofile)
        self.ui.chkvideofile.toggled.connect(self.ui.chkimageiso.setEnabled)
        self.ui.chkimageiso.toggled.connect(self.ui.lnenamedvd.setEnabled)
        self.ui.btnexport.clicked.connect(self.export)
        self.ui.btncancel.clicked.connect(self.cancel)
        # self.UpdateProgressBar(0)

    # ===================================================================================================================
    def help(self, event):

        try:
            webbrowser.open("https://launchpad.net/DvdCreator")
            self.ui.textEdit.append("Website Project is open")
        except:
            QMessageBox.information(self, "Error!", "Unable to open the website")
            self.ui.textEdit.append("Unable to open the website")

    # ===================================================================================================================
    def choosevideofile(self):

        self.filepath = ""
        # self.file_extension = ("MPEG Files (*.mpeg *.mpg *.vob *.dvd)")
        self.filedialog = QFileDialog()
        self.filepath = self.filedialog.getOpenFileName(self, self.tr('Kviso'), ('Choose a MPEG file'))
        if self.filepath:
            # self.btnchoosevideofile.setText(str(filepath))
            self.p1 = str(self.filepath).split('/')
            self.p1.pop()
            self.path = '/'.join(self.p1) + '/'
            self.ui.chkvideofile.setEnabled(True)

    # ===================================================================================================================
    def export(self):

        if self.ui.chkvideofile.isChecked():

            self.ui.textEdit.append("**** dvdauthor : PROCESSUS 1 ****")

            self.processus = QProcess()
            # command = ["-o +(self.path + 'dvd')+ str(self.filepath)"]
            command = ["-p"]

            self.processus.readyReadStandardError.connect(self.readStdErr)
            self.processus.readyReadStandardOutput.connect(self.readStdOut)
            self.processus.setProcessChanelMode() #unification des deux sorties standard et error

            self.filelogpath = self.path + "dvd.log"
            self.filelog = open('self.filelogpath', 'w')

            self.processus.start("tcmodinfo", command)
            # self.processus.finished.connect(self.dvdauthor2)

            self.ui.btncancel.setEnabled(True) #activation button cancel
        else:
            self.ui.textEdit.append("Please choose one file and one action...")

    # ===================================================================================================================
    def cancel(self):

        self.processus.kill() #kill processus
        self.workfinished() #the work is stopped

    # ===================================================================================================================
    def workfinished(self):

        self.ui.textEdit.clear() #remove all text
        self.ui.progressbarexport.reset() #reset to zero the progress bar
        self.ui.btncancel.setEnabled(False) # update the gui for being ready for another conversion
        self.ui.btnexport.setEnabled(True)
        self.ui.chkvideofile.setEnabled(False)
        self.ui.chkimageiso.setEnabled(False)

    # ===================================================================================================================
    def readStdErr(self, linerr=""):
        self.linerr = self.processus.readLineStderr()
        self.ui.textEdit.append(self.linerr)
        self.filelog.write(self.linerr)

    # ===================================================================================================================
    def readStdOut(self, lineout=""):

        self.ui.textEdit.setReadOnly(True)
        self.lineout = self.processus.readLineStdout()
        self.ui.textEdit.append(self.lineout)
        self.filelog.write(self.lineout)

    # ===================================================================================================================
    def dvdauthor2(self):

        self.ui.textEdit.append("**** dvdauthor : PROCESSUS 2 ****")

        # command = ["dvdauthor", "-T", "-o", "(self.path + 'dvd')"]
        command = ["-i +self.path"]
        self.processus = QProcess()

        self.processus.readyReadStandardError.connect(self.readStdErr)
        self.processus.readyReadStandardOutput.connect(self.readStdOut)
        self.processus.setProcessChanelMode() #unification des deux sorties standard et error

        self.processus.start("tcprobe", command)

        if self.ui.chkimageiso.isChecked():
            self.processus.finished.connect(self.dvdiso)
        else:
            self.processus.finished.connect(self.workfinished)

    # ===================================================================================================================
    def dvdiso(self):

        self.ui.textEdit.append("**** mkisofs : PROCESSING ****")

        # command = ["mkisofs", "-o", "(self.path + str(self.ui.lnenamedvd() + '.iso')", "-V", "self.lnenamedvd.text()", "-dvd-video", "(self.path + 'dvd')"]
        command = ["-p"]
        self.processus = QProcess()

        self.processus.readyReadStandardError.connect(self.readStdErr)
        self.processus.readyReadStandardOutput.connect(self.readStdOut)
        self.processus.setProcessChanelMode() #unification des deux sorties standard et error

        self.processus.start("tcmodinfo", command)
        self.processus.finished.connect(self.workfinished)

    # ===================================================================================================================
    def UpdateProgressBar(self):
        while self.processus.Running():
            for i in range(0, 100):
                self.ui.progressbarexport.setProgress(i)
            self.ui.progressbarexport.reset()

        # if self.count == 100:
        #     self.count = 0
        # self.count = self.count + 1
        # self.ui.progressbarexport.setProgress(self.count)



if __name__ == "__main__":
    application = QApplication(sys.argv)
    splashscreen = QSplashScreen()
    splashscreen.setPixmap(QPixmap("splash.png"))
    splashscreen.show()
    # time.sleep(6)
    application.processEvents()
    KvIso = KvIso()
    KvIso.show()
    splashscreen.finish(KvIso)
    application.exec_()

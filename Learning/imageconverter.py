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

import sys
import os
# Need for path
import os.path
#Need for find library
import shutil
#Need for create command line
import subprocess

#need for display gui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

#Load ui files
from imageconverterui import Ui_Dialog

app_name = "Image Converter"
app_version = "0.0.1"
app_author = "Olivier Girard"
author_mail = "olivier@openshot.org"

class ImageConverter(QDialog):

    def __init__(self, parent=None):
        super(ImageConverter, self).__init__(parent)
        self.setupUi()
        self.connectActions()

        format_image = ['bmp', 'eps', 'gif', 'jpeg', 'png', 'tiff']
        for format in format_image:
            self.ui.cmbtargetformat.addItem(format.upper())
            self.ui.cmbtargetformat.setCurrentIndex(4)

    #===========================================================================
    def setupUi(self):
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.btnconvert.setEnabled(False)

    #===========================================================================
    def connectActions(self):

        self.ui.btninputfile.clicked.connect(self.addInputFile)
        self.ui.btnconvert.clicked.connect(self.conVertFile)
        #self.ui.cmbtargetformat.currentIndexChanged.connect(self.targetFormat)
        #self.ui.chkenhance.toggled.connect(self.enHance)
        #self.ui.chkmonochrome.toggled.connect(self.monoChrome)

    #==========================================================================
    def addInputFile(self):
        # initialName = str(self.ui.lnesourcefile.text())
        initialPath = QDir.homePath()
        fileNamePath = QFileDialog.getOpenFileName(self, self.tr("Choose a File"), initialPath)
        if fileNamePath is not None:
            # (dirname, fileName) = os.path.split(fileNamePath)
            self.ui.lnesourcefile.setText(str(fileNamePath)) #on affiche le nom et le chemin du fichier
            self.ui.btnconvert.setEnabled(True) #on active le btn convert

        # if not initialName is not None:
            #self.ui.statusBar().showMessage(msg, 5000) #on affiche le message pendant 5 sec dans la statusbar

    #==========================================================================
    def conVertFile(self):

        self.process = QProcess(self)
        sourceFile = str(self.ui.lnesourcefile.text())
        targetFile = QFileInfo(sourceFile.path() + QDir.separator() + QFileInfo(
            sourceFile.baseName() + "." + self.ui.cmbtargetformat.currentText().toLower)) #copie du nom du fichier source + changement de son extension sleon celle choisie dans la cmbox
        self.ui.btnconvert.setEnabled(False) #desactivation du btn convert
        self.process.readyReadStandardError.connect(self.updateOutputTextEdit)
        self.process.error.connect(self.processError)
        self.process.finished.connect(self.processFinish)
        self.ui.outputtextedit.clear() #nettoyage des anciens messages

        args = [] #ajout des parametres selon les choix fait dans l'interface
        if self.ui.chkenhance.isChecked():
            args += "-enhance"
        if self.ui.chkmonochrome.isChecked():
            args += "-mononchrome"
        args += sourceFile + targetFile
        self.process.start("convert", args)

    #==========================================================================
    def processFinished(self, exitCode="", exitStatus=""):
        if exitStatus == "CrashExit":
            self.ui.outputtextedit.append(self.tr("Conversion program crashed"))
        elif exitStatus != 0:
            self.ui.outputtextedit.append(self.tr("Conversion failed"))
        else:
            self.ui.outputtextedit.append(self.tr("file {} created").format(targetFile))
        self.ui.btnconvert.setEnabled(True)

    #==========================================================================
    def updateOutputTextEdit(self):
        newdata = self.process.readAllStandardError()
        text = str(self.ui.outputtextedit.toPlainText() + str(newdata))
        self.ui.outputtextedit.setPlainText(text)

    #==========================================================================
    def processError(self, error=None):
        if error == QProcess.FailedToStart():
            self.ui.outputtextedit.append(self.tr("Conversion programm not found"))
            self.ui.btnconvert.setEnabled(True)
            #si le processus ne peut etre lance, qProcess emet error au lieu de
            #finished + rapporte toutes les erreurs et active le btn convert
            #conversion asynchrome executer le programme convert et rend immédiatement le controle de l'interface
            #conversion synchrome necessite que le programme soit fini avant de poursuivre

    #==========================================================================

if __name__ == "__main__":
    application = QApplication(sys.argv)
    ImageConverter = ImageConverter()
    ImageConverter.show()
    print((("Welcome to {} {}. \nHope you'll enjoy it. \nPlease report all bugs,"
          "features request and comments at {}\n").format(app_name, app_version, author_mail)))
    sys.exit(application.exec_())

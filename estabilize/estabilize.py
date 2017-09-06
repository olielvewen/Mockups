#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# eStabilize - A Tool for Transcode Stabilize plugin done by Georg Martius
# Copyright (c) 2016 Olivier Girard <olivier@openshot.org>
#
# eStabilize is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# eStabilize is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

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
from estabilizeui import Ui_Dialog

app_name = "eStabilize"
app_version = "0.10"
app_author = "Olivier Girard"
author_mail = "olivier@openshot.org"

class MonAppli(QDialog):

    def __init__(self, parent=None):
        super(MonAppli, self).__init__(parent)
        self.createWidgets()
        self.setupUi()
        self.connectActions()

    #===========================================================================
    def setupUi(self):
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)


    #===========================================================================
    def createWidgets(self):
        """


        """

        pass

    #===========================================================================
    def connectActions(self):
        " "
        pass


if __name__ == "__main__":
    application = QApplication(sys.argv)
    MonAppli = MonAppli()
    MonAppli.show()
    print("Welcome to eStabilize {}. \nHope you'll enjoy it. \nPlease report all bugs,"
          "features request and comments at {}\n".format(app_version, author_mail))
    sys.exit(application.exec_())

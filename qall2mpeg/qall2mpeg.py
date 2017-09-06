#!/usr/bin/env python
# -*- coding: utf8 -*-
#
# MX 5000 - A Tool for MX 5000 Keyboard
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
import os.path

#Need for display gui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

#Load ui files
from qall2mpegui import Ui_Dialog

app_name = "QAll2MPEG"
app_version = "0.01"
app_author = "Olivier Girard"
app_email = "olivier@openshot.org"

class Qall2Mpeg(QDialog):

    def __init__(self, parent=None):
        super(Qall2Mpeg, self).__init__(parent)

        self.setupUi()
        self.connectActions()

    def setupUi(self):

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

    def connectActions(self):

        pass

if __name__ == "__main__":
    application = QApplication(sys.argv)
    Qall2Mpeg = Qall2Mpeg()
    Qall2Mpeg.show()
    sys.exit(application.exec_())
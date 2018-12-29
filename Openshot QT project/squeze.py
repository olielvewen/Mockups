#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Squeze - A tool for the  project
#Copyright (c) 2019 Olivier Girard <olivier@openshot.org>
#
# Squeze is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# Squeze is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import sys
import os

from PyQt5.QtWidgets import QApplication, QDialog

from squezeui import Ui_Dialog
import squeze_rc

class Squeze(QDialog):

    def __init__(self, parent=None):
        super(Squeze, self).__init__(parent)
        self.setupUi()
        self.connectActions()

        self.ui.btncrop.clicked.connect(self.load_crop)
        self.ui.btnsqueze.clicked.connect(self.load_squeze)
        self.ui.btnletterbox.clicked.connect(self.load_letterbox)
        self.ui.btnnone.clicked.connect(self.close_dialog)

    #===================================================================================================================
    def setupUi(self):

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

    #===================================================================================================================
    def connectActions(self):
        pass

    def load_crop(self):
        pass

    def load_squeze(self):
        pass

    def load_letterbox(self):
        pass

    def close_dialog(self):
        QDialog.rejected()



if __name__ == "__main__":
    application = QApplication(sys.argv)
    squeze = Squeze()
    squeze.show()
    sys.exit(application.exec_())
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#Export Video - A tool for the Openshot Qt project
#Copyright (c) 2015 Olivier Girard <olivier@openshot.org>
#
#Export Video is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
#Export Video is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import sys
import os

from PyQt5.QtWidgets import *

from exportvideoui import Ui_Dialog

class ExportVideo(QDialog):

    def __init__(self, parent=None):
        super(ExportVideo, self).__init__(parent)
        self.setupUi()
        self.connectActions()

    #===================================================================================================================
    def setupUi(self):

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

    #===================================================================================================================
    def connectActions(self):
        pass



if __name__ == "__main__":
    application = QApplication(sys.argv)
    export = ExportVideo()
    export.show()
    sys.exit(application.exec_())
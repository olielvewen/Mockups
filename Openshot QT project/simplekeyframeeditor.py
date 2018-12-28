#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#simle keyframe editor - A tool for the Openshot Qt project
#Copyright (c) 2015 Olivier Girard <olivier@openshot.org>
#
#simple keyframe editor is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
#simple keyframe editor is distributed in the hope that it will be useful,
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

from simplekeyframeeditorui import Ui_DockWidget

class SimpleKeyframeEditor(QDockWidget):

    def __init__(self, parent=None):
        super(SimpleKeyframeEditor, self).__init__(parent)
        self.setupUi()
        self.connectActions()

    #===================================================================================================================
    def setupUi(self):

        self.ui = Ui_DockWidget()
        self.ui.setupUi(self)

    #===================================================================================================================
    def connectActions(self):
        pass



if __name__ == "__main__":
    application = QApplication(sys.argv)
    keyframe = SimpleKeyframeEditor()
    keyframe.show()
    sys.exit(application.exec_())
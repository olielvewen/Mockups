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

import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from mx5000ui import Ui_MX5000
import mx5000ressources_rc


app_name = "MX 5000"
app_version = "0.01"
app_author = "Olivier Girard"
app_email = "olivier@openshot.org"


class Mx5000(QDialog):
    def __init__(self, parent=None):
        super(Mx5000, self).__init__(parent)

        self.setupUi()
        self.connectActions()
        self.dirty = False




if __name__ == "__main__":
    application = QApplication(sys.argv)
    Mx5000 = Mx5000()
    Mx5000.show()
    sys.exit(application.exec_())
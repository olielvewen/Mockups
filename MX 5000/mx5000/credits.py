#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Credit - a file for displaying credits -Authors -Translator-Documenter-Licence
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

from PyQt5.QtWidgets import QDialog

from ui.creditsui import Ui_creditscreen

OG = {'name': 'Olivier Girard', 'email': 'olivier@openshot.org'}
CREDITS = {'code': [OG],
           'documentation': [OG],
           'translation': [OG],
           }
path_licence = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Credits(QDialog):

    def __init__(self, parent=None):

        super(Credits, self).__init__(parent)
        self.setupUi()
        self.showLicense()
        # self.showAuthors()

    def setupUi(self):

        self.ui = Ui_creditscreen()
        self.ui.setupUi(self)

    def showLicense(self):

        # path_li = os.path.join(path_licence, "licence.txt")

        with open('licence.txt', 'r') as my_licence:
            text = my_licence.read()
            self.ui.textBrowserlicense.setPlainText(text)
            # self.ui.textBrowserlicense.setText(text)

    def showAuthors(self):

        authors = []
        for person in CREDITS['code']:
            name = person['name']
            email = person['email']
            authors.append("{} <{}>".format(name, email))
        self.ui.textBrowserwritten.setText(authors)

    def showDocumenters(self):

        authors = []
        for person in CREDITS['documentation']:
            name = person['name']
            email = person['email']
            authors.append("{} <{}>".format(name, email))
        self.ui.textBrowserdocumented.setText(authors)

    def showTranslators(self):

        authors = []
        for person in CREDITS['translation']:
            name = person['name']
            email = person['email']
            authors.append("{} <{}>".format(name, email))
        self.ui.textBrowsertranslated(authors)

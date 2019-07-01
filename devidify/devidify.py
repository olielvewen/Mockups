#!/usr/bin/env python
# -*- coding: utf8 -*-
#
# Devidify - A Tool for Ripping DVD Audio Tracks
# Copyright (c) 2019 Olivier Girard <olivier@openshot.org>
#
# Devidify is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# Devidify is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QDialog


from devidifyui import Ui_MX5000
import mx5000ressources_rc


app_name = "Devidify"
app_version = "1.18"
app_author = "Olivier Girard"
app_email = "olivier@openshot.org"


class deViDify(QDialog):
    def __init__(self, parent=None):
        super(deViDify, self).__init__(parent)

        self.setupUi()
        self.connectActions()
        self.dirty = False

    # ==================================================================================================================
    def setupUi(self):

        pass

    # ==================================================================================================================
    def connectActions(self):

        pass

    # ==================================================================================================================
    def doScan(self):
        "Scan le dvd, parcours la liste et l'affiche dans un treeview"
        pass

    # ==================================================================================================================
    def populate(self):
        "vide la list si pas deja fait puis la remplie"
        pass

    # ==================================================================================================================
    def treeClick(self):

        pass

    # ==================================================================================================================
    def playVideo(self):

        pass

    # ==================================================================================================================
    def doRip(self):
        "prepare le travail de rippage"
        pass

    # ==================================================================================================================
    def make_wavs(self):
        "utilisation mplayer pour ripper les fichiers en wav"
        pass

    # ==================================================================================================================
    def make_mp3s(self):
        "utilisation lame pour les mp3"
        pass

    # ==================================================================================================================
    def make_oggs(self):
        "utilisation oggenc pour les ogg"
        pass

    # ==================================================================================================================
    def padDigit(self, digit):
        "ajout un zero au 2 chiffres déjà present"
        pass

    # ==================================================================================================================
    def toggleCheck(self, cell, path):
        "toggle a check box"
        pass

    # ==================================================================================================================
    def selectAll(self):
        "check all tracklist toggled"
        pass

    # ==================================================================================================================
    def unselectAll(self):
        "uncheck all tracklist toggled"
        pass

    # ==================================================================================================================
    def doAbout(self):
        "affiche la fenetre About"
        pass

    # ==================================================================================================================
    def onExit(self):
        "nettoye le prog et quitte le programme"
        pass

    # ==================================================================================================================


class RipDialog(object):

    def shellQueue(self):
        "process shell commmands one after another and ferme la fenetre"
        pass

    # ==================================================================================================================
    def onCancel(self):
        "abandonne la tache en cours des la fermeture de la fenetre"
        pass

    # ==================================================================================================================
    def onDeleteEvent(self):
        "empeche la fermeture ripDialog"
        pass

    # ==================================================================================================================


class ErrorDialog(object):

    pass

    # ==================================================================================================================


class PrefsDialog(object):

    def modeChange(self):
        "callback for modecombo"
        pass

    # ==================================================================================================================
    def dirChange(self):
        "selection du repertoire"
        pass

    # ==================================================================================================================
    def debug(self, msg):
        pass

    # ==================================================================================================================
    def error(self, err):
        pass

    def get_glade(self):
        pass

    def check_all_deps(self):
        pass

    def check_dep(self):
        pass
    def url_hooks(self):
        pass

    # ==================================================================================================================


if __name__ == "__main__":

    application = QApplication(sys.argv)
    window = deViDify()
    window.show()
    sys.exit(application.exec_())

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# tray_menu - A tray menu for MX 5000 Keyboard using MX5000tools
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

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction

app = QApplication([])
app.setQuitOnLastWindowClosed(False)

#Création de l'icone qui se situe dans le dossier image
icon_path_tray = os.path.join(os.path.dirname(__file__), "images/mascot.png")
tray_icon = QIcon(icon_path_tray)

#Création du tray
tray_menu = QSystemTrayIcon()
tray_menu.setIcon(tray_icon)
tray_menu.setVisible(True)

#Création du menu
menulist_tray = QMenu()

#Display another icon
icon_path = os.path.join(os.path.dirname(__file__), "images/")

#Show the main window
actionshow = QAction(QIcon(os.path.join(icon_path, "desktop.png")), "Show Main Window")
menulist_tray.addAction(actionshow)

#Hide the main window
actionHide = QAction(QIcon(os.path.join(icon_path, "mouse.png")), "Hide the Window")
menulist_tray.addAction(actionHide)

#add a separtor
menulist_tray.addSeparator()

#add a help item
actionHelp = QAction(QIcon(os.path.join(icon_path, "reboot.png")), "Help")
menulist_tray.addAction(actionHelp)

#Quit the application
actionQuit = QAction(QIcon(os.path.join(icon_path, "application-exit.png")), "Quit")
menulist_tray.addAction(actionQuit)

#add a separator
menulist_tray.addSeparator()

#Ajout du menu au tray
tray_menu.setContextMenu(menulist_tray)

app.exec_()
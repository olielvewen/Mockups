#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from random import randint

from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QListWidget, QStackedWidget, QListWidgetItem, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QSize


class EssaieStackedWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super(EssaieStackedWidget, self).__init__(*args, **kwargs)
        self.resize(800, 600)

        layout = QHBoxLayout(self, spacing=0)
        layout.setContentsMargins(0, 0, 0, 0)

        # creation d'une liste à gauche de la IA
        self.listWidget = QListWidget(self)
        layout.addWidget(self.listWidget)

        # creation ajout du stackedwidget à IA
        self.stackedWidget = QStackedWidget()
        layout.addWidget(self.stackedWidget)
        self.initUI()

    def initUI(self):
        # modification
        self.listWidget.currentRowChanged.connect(self.stackedWidget.setCurrentIndex)
        self.listWidget.setFrameShape(QListWidget.NoFrame)
        self.listWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        for i in range(9):
            item = QListWidgetItem(QIcon('Data/0%d.ico' % randint(1, 8)), str('blabla %s' % i), self.listWidget)
            item.setSizeHint(QSize(16777215, 60))
            item.setTextAlignment(Qt.AlignCenter)

        for i in range(9):
            label = QLabel('number %d' % i, self)
            label.setAlignment(Qt.AlignCenter)
            label.setStyleSheet('background: rgb(%d, %d, %d); margin: 50px;' % (randint(0, 255), randint(0, 255), randint(0, 255)))
            self.stackedWidget.addWidget(label)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EssaieStackedWidget()
    window.show()
    sys.exit(app.exec_())

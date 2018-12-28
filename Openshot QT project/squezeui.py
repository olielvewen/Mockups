# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'squeze.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(452, 350)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../xdg/openshot.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(10, 10, 431, 321))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(60, 0, 91, 16))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(260, 0, 91, 16))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(60, 160, 91, 16))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(270, 160, 91, 16))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.btncrop = QtWidgets.QPushButton(self.widget)
        self.btncrop.setGeometry(QtCore.QRect(30, 30, 160, 120))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../images/crop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btncrop.setIcon(icon1)
        self.btncrop.setIconSize(QtCore.QSize(140, 120))
        self.btncrop.setObjectName("btncrop")
        self.btnnone = QtWidgets.QPushButton(self.widget)
        self.btnnone.setGeometry(QtCore.QRect(240, 190, 160, 120))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../images/none.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnnone.setIcon(icon2)
        self.btnnone.setIconSize(QtCore.QSize(160, 82))
        self.btnnone.setObjectName("btnnone")
        self.btnsqueze = QtWidgets.QPushButton(self.widget)
        self.btnsqueze.setGeometry(QtCore.QRect(240, 30, 160, 120))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../../images/squeze.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnsqueze.setIcon(icon3)
        self.btnsqueze.setIconSize(QtCore.QSize(150, 100))
        self.btnsqueze.setObjectName("btnsqueze")
        self.btnletterbox = QtWidgets.QPushButton(self.widget)
        self.btnletterbox.setGeometry(QtCore.QRect(30, 190, 160, 120))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../../images/letterbox.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnletterbox.setIcon(icon4)
        self.btnletterbox.setIconSize(QtCore.QSize(140, 110))
        self.btnletterbox.setObjectName("btnletterbox")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("Dialog", "<html><head/><body><p>Crop</p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p>Squeze</p></body></html>"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p>Letter Box</p></body></html>"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p>None</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


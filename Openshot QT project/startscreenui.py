# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'start-screen.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 580)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../xdg/openshot.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.lblrunwizard = QtWidgets.QLabel(Dialog)
        self.lblrunwizard.setObjectName("lblrunwizard")
        self.gridLayout.addWidget(self.lblrunwizard, 3, 0, 1, 1)
        self.lblotherscreen = QtWidgets.QLabel(Dialog)
        self.lblotherscreen.setObjectName("lblotherscreen")
        self.gridLayout.addWidget(self.lblotherscreen, 3, 1, 1, 1)
        self.frame_4 = QtWidgets.QFrame(Dialog)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.btncheckdependencies = QtWidgets.QPushButton(self.frame_4)
        self.btncheckdependencies.setGeometry(QtCore.QRect(0, 0, 120, 120))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../images/compositions-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btncheckdependencies.setIcon(icon1)
        self.btncheckdependencies.setIconSize(QtCore.QSize(120, 120))
        self.btncheckdependencies.setObjectName("btncheckdependencies")
        self.gridLayout.addWidget(self.frame_4, 2, 0, 1, 1)
        self.frame_3 = QtWidgets.QFrame(Dialog)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.btnopenlastproject = QtWidgets.QPushButton(self.frame_3)
        self.btnopenlastproject.setGeometry(QtCore.QRect(0, 0, 120, 120))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../images/folder-video.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnopenlastproject.setIcon(icon2)
        self.btnopenlastproject.setIconSize(QtCore.QSize(120, 120))
        self.btnopenlastproject.setObjectName("btnopenlastproject")
        self.gridLayout.addWidget(self.frame_3, 0, 2, 1, 1)
        self.lblquit = QtWidgets.QLabel(Dialog)
        self.lblquit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblquit.setObjectName("lblquit")
        self.gridLayout.addWidget(self.lblquit, 3, 2, 1, 1)
        self.lblopenproject = QtWidgets.QLabel(Dialog)
        self.lblopenproject.setObjectName("lblopenproject")
        self.gridLayout.addWidget(self.lblopenproject, 1, 1, 1, 1)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.btncreatenewproject = QtWidgets.QPushButton(self.frame)
        self.btncreatenewproject.setGeometry(QtCore.QRect(0, 0, 120, 120))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../../images/krita-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btncreatenewproject.setIcon(icon3)
        self.btncreatenewproject.setIconSize(QtCore.QSize(120, 120))
        self.btncreatenewproject.setObjectName("btncreatenewproject")
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.frame_6 = QtWidgets.QFrame(Dialog)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.btnclose = QtWidgets.QPushButton(self.frame_6)
        self.btnclose.setGeometry(QtCore.QRect(0, 0, 120, 120))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../../images/system-shutdown.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnclose.setIcon(icon4)
        self.btnclose.setIconSize(QtCore.QSize(120, 120))
        self.btnclose.setObjectName("btnclose")
        self.gridLayout.addWidget(self.frame_6, 2, 2, 1, 1)
        self.frame_5 = QtWidgets.QFrame(Dialog)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.btnothersscreens = QtWidgets.QPushButton(self.frame_5)
        self.btnothersscreens.setGeometry(QtCore.QRect(0, 0, 120, 120))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../../images/camera-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnothersscreens.setIcon(icon5)
        self.btnothersscreens.setIconSize(QtCore.QSize(120, 120))
        self.btnothersscreens.setObjectName("btnothersscreens")
        self.gridLayout.addWidget(self.frame_5, 2, 1, 1, 1)
        self.lblopenlastproject = QtWidgets.QLabel(Dialog)
        self.lblopenlastproject.setObjectName("lblopenlastproject")
        self.gridLayout.addWidget(self.lblopenlastproject, 1, 2, 1, 1)
        self.lblnew = QtWidgets.QLabel(Dialog)
        self.lblnew.setObjectName("lblnew")
        self.gridLayout.addWidget(self.lblnew, 1, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.btnopenexistingproject = QtWidgets.QPushButton(self.frame_2)
        self.btnopenexistingproject.setGeometry(QtCore.QRect(0, 0, 120, 120))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("../../images/folder-blue.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnopenexistingproject.setIcon(icon6)
        self.btnopenexistingproject.setIconSize(QtCore.QSize(120, 120))
        self.btnopenexistingproject.setObjectName("btnopenexistingproject")
        self.gridLayout.addWidget(self.frame_2, 0, 1, 1, 1)

        self.retranslateUi(Dialog)
        self.btnclose.clicked.connect(Dialog.reject)
        self.btncreatenewproject.clicked.connect(Dialog.accept)
        self.btnopenexistingproject.clicked.connect(Dialog.accept)
        self.btnopenlastproject.clicked.connect(Dialog.accept)
        self.btncheckdependencies.clicked.connect(Dialog.accept)
        self.btnothersscreens.clicked.connect(Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Start Screen"))
        self.lblrunwizard.setText(_translate("Dialog", "Check Dependencies"))
        self.lblotherscreen.setText(_translate("Dialog", "  Others Screens"))
        self.lblquit.setText(_translate("Dialog", "            Close"))
        self.lblopenproject.setText(_translate("Dialog", "<html><head/><body><p>Open existing</p><p> project</p></body></html>"))
        self.lblopenlastproject.setText(_translate("Dialog", "<html><head/><body><p>Open last project </p><p>opened</p></body></html>"))
        self.lblnew.setText(_translate("Dialog", "<html><head/><body><p>Create new</p><p> project</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


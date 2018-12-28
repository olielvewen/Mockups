# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'profile.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(410, 153)
        self.formLayout = QtWidgets.QFormLayout(Dialog)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.cboProfile = QtWidgets.QComboBox(Dialog)
        self.cboProfile.setObjectName("cboProfile")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.cboProfile)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.buttonBox)
        self.lblSize = QtWidgets.QLabel(Dialog)
        self.lblSize.setStyleSheet("font-weight:bold;")
        self.lblSize.setObjectName("lblSize")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lblSize)
        self.lblFPS = QtWidgets.QLabel(Dialog)
        self.lblFPS.setStyleSheet("font-weight:bold;")
        self.lblFPS.setObjectName("lblFPS")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lblFPS)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lblOther = QtWidgets.QLabel(Dialog)
        self.lblOther.setStyleSheet("font-weight:bold;")
        self.lblOther.setText("")
        self.lblOther.setObjectName("lblOther")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lblOther)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_6)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Choose a Profile"))
        self.label.setText(_translate("Dialog", "Profile:"))
        self.label_2.setText(_translate("Dialog", "Size:"))
        self.lblSize.setText(_translate("Dialog", "1920x1080"))
        self.lblFPS.setText(_translate("Dialog", "24"))
        self.label_3.setText(_translate("Dialog", "FPS:"))
        self.label_6.setText(_translate("Dialog", "Other:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


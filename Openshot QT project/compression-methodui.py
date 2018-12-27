# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'compression-method.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(460, 300)
        Dialog.setMaximumSize(QtCore.QSize(460, 300))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../xdg/openshot.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedKingdom))
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(20, 240, 421, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 40, 150, 15))
        self.label.setObjectName("label")
        self.cbosize = QtWidgets.QComboBox(Dialog)
        self.cbosize.setGeometry(QtCore.QRect(200, 30, 240, 30))
        self.cbosize.setObjectName("cbosize")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 130, 15))
        self.label_2.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label_2.setObjectName("label_2")
        self.spnsize = QtWidgets.QSpinBox(Dialog)
        self.spnsize.setGeometry(QtCore.QRect(200, 80, 191, 30))
        self.spnsize.setMaximum(10000)
        self.spnsize.setSingleStep(10)
        self.spnsize.setProperty("value", 700)
        self.spnsize.setObjectName("spnsize")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(400, 90, 40, 15))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 140, 150, 16))
        self.label_4.setObjectName("label_4")
        self.qualityslider = QtWidgets.QSlider(Dialog)
        self.qualityslider.setGeometry(QtCore.QRect(20, 210, 410, 24))
        self.qualityslider.setMaximum(100)
        self.qualityslider.setSliderPosition(85)
        self.qualityslider.setOrientation(QtCore.Qt.Horizontal)
        self.qualityslider.setObjectName("qualityslider")
        self.lcdquality = QtWidgets.QLCDNumber(Dialog)
        self.lcdquality.setGeometry(QtCore.QRect(270, 140, 121, 40))
        self.lcdquality.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lcdquality.setDigitCount(3)
        self.lcdquality.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdquality.setProperty("value", 85.0)
        self.lcdquality.setObjectName("lcdquality")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        self.qualityslider.valueChanged['int'].connect(self.lcdquality.display)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Compression Methods"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p>Compression Method:</p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p>Size:</p></body></html>"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p>MB</p></body></html>"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p>Quality (%):</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


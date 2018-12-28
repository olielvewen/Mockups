# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'presets.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(406, 326)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../../openshot_qt/xdg/openshot.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.cmbpresets = QtWidgets.QComboBox(Dialog)
        self.cmbpresets.setObjectName("cmbpresets")
        self.horizontalLayout.addWidget(self.cmbpresets)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(108, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.btnclearpreset = QtWidgets.QPushButton(Dialog)
        self.btnclearpreset.setObjectName("btnclearpreset")
        self.horizontalLayout_2.addWidget(self.btnclearpreset)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.btnsavecurrent = QtWidgets.QPushButton(Dialog)
        self.btnsavecurrent.setObjectName("btnsavecurrent")
        self.horizontalLayout_2.addWidget(self.btnsavecurrent)
        spacerItem2 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.listView = QtWidgets.QListView(Dialog)
        self.listView.setObjectName("listView")
        self.verticalLayout.addWidget(self.listView)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem3 = QtWidgets.QSpacerItem(188, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.btncancel = QtWidgets.QPushButton(Dialog)
        self.btncancel.setObjectName("btncancel")
        self.horizontalLayout_3.addWidget(self.btncancel)
        self.btnapply = QtWidgets.QPushButton(Dialog)
        self.btnapply.setObjectName("btnapply")
        self.horizontalLayout_3.addWidget(self.btnapply)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        self.btncancel.clicked.connect(Dialog.reject)
        self.btnapply.clicked.connect(Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Export with FFmpeg Command"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p>Presets:</p></body></html>"))
        self.btnclearpreset.setText(_translate("Dialog", "Delete Preset"))
        self.btnsavecurrent.setText(_translate("Dialog", "Save Current"))
        self.btncancel.setText(_translate("Dialog", "Cancel"))
        self.btnapply.setText(_translate("Dialog", "Export"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


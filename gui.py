# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Projects\sem-6project\gui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(857, 717)
        Dialog.setAutoFillBackground(True)
        self.topline = QtWidgets.QFrame(Dialog)
        self.topline.setGeometry(QtCore.QRect(0, 60, 851, 20))
        self.topline.setFrameShape(QtWidgets.QFrame.HLine)
        self.topline.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.topline.setObjectName("topline")
        self.search2 = QtWidgets.QPushButton(Dialog)
        self.search2.setGeometry(QtCore.QRect(630, 10, 101, 31))
        self.search2.setObjectName("search2")
        self.searchbox2 = QtWidgets.QLineEdit(Dialog)
        self.searchbox2.setEnabled(True)
        self.searchbox2.setGeometry(QtCore.QRect(160, 10, 471, 31))
        self.searchbox2.setMouseTracking(True)
        self.searchbox2.setAutoFillBackground(True)
        self.searchbox2.setText("")
        self.searchbox2.setObjectName("searchbox2")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(0, 680, 851, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.searchbox1 = QtWidgets.QLineEdit(Dialog)
        self.searchbox1.setEnabled(True)
        self.searchbox1.setGeometry(QtCore.QRect(160, 350, 461, 31))
        self.searchbox1.setMouseTracking(True)
        self.searchbox1.setText("")
        self.searchbox1.setObjectName("searchbox1")
        self.search1 = QtWidgets.QPushButton(Dialog)
        self.search1.setGeometry(QtCore.QRect(620, 350, 101, 31))
        self.search1.setObjectName("search1")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.search2.setText(_translate("Dialog", "Search"))
        self.search1.setText(_translate("Dialog", "Search"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

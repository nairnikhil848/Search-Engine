from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import QRect
import sys
import matplotlib
# import PyQt5.QtWidgets
from backend_engine import hello, unique_words, result, docslist


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: #1F1F1F;")  # 1F1F1F
        self.setWindowTitle("SearchWindow")
        self.setGeometry(400, 200, 1022, 717)

        suggestions = unique_words()
        # print(unique_words1)

        self.searchbox1 = QLineEdit(self)
        self.searchbox1.setGeometry(210, 320, 521, 51)
        self.searchbox1.setPlaceholderText("Search here")
        self.searchbox1.setStyleSheet(
            "border: 2px ; border-top-left-radius: 5px; border-bottom-left-radius: 5px; background-color: #333; color: white; font: bold 18px;font-family:Arial; padding-left: 5px; padding-right: 5px;")
        self.searchbox1.returnPressed.connect(self.pressed_clicked)

        self.searchbutton1 = QPushButton(self)
        self.searchbutton1.setGeometry(730, 320, 60, 51)
        self.searchbutton1.setStyleSheet(
            "border: 2px ; border-top-right-radius: 5px; border-bottom-right-radius: 5px;  background-color: #666;")
        self.searchbutton1.setIcon(QtGui.QIcon(
            "D:\Projects\sem-6project\search4.png"))
        self.searchbutton1.setIconSize(QtCore.QSize(40, 30))
        self.searchbutton1.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.searchbutton1.clicked.connect(self.pressed_clicked)

        self.completer = QCompleter(suggestions)
        self.completer.popup().setStyleSheet(
            "background-color:#333;color:white;font:bold 18px;font-family:Arial;border:2px;border-bottom-left-radius: 5px;border-bottom-right-radius: 5px;padding-left: 5px;margin-top:5px;")
        self.completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.searchbox1.setCompleter(self.completer)

        # self.pressed_clicked()  # delete after everything is done

    def pressed_clicked(self):
        text = self.searchbox1.text()
        results = result(text)
        #results = [1, 2, 3, 4]
        # print(type(result1))

        self.setStyleSheet("background-color:#0F0F0F;")

        self.controls = QWidget()  # Controls container widget.
        self.controlsLayout = QVBoxLayout()

        self.results = []

        for i in results:
            item = QPushButton(results[i])
            item.setStyleSheet(
                "background-color:#1F1F1F ; height: 150px;width: 100px;font-family: Arial; align=left ;font: bold 16px;padding-left: 5px;border-radius: 5px;color:white; margin-left: 50px;margin-right: 50px; border-style: outset;border-width: 1px; border-color:#2c2c2c; ")
            item.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
            item.clicked.connect(
                lambda checked, arg=i: self.open(arg))
            self.controlsLayout.addWidget(item)
            self.results.append(item)

        # for key, value in results:

        #     item = QPushButton(str(value))
        #     item.setStyleSheet(
        #         "background-color:#1F1F1F ; height: 150px;width: 100px;font-family: Arial; align=left ;font: bold 16px;padding-left: 5px;border-radius: 5px;color:white; margin-left: 50px;margin-right: 50px; border-style: outset;border-width: 1px; border-color:#2c2c2c; ")
        #     item.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        #     item.clicked.connect(
        #         lambda checked, arg=key: self.open(arg))
        #     self.controlsLayout.addWidget(item)
        #     self.results.append(item)

        spacer = QSpacerItem(1, 1, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.controlsLayout.addItem(spacer)
        self.controls.setLayout(self.controlsLayout)

        # Scroll Area Properties.
        self.scroll = QScrollArea()
        self.scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.controls)

        container = QWidget()
        containerLayout = QVBoxLayout()

        hbox = QHBoxLayout()

        self.icon = QPushButton(self)
        self.icon.setFixedWidth(60)
        self.icon.setFixedHeight(51)

        hbox.addWidget(self.icon)
        hbox.addWidget(self.searchbox1)
        hbox.addWidget(self.searchbutton1)
        hbox.addStretch()
        hbox.setSpacing(0)

        self.searchbox1.setFixedWidth(521)
        self.searchbox1.setFixedHeight(51)
        self.searchbutton1.setFixedWidth(60)
        self.searchbutton1.setFixedHeight(51)

        containerLayout.addLayout(hbox)
        containerLayout.addWidget(self.scroll)
        self.scroll.setStyleSheet(
            "background-color:#1F1F1F;margin-top:10px;border:none;border-radius: 10px;")

        container.setLayout(containerLayout)
        self.setCentralWidget(container)

    def open(self, text):
        mydialog = QDialog(self)

        mydialog.setStyleSheet(
            "background-color:white;")
        lineedit = QTextEdit(mydialog)
        lineedit.setFont(QFont('Times', 23))
        lineedit.setReadOnly(True)
        # ui = sub_search.Ui_Dialog()
        # ui.setupUi(mydialog)

        # lineedit = Qt.QlineEdit(self)
        lineedit.setGeometry(0, 0, 1050, 750)
        # lineedit.setStyleSheet(
        #     "width:500px;,height:500px;")
        documentlist = docslist()
        lineedit.setText(documentlist[text])
        mydialog.setModal(True)
        mydialog.exec()
        # mydialog.show()
        # print(str(text))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

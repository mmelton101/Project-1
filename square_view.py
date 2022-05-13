from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_window_square(object):
    def setupUi(self, window_square):
        window_square.setObjectName("window_square")
        window_square.resize(310, 400)
        window_square.setMinimumSize(QtCore.QSize(310, 400))
        window_square.setMaximumSize(QtCore.QSize(310, 400))
        self.centralwidget = QtWidgets.QWidget(window_square)
        self.centralwidget.setObjectName("centralwidget")
        self.button_back = QtWidgets.QPushButton(self.centralwidget)
        self.button_back.setGeometry(QtCore.QRect(110, 270, 93, 28))
        self.button_back.setObjectName("button_back")
        self.button_enter = QtWidgets.QPushButton(self.centralwidget)
        self.button_enter.setGeometry(QtCore.QRect(110, 110, 93, 28))
        self.button_enter.setObjectName("button_enter")
        self.text_area = QtWidgets.QTextBrowser(self.centralwidget)
        self.text_area.setGeometry(QtCore.QRect(110, 190, 150, 30))
        self.text_area.setMinimumSize(QtCore.QSize(150, 30))
        self.text_area.setMaximumSize(QtCore.QSize(150, 30))
        self.text_area.setObjectName("text_area")
        self.label_area = QtWidgets.QLabel(self.centralwidget)
        self.label_area.setGeometry(QtCore.QRect(20, 200, 81, 16))
        self.label_area.setObjectName("label_area")
        self.line_side = QtWidgets.QLineEdit(self.centralwidget)
        self.line_side.setGeometry(QtCore.QRect(110, 40, 113, 22))
        self.line_side.setObjectName("line_side")
        self.label_length = QtWidgets.QLabel(self.centralwidget)
        self.label_length.setGeometry(QtCore.QRect(20, 40, 81, 16))
        self.label_length.setObjectName("label_length")
        window_square.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(window_square)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 310, 26))
        self.menubar.setObjectName("menubar")
        window_square.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(window_square)
        self.statusbar.setObjectName("statusbar")
        window_square.setStatusBar(self.statusbar)

        self.retranslateUi(window_square)
        QtCore.QMetaObject.connectSlotsByName(window_square)

    def retranslateUi(self, window_square):
        _translate = QtCore.QCoreApplication.translate
        window_square.setWindowTitle(_translate("window_square", "Square Area"))
        self.button_back.setText(_translate("window_square", "Back"))
        self.button_enter.setText(_translate("window_square", "Enter"))
        self.label_area.setText(_translate("window_square", "Square Area:"))
        self.label_length.setText(_translate("window_square", "Length/Side:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window_square = QtWidgets.QMainWindow()
    ui = Ui_window_square()
    ui.setupUi(window_square)
    window_square.show()
    sys.exit(app.exec_())

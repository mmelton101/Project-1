from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_window_rectangle(object):
    def setupUi(self, window_rectangle):
        window_rectangle.setObjectName("window_rectangle")
        window_rectangle.resize(310, 480)
        window_rectangle.setMinimumSize(QtCore.QSize(310, 480))
        window_rectangle.setMaximumSize(QtCore.QSize(310, 480))
        self.centralwidget = QtWidgets.QWidget(window_rectangle)
        self.centralwidget.setObjectName("centralwidget")
        self.text_area = QtWidgets.QTextBrowser(self.centralwidget)
        self.text_area.setGeometry(QtCore.QRect(110, 280, 150, 30))
        self.text_area.setMinimumSize(QtCore.QSize(150, 30))
        self.text_area.setMaximumSize(QtCore.QSize(150, 30))
        self.text_area.setObjectName("text_area")
        self.line_height = QtWidgets.QLineEdit(self.centralwidget)
        self.line_height.setGeometry(QtCore.QRect(100, 40, 151, 22))
        self.line_height.setObjectName("line_height")
        self.line_length = QtWidgets.QLineEdit(self.centralwidget)
        self.line_length.setGeometry(QtCore.QRect(100, 130, 151, 22))
        self.line_length.setObjectName("line_length")
        self.label_height = QtWidgets.QLabel(self.centralwidget)
        self.label_height.setGeometry(QtCore.QRect(20, 40, 55, 16))
        self.label_height.setObjectName("label_height")
        self.label_length = QtWidgets.QLabel(self.centralwidget)
        self.label_length.setGeometry(QtCore.QRect(20, 130, 55, 16))
        self.label_length.setObjectName("label_length")
        self.button_enter = QtWidgets.QPushButton(self.centralwidget)
        self.button_enter.setGeometry(QtCore.QRect(100, 200, 93, 28))
        self.button_enter.setObjectName("button_enter")
        self.button_back = QtWidgets.QPushButton(self.centralwidget)
        self.button_back.setGeometry(QtCore.QRect(100, 360, 93, 28))
        self.button_back.setObjectName("button_back")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 290, 91, 16))
        self.label.setObjectName("label")
        window_rectangle.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(window_rectangle)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 310, 26))
        self.menubar.setObjectName("menubar")
        window_rectangle.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(window_rectangle)
        self.statusbar.setObjectName("statusbar")
        window_rectangle.setStatusBar(self.statusbar)

        self.retranslateUi(window_rectangle)
        QtCore.QMetaObject.connectSlotsByName(window_rectangle)

    def retranslateUi(self, window_rectangle):
        _translate = QtCore.QCoreApplication.translate
        window_rectangle.setWindowTitle(_translate("window_rectangle", "Rectangle Area"))
        self.label_height.setText(_translate("window_rectangle", "Height:"))
        self.label_length.setText(_translate("window_rectangle", "Length:"))
        self.button_enter.setText(_translate("window_rectangle", "Enter"))
        self.button_back.setText(_translate("window_rectangle", "Back"))
        self.label.setText(_translate("window_rectangle", "Rectangle Area:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window_rectangle = QtWidgets.QMainWindow()
    ui = Ui_window_rectangle()
    ui.setupUi(window_rectangle)
    window_rectangle.show()
    sys.exit(app.exec_())

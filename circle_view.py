from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Circle(object):
    def setupUi(self, Circle):
        Circle.setObjectName("Circle")
        Circle.resize(310, 400)
        Circle.setMinimumSize(QtCore.QSize(310, 400))
        Circle.setMaximumSize(QtCore.QSize(310, 400))
        self.centralwidget = QtWidgets.QWidget(Circle)
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
        self.line_radius = QtWidgets.QLineEdit(self.centralwidget)
        self.line_radius.setGeometry(QtCore.QRect(110, 40, 113, 22))
        self.line_radius.setObjectName("line_radius")
        self.label_radius = QtWidgets.QLabel(self.centralwidget)
        self.label_radius.setGeometry(QtCore.QRect(20, 40, 55, 16))
        self.label_radius.setObjectName("label_radius")
        Circle.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Circle)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 310, 26))
        self.menubar.setObjectName("menubar")
        Circle.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Circle)
        self.statusbar.setObjectName("statusbar")
        Circle.setStatusBar(self.statusbar)

        self.retranslateUi(Circle)
        QtCore.QMetaObject.connectSlotsByName(Circle)

    def retranslateUi(self, Circle):
        _translate = QtCore.QCoreApplication.translate
        Circle.setWindowTitle(_translate("Circle", "Circle Area"))
        self.button_back.setText(_translate("Circle", "Back"))
        self.button_enter.setText(_translate("Circle", "Enter"))
        self.label_area.setText(_translate("Circle", "Circle Area:"))
        self.label_radius.setText(_translate("Circle", "Radius:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Circle = QtWidgets.QMainWindow()
    ui = Ui_Circle()
    ui.setupUi(Circle)
    Circle.show()
    sys.exit(app.exec_())

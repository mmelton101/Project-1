from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_window_shape(object):
    def setupUi(self, window_shape):
        window_shape.setObjectName("window_shape")
        window_shape.resize(320, 320)
        window_shape.setMinimumSize(QtCore.QSize(320, 320))
        window_shape.setMaximumSize(QtCore.QSize(320, 320))
        self.centralwidget = QtWidgets.QWidget(window_shape)
        self.centralwidget.setObjectName("centralwidget")
        self.radio_circle = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_circle.setGeometry(QtCore.QRect(40, 60, 95, 20))
        self.radio_circle.setObjectName("radio_circle")
        self.radio_rectangle = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_rectangle.setGeometry(QtCore.QRect(190, 60, 95, 20))
        self.radio_rectangle.setObjectName("radio_rectangle")
        self.radio_square = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_square.setGeometry(QtCore.QRect(40, 120, 95, 20))
        self.radio_square.setObjectName("radio_square")
        self.radio_triangle = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_triangle.setGeometry(QtCore.QRect(190, 120, 95, 20))
        self.radio_triangle.setObjectName("radio_triangle")
        self.button_enter = QtWidgets.QPushButton(self.centralwidget)
        self.button_enter.setGeometry(QtCore.QRect(110, 180, 93, 28))
        self.button_enter.setObjectName("button_enter")
        window_shape.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(window_shape)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 320, 26))
        self.menubar.setObjectName("menubar")
        window_shape.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(window_shape)
        self.statusbar.setObjectName("statusbar")
        window_shape.setStatusBar(self.statusbar)

        self.retranslateUi(window_shape)
        QtCore.QMetaObject.connectSlotsByName(window_shape)

    def retranslateUi(self, window_shape):
        _translate = QtCore.QCoreApplication.translate
        window_shape.setWindowTitle(_translate("window_shape", "Shape Selection"))
        self.radio_circle.setText(_translate("window_shape", "Circle"))
        self.radio_rectangle.setText(_translate("window_shape", "Rectangle"))
        self.radio_square.setText(_translate("window_shape", "Square"))
        self.radio_triangle.setText(_translate("window_shape", "Triangle"))
        self.button_enter.setText(_translate("window_shape", "Enter"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window_shape = QtWidgets.QMainWindow()
    ui = Ui_window_shape()
    ui.setupUi(window_shape)
    window_shape.show()
    sys.exit(app.exec_())

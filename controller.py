from PyQt5.QtWidgets import *
from view import Ui_window_shape


class Controller(QMainWindow, Ui_window_shape):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.shape = ""

        self.button_enter.clicked.connect(lambda: self.shape_select())

    def shape_select(self):
        """
        Determines what radio button was selected when the enter button was pressed and closes the window
        """
        if self.radio_circle.isChecked():
            self.shape = "Circle"
            self.close()

        if self.radio_rectangle.isChecked():
            self.shape = "Rectangle"
            self.close()

        if self.radio_square.isChecked():
            self.shape = "Square"
            self.close()

        if self.radio_triangle.isChecked():
            self.shape = "Triangle"
            self.close()

    def get_shape(self):
        """
        returns self.shape.
        :return: self.shape
        """
        return self.shape

    def set_shape(self):
        """
        sets self.shape = "".
        """
        self.shape = ""

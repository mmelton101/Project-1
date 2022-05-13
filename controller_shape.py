from PyQt5.QtWidgets import *
from circle_view import Ui_Circle
from rectangle_view import Ui_window_rectangle
from square_view import Ui_window_square
from triangle_view import Ui_window_triangle
import mathieson_melton as mm


class ControllerCircle(QMainWindow, Ui_Circle):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.button_enter.clicked.connect(lambda: self.area())
        self.button_back.clicked.connect(lambda: self.back())

    def area(self):
        """
        Determines if the input is a number and if it is the area of the shape will be calculated and printed to the window.
        If the input is not a number then something will be printed to the screen saying that it is invalid input.
        """
        self.text_area.clear()
        if self.is_number(self.line_radius.text()):
            self.text_area.setText(str(mm.circle(float(self.line_radius.text()))))
            self.line_radius.clear()
        else:
            self.line_radius.setText("That is not a valid number")

    def is_number(self, string: str) -> bool:
        """
        Determines if a string is a float or not
        :param string: a string of characters
        :return: Returns True if string is a float and False if string is not a float
        """
        try:
            float(string)
            return True
        except ValueError:
            return False

    def back(self):
        """
        Closes the window and returns to the main menu
        """
        self.close()


class ControllerSquare(QMainWindow, Ui_window_square):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.button_enter.clicked.connect(lambda: self.area())
        self.button_back.clicked.connect(lambda: self.back())

    def area(self):
        """
        Determines if the input is a number and if it is the area of the shape will be calculated and printed to the window.
        If the input is not a number then something will be printed to the screen saying that it is invalid input.
        """
        self.text_area.clear()
        if self.is_number(self.line_side.text()):
            self.text_area.setText(str(mm.square(float(self.line_side.text()))))
            self.line_side.clear()
        else:
            self.line_side.setText("That is not a valid number")

    def is_number(self, string: str) -> bool:
        """
        Determines if a string is a float or not
        :param string: a string of characters
        :return: Returns True if string is a float and False if string is not a float
        """
        try:
            float(string)
            return True
        except ValueError:
            return False

    def back(self):
        """
        Closes the window and returns to the main menu
        """
        self.close()


class ControllerTriangle(QMainWindow, Ui_window_triangle):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.button_enter.clicked.connect(lambda: self.area())
        self.button_back.clicked.connect(lambda: self.back())

    def area(self):
        """
        Determines if the input is a number and if it is the area of the shape will be calculated and printed to the window.
        If the input is not a number then something will be printed to the screen saying that it is invalid input.
        """
        self.text_area.clear()
        if self.is_number(self.line_base.text()) and self.is_number(self.line_height.text()):
            self.text_area.setText(str(mm.triangle(float(self.line_base.text()), float(self.line_height.text()))))
            self.line_base.clear()
            self.line_height.clear()
        else:
            self.line_base.setText("not a valid number")
            self.line_height.setText("not a valid number")

    def is_number(self, string: str) -> bool:
        """
        Determines if a string is a float or not
        :param string: a string of characters
        :return: Returns True if string is a float and False if string is not a float
        """
        try:
            float(string)
            return True
        except ValueError:
            return False

    def back(self):
        """
        Closes the window and returns to the main menu
        """
        self.close()


class ControllerRectangle(QMainWindow, Ui_window_rectangle):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.button_enter.clicked.connect(lambda: self.area())
        self.button_back.clicked.connect(lambda: self.back())

    def area(self):
        """
        Determines if the input is a number and if it is the area of the shape will be calculated and printed to the window.
        If the input is not a number then something will be printed to the screen saying that it is invalid input.
        """
        self.text_area.clear()
        if self.is_number(self.line_length.text()) and self.is_number(self.line_height.text()):
            self.text_area.setText(str(mm.rectangle(float(self.line_length.text()), float(self.line_height.text()))))
            self.line_length.clear()
            self.line_height.clear()
        else:
            self.line_length.setText("not a valid number")
            self.line_height.setText("not a valid number")

    def is_number(self, string: str) -> bool:
        """
        Determines if a string is a float or not
        :param string: a string of characters
        :return: Returns True if string is a float and False if string is not a float
        """
        try:
            float(string)
            return True
        except ValueError:
            return False

    def back(self):
        """
        Closes the window and returns to the main menu
        """
        self.close()

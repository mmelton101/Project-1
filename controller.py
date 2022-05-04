from PyQt5.QtWidgets import *
from view import Ui_mainWindow
import mathieson_melton as mm


class Controller(QMainWindow, Ui_mainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.button_enter.clicked.connect(lambda: self.shape_select())

    def shape_select(self):
        if self.radio_circle.isChecked():
            self.line_area.setText(str(mm.circle(float(self.line_radiusheight.text()))))
            self.line_radiusheight.clear()
            self.line_baselength.clear()

        if self.radio_rectangle.isChecked():
            self.line_area.setText(str(mm.rectangle(float(self.line_baselength.text()), float(self.line_radiusheight.text()))))
            self.line_radiusheight.clear()
            self.line_baselength.clear()

        if self.radio_square.isChecked():
            self.line_area.setText(str(mm.square(float(self.line_radiusheight.text()))))
            self.line_radiusheight.clear()
            self.line_baselength.clear()

        if self.radio_triangle.isChecked():
            self.line_area.setText(str(mm.triangle(float(self.line_baselength.text()), float(self.line_radiusheight.text()))))
            self.line_radiusheight.clear()
            self.line_baselength.clear()

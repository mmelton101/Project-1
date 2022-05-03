from PyQt5.QtWidgets import *
from view import Ui_mainWindow


class Controller(QMainWindow, Ui_mainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.button_enter.clicked.connect(lambda: self.shape_select())

    def shape_select(self):
        pass

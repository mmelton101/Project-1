from controller import *
from controller_shape import *


def main():
    """
    Starts the program and determines if it should close or keep running
    """
    program_running = True
    app = QApplication([])
    while program_running:
        program_running = False
        window = Controller()
        window.show()
        app.exec_()
        if window.get_shape() != "":
            if window.get_shape() == "Circle":
                window_circle = ControllerCircle()
                window_circle.show()
                app.exec_()
                window.set_shape()

            if window.get_shape() == "Rectangle":
                window_rectangle = ControllerRectangle()
                window_rectangle.show()
                app.exec_()
                window.set_shape()

            if window.get_shape() == "Square":
                window_square = ControllerSquare()
                window_square.show()
                app.exec_()
                window.set_shape()

            if window.get_shape() == "Triangle":
                window_triangle = ControllerTriangle()
                window_triangle.show()
                app.exec_()
                window.set_shape()

            program_running = True


if __name__ == "__main__":
    main()

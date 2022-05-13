from math import pi


def circle(radius: float) -> float:
    """
    Calculates the area of a circle
    :param radius: radius of the circle
    :return: calculated area of the circle
    """
    area = pi * (radius ** 2)
    return area


def rectangle(length: float, width: float) -> float:
    """
    Calculates the area of a rectangle
    :param length: length of the rectangle
    :param width: width of the rectangle
    :return: calculated area of the rectangle
    """
    area = length * width
    return area


def square(length: float) -> float:
    """
    Calculates the area of a square
    :param length: the length of a side of a square
    :return: calculated area of the square
    """
    area = length ** 2
    return area


def triangle(base: float, height: float) -> float:
    """
    Calculates the area of a triangle
    :param base: base of the triangle
    :param height: height of the triangle
    :return:
    """
    area = .5 * base * height
    return area

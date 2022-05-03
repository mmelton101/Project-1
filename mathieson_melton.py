from math import pi


def circle(radius: float) -> float:
    if (type(radius) == int or type(radius) == float) and radius > 0:
        area = pi * (radius ** 2)
        return area
    else:
        raise ValueError


def rectangle(length: float, width: float) -> float:
    if ((type(length) == int or type(length) == float) and (type(width) == int or type(width) == float)) and (length > 0 and width > 0):
        area = length * width
        return area
    else:
        raise ValueError


def square(length: float) -> float:
    if (type(length) == int or type(length) == float) and length > 0:
        area = length ** 2
        return area
    else:
        raise ValueError


def triangle(base: float, height: float) -> float:
    if ((type(base) == int or type(base) == float) and (type(height) == int or type(height) == float)) and (base > 0 and height > 0):
        area = .5 * base * height
        return area
    else:
        raise ValueError

import math


def plus(a, b):
    return a + b


def minus(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def power(a, b):
    return math.pow(a, b)


def square_root(a):
    if a < 0:
        raise ValueError("Cannot take the square root of a negative number.")
    return math.sqrt(a)


def factorial(n):
    if n < 0:
        raise ValueError("Cannot take the factorial of a negative number.")
    return math.factorial(n)


def sin(a):
    return math.sin(math.radians(a))


def cos(a):
    return math.cos(math.radians(a))


def tan(a):
    return math.tan(math.radians(a))


def asin(a, b):
    if a < -b or a > b:
        raise ValueError("Input for arcsin must be in the range [-b, b].")
    return math.degrees(math.asin(a / b))


def acos(a, b):
    if a < -b or a > b:
        raise ValueError("Input for arccos must be in the range [-b, b].")
    return math.degrees(math.acos(a / b))


def atan(a, b):
    return math.degrees(math.atan(a / b))


def circumference(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    return 2 * math.pi * radius


def area_circle(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    return math.pi * radius**2


def area_rectangle(length, width):
    if length < 0 or width < 0:
        raise ValueError("Length and width cannot be negative.")
    return length * width

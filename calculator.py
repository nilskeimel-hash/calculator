import math


def plus(a:float, b:float) -> float:
    return a + b


def minus(a:float, b:float) -> float:
    return a - b


def multiply(a:float, b:float) -> float:
    return a * b


def divide(a:float, b:float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def power(a:float, b:float) -> float:
    return math.pow(a, b)


def square_root(a:float) -> float:
    if a < 0:
        raise ValueError("Cannot take the square root of a negative number.")
    return math.sqrt(a)


def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Cannot take the factorial of a negative number.")
    return math.factorial(n)


def sin(a: float) -> float:
    return math.sin(math.radians(a))


def cos(a: float) -> float:
    return math.cos(math.radians(a))


def tan(a: float) -> float:
    return math.tan(math.radians(a))


def asin(a: float, b: float) -> float:
    if a < -b or a > b:
        raise ValueError("Input for arcsin must be in the range [-b, b].")
    return math.degrees(math.asin(a / b))


def acos(a: float, b: float) -> float:
    if a < -b or a > b:
        raise ValueError("Input for arccos must be in the range [-b, b].")
    return math.degrees(math.acos(a / b))


def atan(a: float, b: float) -> float:
    return math.degrees(math.atan(a / b))


def circumference(radius: float) -> float:
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    return 2 * math.pi * radius


def area_circle(radius: float) -> float:
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    return math.pi * radius**2


def area_rectangle(length: float, width: float) -> float:
    if length < 0 or width < 0:
        raise ValueError("Length and width cannot be negative.")
    return length * width

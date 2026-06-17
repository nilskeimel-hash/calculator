import calculator

list_of_operations = [
    "+",
    "-",
    "*",
    "/",
    "^",
    "sqrt",
    "!",
    "sin",
    "cos",
    "tan",
    "asin",
    "acos",
    "atan",
    "circumference",
    "area_circle",
    "area_rectangle",
]

while True:
    print("Welcome to the calculator!")
    print(f"Available operations: {', '.join(list_of_operations)}")
    operation = input("Enter an operation (or 'exit' to quit): ")
    if operation == "exit":
        print("Until the next time!")
        break
    elif operation in ["+", "-", "*", "/", "^"]:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        if operation == "+":
            result = calculator.plus(a, b)
        elif operation == "-":
            result = calculator.minus(a, b)
        elif operation == "*":
            result = calculator.multiply(a, b)
        elif operation == "/":
            try:
                result = calculator.divide(a, b)
            except ValueError as e:
                print(e)
                continue
        elif operation == "^":
            result = calculator.power(a, b)
        print(f"The result is: {result}")
    elif operation == "sqrt":
        a = float(input("Enter the number: "))
        try:
            result = calculator.square_root(a)
            print(f"The square root of {a} is: {result}")
        except ValueError as e:
            print(e)
            continue
    elif operation == "!":
        n = int(input("Enter a non-negative integer: "))
        try:
            result = calculator.factorial(n)
            print(f"The factorial of {n} is: {result}")
        except ValueError as e:
            print(e)
            continue
    elif operation == "sin":
        a = float(input("Enter the angle in degrees: "))
        result = calculator.sin(a)
        print(f"The sine of {a} degrees is: {result}")
    elif operation == "cos":
        a = float(input("Enter the angle in degrees: "))
        result = calculator.cos(a)
        print(f"The cosine of {a} degrees is: {result}")
    elif operation == "tan":
        a = float(input("Enter the angle in degrees: "))
        result = calculator.tan(a)
        print(f"The tangent of {a} degrees is: {result}")
    elif operation == "asin":
        a = float(input("Enter the value for Gegenkathete: "))
        b = float(input("Enter the hypotenuse: "))
        try:
            result = calculator.asin(a, b)
            print(f"The arcsine of {a}/{b} is: {result}")
        except ValueError as e:
            print(e)
    elif operation == "acos":
        a = float(input("Enter the value for Ankathete: "))
        b = float(input("Enter the hypotenuse: "))
        result = calculator.acos(a, b)
        print(f"The arccosine of {a}/{b} is: {result}")
    elif operation == "atan":
        a = float(input("Enter the value for Gegenkathete: "))
        b = float(input("Enter the Ankathete: "))
        try:
            result = calculator.atan(a, b)
            print(f"The arctangent of {a}/{b} is: {result}")
        except ValueError as e:
            print(e)
    elif operation == "circumference":
        radius = float(input("Enter the radius of the circle: "))
        try:
            result = calculator.circumference(radius)
            print(f"The circumference of the circle with radius {radius} is: {result}")
        except ValueError as e:
            print(e)
    elif operation == "area_circle":
        radius = float(input("Enter the radius of the circle: "))
        try:
            result = calculator.area_circle(radius)
            print(f"The area of the circle with radius {radius} is: {result}")
        except ValueError as e:
            print(e)
    elif operation == "area_rectangle":
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        try:
            result = calculator.area_rectangle(length, width)
            print(
                f"The area of the rectangle with length {length} and width {width} is: {result}"
            )
        except ValueError as e:
            print(e)
    else:
        print("Invalid operation. Please try again.")

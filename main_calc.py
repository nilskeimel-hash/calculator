import calculator

TWO_NUMBER_OPS = {
    "+": calculator.plus,
    "-": calculator.minus,
    "*": calculator.multiply,
    "/": calculator.divide,
    "^": calculator.power,
    "asin": calculator.asin,
    "acos": calculator.acos,
    "atan": calculator.atan,
    "area_rectangle": calculator.area_rectangle,
}

ONE_NUMBER_OPS = {
    "sqrt": calculator.square_root,
    "sin": calculator.sin,
    "cos": calculator.cos,
    "tan": calculator.tan,
    "circumference": calculator.circumference,
    "area_circle": calculator.area_circle,
}

INTEGER_OPS = {"!": calculator.factorial}


while True:
    print("Welcome to the calculator!")
    print(
        f"Available operations: {', '.join(list(TWO_NUMBER_OPS.keys()) + list(ONE_NUMBER_OPS.keys()) + list(INTEGER_OPS.keys()))}"
    )
    operation = input("Enter an operation (or 'exit' to quit): ")
    if operation.lower() == "exit":
        print("Exiting the calculator. Goodbye!")
        break
    elif operation in TWO_NUMBER_OPS:
        try:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            result = TWO_NUMBER_OPS[operation](a, b)
            print(f"The result is: {result}")
        except ValueError as e:
            print(e)
            continue
    elif operation in ONE_NUMBER_OPS:
        try:
            a = float(input("Enter a number: "))
            result = ONE_NUMBER_OPS[operation](a)
            print(f"The result is: {result}")
        except ValueError as e:
            print(e)
            continue
    elif operation in INTEGER_OPS:
        try:
            n = int(input("Enter an integer: "))
            result = INTEGER_OPS[operation](n)
            print(f"The result is: {result}")
        except ValueError as e:
            print(e)
            continue
    else:
        print("Invalid operation. Please try again.")

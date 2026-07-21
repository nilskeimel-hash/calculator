import calculator

def log_history(line: str) -> None:
    with open("history.txt", "a") as history_file:
        history_file.write(line + "\n")

def read_history() -> list[str]:
    try:
        with open("history.txt", "r") as history_file:
            return [line.strip() for line in history_file.readlines()]
    except FileNotFoundError:
        return []

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

COMMAND_OPS = {
    "history" : read_history,
}

ALLE_OPS = TWO_NUMBER_OPS | ONE_NUMBER_OPS | INTEGER_OPS | COMMAND_OPS


while True:
    print("Welcome to the calculator!")
    print(
        f"Available operations: {', '.join(ALLE_OPS)}"
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
            log_history(f"{a} {operation} {b} = {result}")
            print(f"The result is: {result}")
        except calculator.CalculationError as e:
            print(f"Math error: {e}")
        except ValueError:
            print("Please enter a valid number.")
            continue
    elif operation in ONE_NUMBER_OPS:
        try:
            a = float(input("Enter a number: "))
            result = ONE_NUMBER_OPS[operation](a)
            log_history(f"{operation} of {a} = {result}")
            print(f"The result is: {result}")
        except calculator.CalculationError as e:
            print(f"Math error: {e}")
        except ValueError:
            print("Please enter a valid number.")
            continue
    elif operation in INTEGER_OPS:
        try:
            n = int(input("Enter an integer: "))
            result = INTEGER_OPS[operation](n)
            log_history(f"{n}{operation} = {result}")
            print(f"The result is: {result}")
        except calculator.CalculationError as e:
            print(f"Math error: {e}")
        except ValueError:
            print("Please enter a valid integer.")
            continue
    elif operation in COMMAND_OPS:
        lines = COMMAND_OPS[operation]()
        if lines:
            print("History:")
            for line in lines:
                print(line)
        else:
            print("No history found.")

    else:
        print("Invalid operation. Please try again.")

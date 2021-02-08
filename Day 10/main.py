import grey
import art
import time


def add(n1, n2):
    """Addition Calculator for 2 numbers"""
    return n1 + n2


def subtract(n1, n2):
    """Subtraction Calculator for 2 numbers"""
    return n1 - n2


def multiply(n1, n2):
    """Multiplication Calculator for 2 numbers"""
    return n1 * n2


def divide(n1, n2):
    """Division Calculator for 2 numbers"""
    return n1 / n2


def main():
    """This is the main function of the program. It starts the simple calculator process."""

    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
    }

    continue_on = True

    first_operation = True

    previous_answer = int

    while continue_on is True:
        print(art.logo + "\n")

        if continue_on is True and first_operation is not True:
            num1 = previous_answer
            print(f"The first number is {previous_answer}")
        else:
            num1 = int(input("What's the first number?: "))
        print("")

        for key in operations:
            print(key)
        print("")

        operation_symbol = str(input("Pick an operation_symbol: "))
        print("")

        num2 = int(input("What's the second number?: "))
        print("")

        answer = operations[operation_symbol](num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        print("\nHere are your options forward:\n\n1. Continue the calculation using the previous answer.\n2. Start a "
              "new calculation.\n3. Quit the application.\n")

        stop_or_continue = str(input("Answer with either '1', '2' or '3', or 'continue', 'new' or 'stop': ")).lower()

        if stop_or_continue == "1" or stop_or_continue == "continue":
            first_operation = False
            grey.clear()
            previous_answer = answer
        elif stop_or_continue == "2" or stop_or_continue == "new":
            grey.clear()
            previous_answer = int
            first_operation = True
        elif stop_or_continue == "3" or stop_or_continue == "stop":
            print("Quitting")
            time.sleep(2)
            grey.clear()
            continue_on = False
        else:
            print("Your input was invalid. Going to start a new calculation.")
            time.sleep(6)
            grey.clear()
            previous_answer = int
            first_operation = True


main()

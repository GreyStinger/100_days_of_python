import time

import art
import grey


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
    previous_operations = []

    while continue_on is True:
        print(art.logo + "\n")

        if first_operation is False:
            print("Your previous calculations were:")
            for string_number in range(len(previous_operations)):
                print(previous_operations[string_number])
            print("")
            num1 = previous_answer
            print(f"Your last answer and now first number is {previous_answer}")
        else:
            num1 = float(input("What's the first number?: "))
        print("")

        for key in operations:
            print(key)
        print("")

        operation_symbol = str(input("Pick an operation_symbol: "))
        print("")

        if operation_symbol not in operations:
            print("Please enter a valid operational symbol.\nThe program will be restarted.\n")
            time.sleep(8)
            continue

        num2 = float(input("What's the second number?: "))
        print("")

        answer = operations[operation_symbol](num1, num2)

        current_operation = f"{num1} {operation_symbol} {num2} = {answer}"

        print(current_operation)
        print("\nHere are your options forward:\n\n1. Continue the calculation using the previous answer.\n2. Start a "
              "new calculation.\n3. Quit the application.\n")

        stop_or_continue = str(input("Answer with either '1', '2' or '3', or 'continue', 'new' or 'stop': ")).lower()

        if stop_or_continue == "1" or stop_or_continue == "continue":
            grey.clear()
            first_operation = False
            previous_answer = answer
            previous_operations.append(current_operation)
        elif stop_or_continue == "2" or stop_or_continue == "new":
            grey.clear()
            previous_answer = int
            first_operation = True
            previous_operations = []
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


if __name__ == '__main__':
    main()

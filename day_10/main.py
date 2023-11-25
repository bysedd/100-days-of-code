from art import logo
from calculator import operations


def calculator() -> None:
    """
    This method runs the calculator.
    """
    print(logo)
    number1 = float(input("What's the first number? "))
    print("\n".join(operations.keys()))
    continue_flag = True

    while continue_flag:
        operation = input("Pick an operation: ")
        number2 = float(input("What's the next number? "))
        try:
            answer = operations[operation](number1, number2)
            print(f"{number1} {operation} {number2} = {answer}")
            number1 = answer
            continue_flag = (
                input(
                    f"Type 'y' to continue calculating with {number1}, or 'n' to exit: "
                )
                .strip()
                .lower()
                == "y"
            )
        except KeyError:
            print("Invalid operation. Try again.")


calculator()

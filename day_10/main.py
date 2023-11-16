from art import logo
from calculator import operations, Number


def ask_to_continue(number: Number) -> bool:
    """
    This method asks the user if they want to continue using the calculator.

    :param number: The last answer.
    """
    return (
        input(f"Type 'y' to continue calculating with {number}, or 'n' to exit: ")
        .strip()
        .lower()
        == "y"
    )


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
        answer = operations[operation](number1, number2)
        print(f"{number1} {operation} {number2} = {answer}")
        number1 = answer
        continue_flag = ask_to_continue(answer)


calculator()

from typing import TypeVar

Number = TypeVar("Number", int, float)


def add(a: Number, b: Number) -> Number:
    """
    This method adds two numbers together.

    :param a: The first number to add.
    :param b: The second number to add.
    :return: The sum of a and b.
    """
    return a + b


def subtract(a: Number, b: Number) -> Number:
    """
    This method subtracts one number from another.

    :param a: The number from which to subtract.
    :param b: The number to subtract.
    :return: The result of a minus b.
    """
    return a - b


def multiply(a: Number, b: Number) -> Number:
    """
    This method multiplies two numbers together.

    :param a: The first number to multiply.
    :param b: The second number to multiply.
    :return: The product of a and b.
    """
    return a * b


def divide(a: Number, b: Number) -> Number:
    """
    This method divides one number by another.

    :param a: The dividend.
    :param b: The divisor.
    :return: The quotient of a divided by b.
    :raises ZeroDivisionError: If b is zero.
    """
    return a / b


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

import os
from random import choice

from art import logo, vs
from game_data import data


def format_data(account: dict[str, str | int]) -> str:
    """
    Format the account data into printable format.
    :param account: A dictionary containing the account data.
    :return: A string containing the formatted account data.
    """
    return f"{account['name']}, a {account['description']}, from {account['country']}"


def check_answer(guess: str, a_followers: int, b_followers: int) -> bool:
    """
    Checks followers against user's guess and returns True if they got it right.
    :param guess: The user's guess.
    :param a_followers: Account A's follower count.
    :param b_followers: Account B's follower count.
    :return: True if the user's guess is correct, False otherwise.
    """
    if a_followers > b_followers:
        return guess == "a"
    return guess == "b"


def clear() -> None:
    """
    Clears the terminal.
    """
    os.system("cls" if os.name == "nt" else "clear")


print(logo)
score = 0
account_a = choice(data)
account_b = choice(data)

while True:
    while account_a == account_b:
        account_b = choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    is_correct = check_answer(user_guess, account_a["follower_count"], account_b["follower_count"])

    clear()
    print(logo)

    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}")
        account_a = account_b
        account_b = choice(data)
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        break

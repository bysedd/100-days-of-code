import os
from typing import List, Dict

from art import logo

# List of dictionaries to store the name and bid of each person
people: List[Dict[str, str]] = []


def clear_screen() -> None:
    """
    Function to clear the console screen.
    It checks the operating system and uses the appropriate command.
    """
    os.system("cls" if os.name == "nt" else "clear")


def add_person() -> None:
    """
    Function to add a person to the auction.
    It asks for the person's name and bid, then adds them to the 'people' list.
    """
    name = input("What's your name? ").strip().title()
    bid = int(input("What's your bid? $"))
    people.append({"name": name, "bid": bid})


def find_winner() -> None:
    """
    Function to find the person with the highest bid.
    It finds the person with the maximum bid in the 'people' list and prints their name and bid.
    """
    winner = max(people, key=lambda p: p["bid"])
    print(f"The winner is {winner['name']} with a bid of ${winner['bid']}.")


print(logo)
print("Welcome to the secret auction program.")

while True:
    add_person()
    more_people = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    if more_people == "no":
        break
    clear_screen()

find_winner()

import os
from random import choice

from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []
keep_playing = True
user_score, computer_score = 0, 0


def show_results() -> None:
    global user_cards, computer_cards, user_score, computer_score

    print(f"\tYour final hand: {user_cards}, final score: {user_score}")
    print(f"\tComputer's final hand: {computer_cards}, final score: {computer_score}")

    if user_score > 21:
        print("You went over. You lose 😭")
    elif computer_score > 21:
        print("Opponent went over. You win 😁")
    elif result := compare():
        print(result)
    else:
        if user_score > computer_score:
            print("You win 😃")
        elif user_score < computer_score:
            print("You lose 😤")
        else:
            print("It's a draw 🙃")


def compare() -> str:
    global user_cards, computer_cards, user_score

    result = ""

    # Does the user or computer have a blackjack? (ace + 10)
    if 11 in user_cards and 10 in user_cards:
        result = "You win with a Blackjack 😎"
    elif 11 in computer_cards and 10 in computer_cards:
        result = "You lose, opponent has Blackjack 😱"

    # Is the user score over 21?
    if user_score > 21:
        # Do they have an "Ace"?
        if 11 in user_cards:
            # If the ace counts as a 1 instead of 11, are they still over 21?
            user_cards.remove(11)
            user_cards.append(1)
            user_score = sum(user_cards)
            if user_score > 21:
                result = "You went over. You lose 😭"
        else:
            result = "You went over. You lose 😭"

    return result


def reset_game():
    global cards, user_cards, computer_cards
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user_cards = []
    computer_cards = []


def keep_playing_game() -> None:
    global keep_playing
    keep_playing = input(
        "Do you want to play a game of Blackjack? Type 'y' or 'n': "
    ).lower()
    keep_playing = True if keep_playing == "y" else False

    if keep_playing:
        os.system("cls" if os.name == "nt" else "clear")
        reset_game()
        print(logo)


def deal_cards(__cards):
    return [choice(__cards) for _ in range(2)]


def calculate_score(__cards):
    return sum(__cards)


def play_game():
    global user_cards, computer_cards, keep_playing

    if (
        input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
        == "y"
    ):
        print(logo)

        while keep_playing:
            if not user_cards and not computer_cards:
                # Deal 2 cards to each player
                user_cards = deal_cards(cards)
                computer_cards = deal_cards(cards)

            user_score = calculate_score(user_cards)
            computer_score = calculate_score(computer_cards)

            if compare():
                show_results()
                keep_playing_game()
                continue

            print(f"\tYour cards: {user_cards}, current score: {user_score}")
            print(f"\tComputer's first card: {computer_cards[0]}")

            get_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if get_card == "y":
                user_cards.append(choice(cards))
            elif get_card == "n":
                while user_score != 0 and computer_score < 17:
                    computer_cards.append(choice(cards))
                    computer_score = calculate_score(computer_cards)
                show_results()
                keep_playing_game()
            else:
                print("Invalid input")
                keep_playing_game()


if __name__ == "__main__":
    play_game()

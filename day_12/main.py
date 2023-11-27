from random import randint


def get_attempts(difficulty: str, /) -> int | None:
    """
    Returns the number of attempts based on the difficulty.
    :param difficulty: The difficulty level.
    :return: The number of attempts.
    """
    match difficulty:
        case "easy":
            return 10
        case "hard":
            return 5
        case _:
            print("Invalid difficulty.")
            exit()


def game() -> None:
    """
    The main game function.
    """
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number = randint(1, 100)
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    attempts = get_attempts(difficulty)

    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == number:
            print(f"You got it! The answer was {number}.")
            exit()
        elif guess > number:
            print("Too high.")
        elif guess < number:
            print("Too low.")
        attempts -= 1
        if attempts > 0:
            print("Guess again.")
        else:
            print("You've run out of guesses, you lose.")
            exit()


if __name__ == "__main__":
    game()

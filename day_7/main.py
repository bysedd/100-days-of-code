import random

from hangman_art import logo, stages
from hangman_words import word_list

word_list = word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(logo)

print(f'Pssst, the solution is {chosen_word}.')

display = ["_" for word in chosen_word]
guessed_words = []

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # Validate the guess
    if guess.isnumeric():
        print("You can't guess numbers.")
    elif len(guess) == 0:
        print("You didn't guess anything.")
    elif len(guess) > 1:
        print("You can only guess one letter at a time.")
    elif guess in guessed_words:
        print(f"You've already guessed the letter {guess}.")
    elif guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])
    guessed_words.append(guess)

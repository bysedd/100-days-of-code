from string import ascii_lowercase

from art import logo
from colorama import Fore, Style

alphabet = [*ascii_lowercase]


def format_input(msg: str) -> str:
    return input(msg).strip().lower()


def caesar(*, plain_text: str, shift_number: int, caesar_direction: str) -> None:
    result_text = ""

    if caesar_direction not in ["encode", "decode"]:
        print("Invalid input")
        return

    shift_number = shift_number if caesar_direction == "encode" else -shift_number

    for letter in plain_text:
        if letter in alphabet:
            index = alphabet.index(letter)
            result_text += alphabet[(index + shift_number) % len(alphabet)]
        else:
            result_text += letter

    print(f"Here's the {caesar_direction}d text: {Fore.GREEN}{result_text}{Style.RESET_ALL}")


print(logo)
while True:
    try:
        restart = ""
        direction = format_input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
        text = format_input("Type your message: ")
        shift = int(input("Type the shift number: "))

        caesar(plain_text=text, shift_number=shift, caesar_direction=direction)

        while restart not in ["yes", "no"]:
            restart = format_input("Type 'yes' if you want to go again. Otherwise type 'no': ")
        if restart == "no":
            break
        print()
    except ValueError:
        print("Invalid input")
    except KeyboardInterrupt:
        break

print("\nGoodbye")

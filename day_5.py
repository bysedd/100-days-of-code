# Password Generator Project
import random
from string import ascii_letters, digits

letters = [*ascii_letters]
numbers = [*digits]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
easy_pass = ""

easy_pass += "".join(random.choices(letters, k=nr_letters))
easy_pass += "".join(random.choices(symbols, k=nr_symbols))
easy_pass += "".join(random.choices(numbers, k=nr_numbers))

print(f"Here is your password: {easy_pass}")

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
hard_pass = ""

hard_pass += "".join(random.sample(letters, k=nr_letters))
hard_pass += "".join(random.sample(symbols, k=nr_symbols))
hard_pass += "".join(random.sample(numbers, k=nr_numbers))

# shuffle the password
hard_pass = "".join(random.sample(hard_pass, len(hard_pass)))

print(f"Here is your password: {hard_pass}")

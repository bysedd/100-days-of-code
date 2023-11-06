from random import randint

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# Write your code below this line 👇
user_choice = int(
    input("What do you choose? 0 for Rock, 1 for Paper, 2 for Scissors.\n")
)
computer_choice = randint(0, 2)
moves = ["Rock", "Paper", "Scissors"]

user_move = moves[user_choice]
computer_move = moves[computer_choice]

result_matrix = {
    "Rock": {"Rock": "It's a draw.", "Paper": "You lose.", "Scissors": "You win."},
    "Paper": {"Rock": "You win.", "Paper": "It's a draw.", "Scissors": "You lose."},
    "Scissors": {"Rock": "You lose.", "Paper": "You win.", "Scissors": "It's a draw."},
}

result_message = result_matrix[user_move][computer_move]

print(f"\nYou chose:\n{eval(user_move.lower())}")
print(f"Computer chose:\n{eval(computer_move.lower())}")
print(result_message)

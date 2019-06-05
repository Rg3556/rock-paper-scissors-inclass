# game.py

import random  

print("Rock, Paper, Scissors, Shoot!")


# Capture inputs

user_choice = input("Please choose one of the following options: 'rock', 'paper', or 'scissors' (without the quotes): ")

print("-------------------------------")
print("USER CHOICE: ", user_choice)


# Validate inputs

options = ["rock", "paper", "scissors"]
if user_choice not in options:
    print("INVALID SELECTION, PLEASE TRY AGAIN...")
    exit()


# Generate computer selection

computer_choice = random.choice(options)
print("-------------------------------")
print("GENERATING...")
print("COMPUTER CHOICE: ", computer_choice)

# Determine the winner

# Display final outputs / outcomes

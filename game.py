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

# rock beats scissors
# paper beats rock
# scissors beats paper
# Same selections is a tie

# Plan before starting coding
if user_choice == computer_choice:
    print("TIE")
elif user_choice == "rock" and computer_choice == "paper":
    print("PAPER")
elif user_choice == "rock" and computer_choice == "scissors":
    print("ROCK")        

elif user_choice == "paper" and computer_choice == "rock":
    print("PAPER")
elif user_choice == "paper" and computer_choice == "scissors":
    print("SCISSORS")

elif user_choice == "scissors" and computer_choice == "paper":
    print("SCISSORS")
elif user_choice == "scissors" and computer_choice == "rock":
    print("ROCK")        


# Display final outputs / outcomes

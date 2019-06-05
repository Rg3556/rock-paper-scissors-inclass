# game.py

print("Rock, Paper, Scissors, Shoot!")


# Capture inputs

user_choice = input("Please choose one of the following options: 'rock', 'paper', or 'scissors' (without the quotes): ")

print("-------------------------------")
print("USER CHOICE: ", user_choice)


# Validate inputs

if user_choice in ["rock", "paper", "scissors"]:
    print("VALID")
else:
    print("INVALID SELECTION, PLEASE TRY AGAIN...")
    exit()


# Generate computer selection


print("GENERATING...")

# Determine the winner

# Display final outputs / outcomes

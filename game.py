# game.py

import random  


def determine_winner(user_choice, computer_choice):
        winners = {
        "rock":{
            "rock": None,
            "paper": "paper",
            "scissors": "rock",
        },
        "paper":{
            "rock": "paper",
            "paper": None,
            "scissors": "scissors",
        },
        "scissors":{
            "rock": "rock",
            "paper": "scissors",
            "scissors": None,
        },
    }

if __name__ == "__main__":
    


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
    # if user_choice == computer_choice:
    #     print("TIE")
    # elif user_choice == "rock" and computer_choice == "paper":
    #     print("PAPER")
    # elif user_choice == "rock" and computer_choice == "scissors":
    #     print("ROCK")        
    # 
    # elif user_choice == "paper" and computer_choice == "rock":
    #     print("PAPER")
    # elif user_choice == "paper" and computer_choice == "scissors":
    #     print("SCISSORS")
    # 
    # elif user_choice == "scissors" and computer_choice == "paper":
    #     print("SCISSORS")
    # elif user_choice == "scissors" and computer_choice == "rock":
    #     print("ROCK")        


    # first attribute represents the user, second represents the computer
    winners = {
        "rock":{
            "rock": None,
            "paper": "paper",
            "scissors": "rock",
        },
        "paper":{
            "rock": "paper",
            "paper": None,
            "scissors": "scissors",
        },
        "scissors":{
            "rock": "rock",
            "paper": "scissors",
            "scissors": None,
        },
    }

    winning_choice = winners[user_choice][computer_choice]


    if winning_choice:
        if winning_choice == user_choice:
            print("YOU WON")
        elif winning_choice == computer_choice:
            print("YOU LOST")
        else:
            print("TIE")


    # winning_choice = winners[user_choice][computer_choice]



    # Display final outputs / outcomes

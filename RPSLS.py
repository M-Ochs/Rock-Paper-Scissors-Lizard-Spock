import random

#function to get input from the player
def get_player_choice():
    #displays the valid choices for Rock, Paper, Scissors, Lizard, Spock
    print("Choose: Rock, Paper, Scissors, Lizard, or Spock")
    #while loop to ensure continuous input until a valid choice is entered
    while True:
       #applies strip() to remove leading and tailing whitespace from the player's input
       #applies capitalize() to capitalize the first letter of the player's input
       #ensures a cleaned and standardized player input
       player = input("Your choice: ").strip().capitalize()
       #if player's choice matches any item in the list, returns the choice
       if player in ["Rock", "Paper", "Scissors", "Lizard", "Spock"]:
          return player
       #displays an error message and prompts the player to enter a valid choice
       #if player's choice doesn't match any item in the list
       else:
        print("Invalid choice. Please enter Rock, Paper, Scissors, Lizard, or Spock.")

#Generate a random choice for the computer from a list
def get_computer_choice():
    choices = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
    # returns the randomly chosen option as the computer's choice
    return random.choice(choices)

#Determine the winner of the game
def winner(player, computer_choice):
    #compares the player's choice with the computer's choice
    if player == computer_choice:
        return "It's a tie!"
     
    #defines two dictionaries for winning and loosing statements
    winning_statements = {
        "Rock-Scissors": "Rock crushes Scissors. You win!",
        "Paper-Rock": "Paper covers Rock. You win!",
        "Scissors-Paper": "Scissors cuts Paper. You win!",
        "Lizard-Paper": "Lizard eats Paper. You win!",
        "Spock-Rock": "Spock vaporizes Rock. You win!",
        "Scissors-Lizard": "Scissors decapitates Lizard. You win!",
        "Lizard-Spock": "Lizard poisons Spock. You win!",
        "Spock-Scissors": "Spock smashes Scissors. You win!",
        "Paper-Spock": "Paper disproves Spock. You win!",
        "Rock-Lizard": "Rock crushes Lizard. You win!",
    }

    losing_statements = {
        "Rock-Paper": "Paper covers Rock. You lose!",
        "Paper-Scissors": "Scissors cuts Paper. You lose!",
        "Scissors-Rock": "Rock crushes Scissors. You lose!",
        "Lizard-Scissors": "Scissors decapitates Lizard. You lose!",
        "Spock-Lizard": "Lizard poisons Spock. You lose!",
        "Scissors-Lizard": "Lizard eats Paper. You lose!",
        "Lizard-Rock": "Rock crushes Lizard. You lose!",
        "Spock-Scissors": "Spock smashes Scissors. You lose!",
        "Paper-Spock": "Paper covers Rock. You lose!",
        "Rock-Spock": "Spock vaporizes Rock. You lose!",
    }
    #concatenates the player's and computer's choice
    combined_choices = f"{player}-{computer_choice}"
    
    #checks if the combined choice is a winning or losing combination to determine the result
    if combined_choices in winning_statements:
        return winning_statements[combined_choices]
    elif combined_choices in losing_statements:
        return losing_statements[combined_choices]
    else:
        return "Invalid combination. It's a tie!"

#function to play several rounds of the game
def ask_for_another_round():
    response = input("Do you want to play another round? y/n: ").strip().lower()
    return response == "y"

#loop to play the game
def play_game():
    while True:
     #gets player and computer choice
     player = get_player_choice()
     computer_choice = get_computer_choice()

    #prints choice
     print(f"You chose: {player}")
     print(f"Computer chose: {computer_choice}")
    #determines and prints the winner
     result = winner(player, computer_choice)
     print(result)

    #asks if the player wants to play another round
    #or ends loop
     if not ask_for_another_round():
         print("Thanks for playing!")
         break

play_game()
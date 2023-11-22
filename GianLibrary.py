# Gianmarco Roldan
# April 2nd, 2023
# This file displays a in-depth algorithim that plans the functions to run
# concerning menu choice interactions, generating treasure, determining a gain
# or lose point system, displaying the user's score, and recording the user's
# score if they can land on the score board.

# 8, 10, 12, 13, 14

import DiaLibrary
from JadeLibrary import DisplayMenu, MenuChoice, DisplayIntro, DisplayOutro, GetName
import GianLibrary


# 8)

# Return Type: 1 string, MenuChoice
# Parameters: none
# Purpose: Allows for user to choose a selection from the menu ranging from 1-3 options

# Define MenuChoice function
def MenuChoice(userChoice):
    # Display the first room layout, with a menu to interact with 1) Treasure, 2)Enemy, 3) Exit
    print("Loading menu . . .\n")
    print("1) Treasure")
    print("2) Enemy")
    print("3) Exit\n")
    userChoice = int(input("Please enter your option here: \n"))
    # Create a nested selection structure that allows for interactive results
    # use if, elif, and else statements
    # store choice that user has made
    if userChoice == 1:
        print("As you pick up the scroll, a message appears...")
        print("Between two doors, what you are looking for will appear.")
    elif userChoice == 2:
        print("Throughout this journey many obstacles will be thrown your way, will you be able to overcome them?")
    elif userChoice == 3:
        return userChoice
    else:
        print("Error . . .Please enter a number 1-3")


# 10)
# Return Type: 1 string MenuOption, 1 string TreasureChoice
# Parameters: None
# Purpose: Allows for the game to let the user have selections on how to get to the treasure/recieve points

# define TreasureChoice function
def TreasureChoice(doorChoice, chances):
    # If user chooses treasure, continue onto a next variety of selections
    # Display a menu that gives the
    # user to choose between a set of doors, one on the right and another on the left
    # Using a selection structure, allow for each choice to have a consequence.
    # Prompt user for their response, validate it
    # If the user chooses the door on the right, they choose the right option!
    # Print a statement to ensure they are aware that they found the treasure
    # If the user chooses the door on the left, they came across a trap where they have to step carefully
    # Generate random chance that they survive
    # If they survive, print a statement that they overcame the obstacle and managed to get to the treasure
    # Else, print an error statement and to choose through the options of numbers
    items = ['potions', 'gold coins', 'new weapons']
    potions = potions
    goldCoins = goldCoins
    newWeapons = newWeapons
    treasure = print(random.choice(items))
    if treasure == potions:
        print("Congratulations {name}, you have recieved valuable potions!")
        print("This can be of use in combat, health, or abilities.")
    elif treasure == goldCoins:
        print("Congratulations {name}, you have recieved valuable currency!")
        print("This will allow for you to buy items to help you moving foward")
    elif treasure == newWeapons:
        print("Congratulations {name}, you have recieved new weapons!")
        print("This will allow you to protect yourself from enemies.")
    else:
        print("The treasure has already been found!")


# 12)
# Return Type: 1 string victory or loss
# Parameters: 1 string for user's outcome
# Purpose: This function allows for a user to either gain or lose a point

# define PointSystem function
def PointSystem(points, playerScore, playerHealth):
    # Determine if the user defeated an enemy, if so they gain a point
    # If correct return their victory
    # If they lose, they are not correct, they suffered a lose
    # If they suffered a lose, they lose a point
    playerScore = 0
    playerHealth = 100
    points = 0
    if playerHealth > 0:
        random.randint(10, 20) and + playerScore
        print("You have gained one point !")
    else:
        random.randint(10, 20) and - playerScore
        print("You have lost one point !")


# 13)
# Return Type: None
# Parameters: 1 string user's score
# Purpose: This function displays the user's score

# Define usersScore
def usersScore():
    # string user's score and allow it to be saved as an input
    userScore = 0
    # Once rounds of the game have finished display the user's score
    print("*" * 40)
    print(userScore)
    print("*" * 40)


# 14)
# Return Type: 1 string user's score, 1 string highscore
# Parameters: None
# Purpose: This function records the user's score and ensures to see if it is possible to be recorded on the score board

# Define ScoreBoard
def ScoreBoard():
    # Use operators and determine if the user's score is high enough to be on the score boardAQ
    # If true, then the score can contine on and be displayed
    # Display a statement congratulating the user
    # If false, then display a statment asking the user to try again
    print("Loading Score Board . . .\n")
    print("*" * 40)
    text_file = open("highscores.txt", "r")
    with open('highscores.txt', 'r')
        contents = file.readlines()

    for i in range(len(contents)):
        contents[i] = contents[i].strip
    print(contents)
    whole_thing = text_file.read()
    print(whole_thing)
    text_file.close()
    if userScore > highScore:
        print(userScore)
        print("Congratulations {name} !, you have made it onto the offical Score Board.")
        print("*" * 40)





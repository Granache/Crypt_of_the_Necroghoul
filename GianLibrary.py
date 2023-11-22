# Gianmarco Roldan
# April 2nd, 2023
# This file displays a in-depth algorithim that plans the functions to run
# concerning menu choice interactions, generating treasure, determining a gain
# or lose point system, displaying the user's score, and recording the user's
# score if they can land on the score board.

# 8, 10, 12, 13, 14

import DiaLibrary
from JadeLibrary import DisplayMenu, MenuChoice, DisplayIntro, DisplayOutro, GetName


# 8)

# Return Type: 1 string, MenuChoice
# Parameters: none
# Purpose: Allows for user to choose a selection from the menu ranging from 1-3 options


# Define MenuChoice function
def MenuChoice(userChoice):
    # Display the first room layout, with a menu to interact with 1) Treasure, 2)Enemy, 3) Exit
    # Create a nested selection structure that allows for interactive results
    # use if, elif, and else statements
    # store choice that user has made
    pass


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
    pass


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
    pass


# 13)
# Return Type: None
# Parameters: 1 string user's score
# Purpose: This function displays the user's score

# Define usersScore
def usersScore():
    # string user's score and allow it to be saved as an input
    # Once rounds of the game have finished display the user's score
    pass


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
    pass




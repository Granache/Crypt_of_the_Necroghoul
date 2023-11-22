# Jade Ho
# Date
# Function 1-4, 16, and 17

from time import sleep


# 1)
# return type: none
# parameters: none
# Purpose: Display introduction
# Define DisplayIntro function
def DisplayIntro():
    # Display Intro
    print("↫↫↫↫↫ W͛E͛L͛C͛O͛M͛E͛ ͛T͛O͛ ↬↬↬↬↬".center(70))
    sleep(.3)
    print("C͛R͛Y͛P͛T͛ ͛O͛F͛ ͛T͛H͛E͛ ͛N͛E͛C͛R͛O͛-͛G͛H͛O͛U͛L͛".center(70))


# 2)
# return type: 1 str for player name
# parameters: non
# Purpose: prompt for user name
# Define PlayerName function
def GetName():
    # Declare and string variable
    pName = ''
    # Prompt for player name
    pName = input('Hi player, please create a user name: ').strip().capitalize()
    # Return player name
    return pName


# 3)
# return type: none
# parameters: none
# Purpose: Display menu of choice 1) Play, 2) Rules, 3) High Score board, 4) Quit
# Define menu function
def DisplayMenu():
    # Display menu 1) Play, 2) Rules, 3) High Score board, 4) Quit
    print("Let's get started!! \nFirst, please choose a option from the menu below.")
    print("1) Play \n2) Rules \n3) High Score board \n4) Quit")


# 4)Get Menu Choice for starting the game
# return type: 1 int for choice
# parameters:none
# Purpose: Get player for starting the game
# Define MenuChoice function
def MenuChoice():
    # Declare and initialize int variables for choice
    menuChoice = 0
    # Use while loop until get the valid number
    # Get player choice and validate it
    # Use if-else for number error
    # Use try-except for other unexpected error
    while menuChoice < 1 or menuChoice > 4:
        try:
            menuChoice = int(input('PLease enter your choice here: '))
            if menuChoice < 1 or menuChoice > 4:
                print('Please select a number fom 1 to 4 only!')
        except:
            print('Please type a whole numer!')

    # Return player choice
    if menuChoice == 1:
        return "play"
    elif menuChoice == 2:
        return "rules"
    elif menuChoice == 3:
        return "score"
    else:
        return "quit"


# 16
# return type:none
# parameters: n/a
# Purpose: Display high score board
# Define HighScore function
def HighScore():
    # Get record of high score from part #14
    # Display high score board
    print()


# 17
# return type: 1 str for player choice
# parameters: 1 str for choice
# Purpose: Prompt for player if they want to play again
# Define PlayAgain function
# Declare and initialize for player choice
# Prompt for player if they want to play again
# If yes, restart again from the menu choice by while loop
# Reset variables
# If no, display outro
# Else, display error
# Return PlayAgain choice
# DID IN MAIN FUNCTION

# 18
# return type: none
# parameters: none
# Purpose: Display Outro
# Define DiplayOutro function
def DisplayOutro():
    # Display outro
    print("↫↫↫↫↫ S͛E͛E͛ ͛Y͛O͛U͛ ͛S͛O͛O͛N͛ ↬↬↬↬↬".center(70))
    sleep(.3)
    print("C͛R͛Y͛P͛T͛ ͛O͛F͛ ͛T͛H͛E͛ ͛N͛E͛C͛R͛O͛-͛G͛H͛O͛U͛L͛".center(70))

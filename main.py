# Name
# Date
# title

import DiaLibrary
from JadeLibrary import DisplayMenu, MenuChoice, DisplayIntro, DisplayOutro, GetName
from time import sleep


# 1) Display introduction
# 2) Prompt user name
# 3) Display menu of choice 1) Play, 2) Rules, 3) High Score board, 4) Quit
# 4) Get Menu Choice for strating the menu
# 5) Display the menu choice for 2 charaters, display different statistics, and get user choice
# 6) Create and display enemy statistics
# 7) Display room layout with menu for interactions
# 8) Get Menu Choice for room interactions
# 9) Run combat encounters
# 10) Generate the treasure
# 11) Random number generation
# 12) Determine if user gain or loose points
# 13) Display user score
# 14) Record user score in high score board if high enough
# 15) Display rules
# 16) Display high score board
# 17) Prompt for player if they want to play again
# 18) Display outro
# 19) Run treasure searching interaction


# Define main function
def main():
    # Declare and initialize constants
    # Integer value for treasure
    # Statistics for the Necro-Ghoul
    gSTR = 3
    gEND = 2
    gDEX = 2
    gINT = 1
    gHP = 20
    # Declare and initialize variables
    # String variable for menuChoice, playerName
    menuChoice = playerName = playerClass = roomType = enemyName = again = ""
    # Integer variable for playerStatistics, playerHealth, enemyStatistics, enemyHealth, score
    pSTR = pEND = pDEX = pINT = pHP = 0
    eSTR = eEND = eDEX = eINT = eHP = 0
    playerScore = 0
    # Boolean value for treasureSearched and enemyFought
    treasureSearched = False
    enemyFought = False
    finished = False
    # Display the introduction
    while again != 'no':
        finished = False
        again = ""
        print()
        DisplayIntro()
        # Display menu of choice 1) Play, 2) Rules, 3) High Score board, 4) Quit
        # Get the user's choice and execute that section

        DisplayMenu()
        menuChoice = MenuChoice()

        # If the user selects play, play the game:
        if menuChoice == "play":
            # Prompt for userName
            print()
            playerName = GetName()
            # Display the menu choice for 2 charaters and their characteristics, get the player's
            # choice
            print()
            pSTR, pEND, pDEX, pINT, pHP, playerClass = DiaLibrary.ChooseCharacter(playerName)

            # Display first room layout, with a menu to interact with 1) Treasure, 2) Enemy, 3) Exit
            for i in range(2):
                repeat = False
                enemyFought = False
                treasureSearched = False
                if pHP > 0:

                    eSTR, eEND, eDEX, eINT, eHP, enemyName = DiaLibrary.GenerateEnemy()
                    roomType = DiaLibrary.DisplayRoom(playerClass, enemyName)
                    # Get the player's choice
                    menuChoice = ""
                    while menuChoice != "3":
                        if pHP <= 0:
                            sleep(1)
                            print("\nThis is the end of your adventure.")
                            menuChoice = "3"
                        elif pHP > 0:
                            if repeat == True:
                                print(f"\n1) Search for treasure\n2) Face the {enemyName}\n3) Run for the exit")

                            menuChoice = input("Enter your choice: ")
                            # If the player selects Treasure:
                            if menuChoice == "1" and treasureSearched == False:
                                # Describe some obstacle and display various options to get through it
                                # Get the player's choice, generate a random number to determine their success
                                # If successful, generate a random selection of treasure and add it to their score
                                # If unsuccessful, they gain no treasure and may take some damage
                                playerScore, pHP = DiaLibrary.HuntTreasure(roomType, playerScore, pINT, pDEX, pHP)
                                treasureSearched = True
                                repeat = True



                            elif menuChoice == "1" and treasureSearched == True:
                                print("\nThe treasure has already been found.")

                            # If the player selects Enemy:
                            elif menuChoice == "2" and enemyFought == False:
                                # Create and dislay enemy statistics
                                # Begin the combat encounter
                                # If the player defeats the enemy, generate a random selection of treasure
                                # and add the values to the player's score
                                # If the enemy defeats the player, end the game
                                pHP, playerScore = DiaLibrary.RunCombat(pHP, pSTR, pEND, pDEX, pINT, eHP, eSTR, eEND,
                                                                        eDEX, eINT, playerScore, enemyName)
                                enemyFought = True
                                repeat = True


                            elif menuChoice == "2" and enemyFought == True:
                                print("\nThe enemy has already been defeated.")

                            # If the player selects Exit:
                            elif menuChoice == "3":
                                # Move on to the next room
                                print("\nTo the next room...")

                            else:
                                print('\nYou must enter "1", "2", or "3". Try again.')

                # Repeat the steps for room layout and interactions a second time
            # For the third and final room, display the room layout and the final boss
            if pHP > 0:
                print(
                    "\nStanding in the center of a great antechamber is the fearsome Necro-Ghoul! It bears its fangs and readies its claws. There is no turning back now, prepare to fight!")
                sleep(4)

                # Begin combat with the final boss
                # If the player defeats the final boss, generate a large random selection of treasure
                # and add the values to the player's score
                # If the final boss defeats the player, end the game
                pHP, playerScore = DiaLibrary.RunCombat(pHP, pSTR, pEND, pDEX, pINT, gHP, gSTR, gEND, gDEX, gINT,
                                                        playerScore, "Necro-Ghoul")
            # Display user score
            print(playerScore)

            finished = True

        if menuChoice == "rules":
            DiaLibrary.DisplayRules()
        # If the user selects High Score Board, display the current high score board
        # If the user selects Quit, Display Outro
        if menuChoice == "quit":
            print("\nQuitting...")
            finished = True

        while again != "yes" and again != "no" and finished == True:
            again = input('\nDo you want to play one more time, YES or NO? ').lower()
            if again == "yes":
                print("\nRebooting the game, please wait one second")
                sleep(1)

            elif again == "no":
                sleep(.5)
                print()
                DisplayOutro()

            else:
                print('\nPlease enter "YES" or "NO". Try again.')


main()

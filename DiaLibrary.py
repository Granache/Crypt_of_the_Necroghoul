#Dia Fallon
#4/2/2023
#This is a library file containing several functions related to rules
#and systems for "The Crypt of the Necro-Ghoul"

#Import random number generator
from random import randint\
#Import sleep
from time import sleep

#Return Type: 1 string for user's character choice, 5 integers for character's Health,
#   Strength, Endurance, Dexterity, and Intelligence
#Parameters: 1 string for user's name
#Purpose: Display the menu choice for 2 charaters, display different statistics,
#   and get user choice
#Define Character Choice
def ChooseCharacter(userName):
    #Declare and initialize constants
    #Whole numbers for Fighter's Strength, Endurance, Dexterity, Intelligence,
    #   and Health
    FSTRENGTH = 3
    FENDURANCE = 3
    FDEX = 2
    FINT = 1
    FHEALTH = 30
    
    #Whole numbers for Thief's Strength, Endurance, Dexterity, Intelligence,
    #   and Health
    TSTRENGTH = 1
    TENDURANCE = 2
    TDEX = 3
    TINT = 3
    THEALTH = 20
    
    #Declare and initialize int variable for menu choice
    menChoice1 = menChoice2 = 0
    #Boolean value for repeat
    repeat = False
    #Display menu choice for the player to view the statistics of the
    #   two characters, the Fighter and the Thief
    print(f"Now then, {userName}, what will you be?\n1) Fighter\n2) Thief")
    while menChoice1 != "1" and menChoice1 != "2":
        if repeat == True:
            print(f"Now then, {userName}, what will you be?\n1) Fighter\n2) Thief")
            repeat = False
            menChoice2 = 0
            
        menChoice1 = input("\nMake your choice, 1 or 2: ")
    
        #If the player selects the Fighter:
        if menChoice1 == "1":
            #Display the Fighter's statistics and a brief description of the playstyle
            print(f"The Fighter is designed to fight monsters, having +{FSTRENGTH} to"
            f" strength rolls, +{FENDURANCE} to endurance, and {FHEALTH} health points."
            f" However, the Fighter only has +{FDEX} to dexterity and +{FINT} to intelligence.")
            
            #Prompt the user to confirm if they want this character or if they want to view the other
            while menChoice2 != "1" and menChoice2 != "2":
                print("\nIs this the character you wish to play?\n1) Yes\n2) No, return to menu")
                menChoice2 = input("\nMake your choice: ")
                if menChoice2 == "1":
                #If they confirm that they wish to play this character:
                    #Return Fighter's Strength, Endurance, Dexterity, Intelligence, and Health,
                    #and a string that says "Fighter"
                    return FSTRENGTH, FENDURANCE, FDEX, FINT, FHEALTH, "Fighter"
                #If they wish to return, return to the menu
                elif menChoice2 == "2":
                    menChoice1 = 0
                    repeat = True
                else:
                    print("\nYou must choose 1 or 2 only. Try again.")
        #If the player selects the Thief:
        elif menChoice1 == "2":
            #Display the Thief's statistics and a brief description of the playstyle
            print(f"The Thief is designed to solve obstacles and use tricks, having +{TDEX} to"
            f" dexterity rolls and +{TINT} to intelligence. However, the Thief only has +{TSTRENGTH} to strength,"
            f" +{TENDURANCE} to endurance, and {THEALTH} health points.")
            
            #Prompt the user to confirm if they want this character or if they want to view the other
            while menChoice2 != "1" and menChoice2 != "2":
                print("Is this the character you wish to play?\n1) Yes\n2) No, return to menu")
                menChoice2 = input("\nMake your choice: ")
                if menChoice2 == "1":
            #If they confirm that they wish to play this character:
                #Return Thief's Strength, Endurance, Dexterity, Intelligence, and Health,
                #and a string that says "Thief"
                    return TSTRENGTH, TENDURANCE, TDEX, TINT, THEALTH, "Thief"
            #If they wish to return, return to the menu
                elif menChoice2 == "2":
                    menChoice1 = 0
                    repeat = True
                else:
                    print("\nYou must choose 1 or 2 only. Try again.")
        #Verify the user's inputs
        else:
            print("\nYou must choose 1 or 2 only. Try again.")


#Return Type: 1 string for enemy's name, 5 integers for enemy's Health, Strength,
    #Endurance, Dexterity, and Intelligence
#Parameters: n/a
#Purpose: Create and display enemy statistics
#Define EnemyGeneration
def GenerateEnemy():
    #Declare and initialize constants
    #Whole numbers for Zombie's Strength, Endurance, Dexterity, Intelligence,
    #   and Health
    ZSTR = 2
    ZEND = 2
    ZDEX = 1
    ZINT = 0
    ZHP = 13

    #Whole numbers for Skeleton's Strength, Endurance, Dexterity, Intelligence,
    #   and Health
    SSTR = 1
    SEND = 0
    SDEX = 2
    SINT = 2
    SHP = 15
    
    #Whole numbers for Carrion Crawler's Strength, Endurance, Dexterity, Intelligence,
    #   and Health
    CSTR = 3
    CEND = 3
    CDEX = 0
    CINT = 0
    CHP = 20
    
    #Declare and initialize whole number variable for random number
    randNum = 0

    #Generate a random number from 1 to 3 with no modifier
    randNum = GenerateNumber(1, 3, 0)
    
    #If that random number is a 1:
    if randNum == 1:
        #Return Zombie's Strength, Endurance, Dexterity, Intelligence,
        #and Health, and a string that reads "Zombie"
        return ZSTR, ZEND, ZDEX, ZINT, ZHP, "Zombie"
    
    #If that random number is a 2:
    if randNum == 2:
        #Return Skeleton's Strength, Endurance, Dexterity, Intelligence,
        #and Health, and a string that reads "Skeleton"
        return SSTR, SEND, SDEX, SINT, SHP, "Skeleton"
    
    #If that random number is a 3:
    if randNum ==3:
        #Return Carrion Crawler's Strength, Endurance, Dexterity, Intelligence,
        #and Health, and a string that reads "Carrion Crawler"
        return CSTR, CEND, CDEX, CINT, CHP, "Carrion Crawler"


#Return Type: 1 string for room type
#Parameters: 1 string for user's character choice, 1 string for enemy's name
#Purpose: Display room layout with menu for interactions
#Define DisplayRoom
def DisplayRoom(characterChoice, enemyType):
    #Declare and initialize whole number variable for random number
    randNum = 0
    #String variable for room type
    roomType = ""

    #Generate a random number for 1 to 3 with no modifier
    randNum = GenerateNumber(1,3,0)

    #If that number is a 1:
    if randNum == 1:
        #Display the description of a circular room with a pit of sand in the center,
        #a shadowy figure, a (enemy's name), scratches around in the sand pit,
        #several ceramic jars line the walls, laden with loot
        print(f"\nYou enter a circular room with a pit of sand in the center. A shadowy {enemyType} scratches around in the pit.")
        print("Several tall and heavy ceramic jars line the walls, laden with loot. It would be a struggle to pull them down.")

        #Set room type to "sandRoom"
        roomType = "sandRoom"
        
    #If that number is a 2:
    elif randNum == 2:
        #Display the description of a spacious library, with a (enemy's name) reading the
        #books. Several crates of books, and perhaps treasures, are organized alphabetically
        print(f"\nYou enter a spacious library with various crates of books littered around. A {enemyType} wanders the aisles.")
        print("Some of the crates seem to have sorted treasures within. You wonder if you can find the \"Gold\" section.")

        #Set room type to "library"
        roomType = "libraryRoom"
        
    #If that number is a 3:
    elif randNum == 3:
        #Display the description of a marble mausoleum, a (enemy's name) rises from a coffin,
        #and two stone doors lie on one side
        print(f"\nYou enter a marble masoleum, various urns lie among countless depressions in the wall. A {enemyType} rises from a stone coffin.")
        print("To your right, two stone doors seem to lead to two different side rooms. Strange pictograms are engraved on each.")
        
        #Set room type to "marble"
        roomType = "marbleRoom"
    
    #Display a menu with three options: 1) Search for treasure, 2) Face the (enemy's name)
    #3) Run for the exit
    sleep(2)
    print(f"\nBrave {characterChoice}, what do you wish to do?\n1) Search for treasure\n2) Face the {enemyType}\n3) Run for the exit")
    return roomType


#Return Type: 1 integer for treasure received
#Parameters: 1 string for room type, 4 integers for player score, intelligence, dexterity, and Health
#Purpose: Run a treasure hunting interaction where the player can overcome an obstacle for
#   Treasure
#Define HuntTreasure
def HuntTreasure(roomType, playerScore, pInt, pDex, pHP):
    #Initialize "HuntSuccess" to "False"
    HuntSuccess = False
    #String for menu choice
    menuChoice = ""
    #Whole number for damage
    damage = treasure = 0
    #If room type is the "sandRoom":
    if roomType == "sandRoom":
        #Display a description of the heavy ceramic jars
        print("\nThe ceramic jars are too heavy to lower down, but just knocking them over would destroy the treasure within.")
        print("You wonder if, with a bit of clever thinking, you can make something work...")

        sleep(5)
        
        #Generate a random number from 1 to 10 with the character's intelligence added to the result        
        #If the generated number is greater than 5:
        if GenerateNumber(1, 10, pInt) > 5:
            #Display a description of the character lowering the jars to the ground
            #and grabbing the treasure within
            print("\nBy attaching a pulley system to the wall, you're able to lower one jar after the other.")
            print("You find a copious amount of gold and gems within!")
            #Set "HuntSuccess" to "True"
            HuntSuccess = True

        #If the generated number is less than 5:
        else:
            #Display a description of the character dropping the jars, smashing the treasure
            print("\nYou fumble with one of the jars and it crashes down on the next in line. Like a row of dominoes, they all fall.")
            print("Amidst the rubble you find shattered gems and bent coins. Maybe the scrapyard might take it...")
            
    #If the room type is the "library":
    elif roomType == "libraryRoom":
        #Display a description of the crates, ordered in the Dewey Decimal System
        print("\nThe crates seem to be ordered in some obscure decimal system, with each number corresponding to the type of items within.")
        print("You scratch your chin and wonder if you can understand this system...")

        sleep(5)
        
        #Generate a random number from 1 to 10 with the character's intelligence added to the result
        #If the generated number is greater than 5:
        if GenerateNumber(1, 10, pInt) > 5:
            #Display a description of the character finding the crates labeled "treasure"
            print("\nEureka! You run down the aisles and find the geology section.")
            print("The crates here are filled with gold, silver, and platinum!")
            #Set "HuntSuccess" to "True"
            HuntSuccess = True
            
        #If the generated number is less than 5:
        else:
            #Describe the character getting lost and finding the crates labeled "trash"
            print("\nYou think you know where to go, but end up getting lost. You find yourself back where you began.")
            print("You open up a crate and find an assorted set of rusted spoons.")
            
    #If the room type is the "marble" room:
    elif roomType == "marbleRoom":
        #Display a menu that gives the user to choose between a set of doors, one on the right and another on the left
        print("\nYou see two doors along the corridor, one to your right and one to your left, each one inscribed with strange symbols.")
        if GenerateNumber(1, 10, pInt) > 5:
            print("Studying the symbols, you realize that the door on the left is inscribed with the magic symbol for \"Fire\","
                  " while the door on the right is inscribed with the symbol for \"Water\".")

        sleep(4)
        
        while menuChoice != "1" and menuChoice != "2":
            print("\nWhich door will you choose?\n1) Enter the Right Door\n2) Enter the Left Door")
            menuChoice = input("\nEnter your choice: ")
            if menuChoice != "1" and menuChoice != "2":
                print('\nYou must enter "1" or "2". Try again.')
        
        #Using a selection structure, allow for each choice to have a consequence.
        #Prompt user for their response, validate it
        #If the user chooses the door on the right, they choose the right option!
        if menuChoice == "1":
            #Print a statement to ensure they are aware that they found the treasure
            print("\nYou enter the Right Door.\nTaking your first step into the dark room, your heart falls as you do, too. You stumble and land into a pool of water!"
                  "\nThe water is only a few inches deep, and yet something metallic shifts around within. You grope around, and find piles of gold!")
            
            #Set "HuntSuccess" to "True"
            HuntSuccess = True
        
        #If the user chooses the door on the left, they came across a trap where they have to step carefully
        if menuChoice == "2":
            print("\nYou step through the Left Door.\nOut of the darkness, you are suddenly greated by a bright light and a terrible heat!")

            sleep(1.5)
            
            #Generate a random number from 1 to 10 with the character's dexterity added to the result
            if GenerateNumber(1, 10, pDex) < 5:
            #If the result is less than 5:
                #Generate a random number from 1 to 10 and subtract the result for the player's health
                damage = GenerateNumber(1, 10, 0)
                pHP -= damage
                print(f"Flames errupt from the ground, you have stepped into a trap! You stumble through the flames and take {damage} damage!")
                #If the player's health is at or below 0, break
                if pHP <= 0:
                    print("\nThe flames consume you as you hear the distant laugh of the Necro-Ghoul. Your ashes will find a new home among this marble masoleum.")
                    return playerScore, pHP
            else:
                print("Flames errupt from the ground and you reflexively jump into the air. You grab onto a well-placed ledge and hang there."
                      " The heat is unbearable, but you avoid the worst of the flames.")
            #If they survive, print a statement that they overcame the obstacle and managed to get to the treasure
            print("\nEventually, the flames recede. Although your clothes are singed, you are happy to see piles of treasure along the ground. They are hot to the touch.")
                #Set "HuntSuccess" to "True"
            HuntSuccess = True
        #Else, print an error statement and to choose through the options of numbers
    #If "HuntSuccess" is set to "True":
    if HuntSuccess == True:
        #Generate treasure, add that value to the player's score, and return the new score
        treasure = GenerateNumber(10, 20, 0)
        playerScore += treasure
        print(f"You gain {treasure} points!")
        return playerScore, pHP

    #If "HuntSuccess" is set to "False":
    elif HuntSuccess == False:
        #Generate treasure, divide it by 4 and round down
        treasure = GenerateNumber(10, 20, 0)
        playerScore += round(treasure / 4)
        print(f"You gain {round(treasure / 4)} points.")
        #Add that value to the player's score and return the new score
        return playerScore, pHP



#Return Type: 1 integer for player health and 1 integer for treasure received
#Parameters: 4 integers for player Health, Strength, Endurance, Dexterity, and Intelligence;
    #4 integers for enemy Health, Strength, Endurance, Dexterity, and Intelligence;
    #1 integer for player score, and 1 string for enemy name
#Purpose: Run combat encounters, where the player and enemy will take turns attacking the other
#Once one of their Health values reach or go below 0, the encounter will end
#Define RunCombat
#NOTE: For room 1 and 2, a random enemy will be loaded into the combat encounter. For the
#   final room, it will always be the Necro-Ghoul
def RunCombat(pHP, pSTR, pEND, pDEX, pINT, eHP, eSTR, eEND, eDEX, eINT, pSCORE, eNAME):
    #initialize integer variable for random value, counter
    randomNum = treasure = 0
    count = 1
    #String for player choice
    pChoice = ""
    
    #While the player's Health or the enemy's Health is not equal to or below 0:
    while pHP > 0 and eHP > 0:
        print(f"\nROUND {count}\t\tPLAYER HEALTH: {pHP}\t{eNAME.upper()} HEALTH: {eHP}")
        print()
        print("*"*60)

        sleep(1)
        
        #Display a menu with two options, 1) Attack, 2) Maneuver
        print("\nNow is your chance to strike. What do you do?\n1) Attack\n2) Maneuver")
        pChoice = ""

        #Get the user's input for 1 or 2
        while pChoice != "1" and pChoice != "2":

            pChoice = input("\nEnter your choice: ")

            sleep(1)

            #If the user selects 1:
            if pChoice == "1":
                
                #Generate a random number from 1 to 10 with the player's Dexterity added to the result
                randomNum = GenerateNumber(1, 10, pDEX)

                #If the result is greater than 5:
                if randomNum > 5:
                    #Describe the player landing a blow on the (enemy name)
                    print(f"\nYou slice at the {eNAME}!")

                    #Generate a random number from 1 to 10 with the player's Strength added to the result
                    randomNum = GenerateNumber(1, 10, pSTR)
                    sleep(1)
                    print(f"\nYou deal {randomNum} damage!")
                    if randomNum == 10 + pSTR:
                        print("A critical hit! Maximum damage!")

                    #Subtract the result from the enemy's Health
                    eHP -= randomNum

                #Else:
                else:
                    #Describe the player missing the (enemy name)
                    print(f"\nYou swing, but miss the {eNAME}!")
                    
            #If the user selects 2:
            elif pChoice == "2":
                
                #Generate a random number from 1 to 10 with the enemy's Endurance added to the result
                randomNum = GenerateNumber(1, 10, eEND)
                
                #If the result is less than (5 + the player's Intelligence):
                if randomNum < (5 + pINT):
                    
                    #Describe the successful maneuver
                    print(f"\nYou flank the {eNAME} and strike!")
                    
                    #Generate a random number from 1 to 10 with the player's Dexterity added to the result
                    randomNum = GenerateNumber(1, 10, pDEX)
                    sleep(1)
                    print(f"\nYou deal {randomNum} damage!")

                    if randomNum == 10 + pDEX:
                        print("A critical hit! Maximum damage!")
                    #Subtract the result from the enemy's Health
                    eHP -= randomNum
                    
                #Else:
                else:
                    #Describe the enemy out smarting the player's maneuver
                    print(f"\nThe {eNAME} spots your maneuver and dodges!")
            else:
                print('\nYou must enter a "1" or "2", please try again')

        if eHP > 0:
            sleep(1)
            print(f"\nIt is now the {eNAME}'s turn!")
            #Generate a random number from 1 to 3
            randomNum = GenerateNumber(1, 3, 0)
            sleep(1)

            #If the number is 1-2, the enemy attacks:
            if randomNum == 1 or randomNum == 2:
                print(f"\nThe {eNAME} goes to attack!")

                #Generate a random number from 1 to 10 with the enemy's dexterity added to the result
                randomNum = GenerateNumber(1, 10, eDEX)

                sleep(1)

                #If the result is greater than 7:
                if randomNum > 7:
                    #Describe the (enemy name) striking the player
                    print(f"\nThe {eNAME} hits!")

                    #Generate a random number from 1 to 10 with the enemy's Strength added to the result
                    randomNum = GenerateNumber(1, 10, eSTR)

                    #Subtract the result from the player's health
                    sleep(1)
                    print(f"\nYou take {randomNum} damage!")
                    pHP -= randomNum
                    
                    #If the player's health is at or below 0, break
                    if pHP <= 0:
                        print(f"\nThe {eNAME} laughs as you draw your final breath. This foul crypt will be your resting place.")
                        return [pHP, pSCORE]
                #If the result is less than 7:
                elif randomNum <= 7:
                    #Describe the (enemy name) missing the player
                    print(f"\nThe {eNAME} misses its attack!")
            #If the number is a 3, the enemy performs a maneuver:
            elif randomNum == 3:
                print(f"\nThe {eNAME} tries to flank you!")
                sleep(1)
                #Generate a random number from 1 to 10 with the player's Endurance added to the result
                randomNum = GenerateNumber(1, 10, pEND)
                #If the result is less than (5 + the enemy's intelligence):
                if randomNum < (5 + eINT):
                    #Describe the successful maneuver
                    print(f"\nThe {eNAME} circles you and slashes you on the back!")
                    
                    #Generate a random number from 1 to 10 with the enemy's Dexterity added to the result
                    randomNum = GenerateNumber(1, 10, pDEX)
                    #Subtract the result from the player's Health
                    sleep(1)
                    print(f"\nYou take {randomNum} damage!")
                    pHP -= randomNum
                    
                    #If the player's health is at or below 0, break
                    if pHP <= 0:
                        print(f"\nThe {eNAME} laughs as you draw your final breath. This foul crypt will be your resting place.")
                        return [pHP, pSCORE]
                #Else:
                else:
                    #Describe the player out-smarting the enemy
                    print(f"\nYou are too smart for the {eNAME}! You dodge out of the way!")
        #If enemy health is equal to or less than 0:
        elif eHP <= 0:
            sleep(1)
            print(f"\nThe {eNAME} collapses, victory is yours!")
            #Describe the treasure the player finds
            print(f"In the aftermath, you find the treasure horde of the {eNAME}!")
            #Add the value of the treasure to the player's score
            if eNAME == "Necro-Ghoul":
                print("\nAt last, the foul Necro-Ghoul has been slain! Rejoice and claim your bounty!")
                treasure = GenerateNumber(50, 100, 0)
                pSCORE += treasure
                print(f"You gain {treasure} points!")
            else:
                treasure = GenerateNumber(10, 30, 0)
                pSCORE += treasure
                print(f"You gain {treasure} points!")
            #Return the player's health and the player's score
            return [pHP, pSCORE]
        sleep(1)
        count += 1
    


#Return Type: 1 integer for random number
#Parameters: 1 integer for beginning of range, 1 integer for end of range
#and 1 integer for modifier
#Purpose: Generate a random number, add any relevant modifier, and return the result
#Define GenerateNumber
def GenerateNumber(begin, end, modifier):
    #Return [(random number from start of range to end of range) + integer modifier]
    return (randint(begin, end) + modifier)

#Return Type: n/a
#Parameters: n/a
#Purpose: Display rules of the game
#Define DisplayRules
def DisplayRules():
    userChoice = ""
    
    #Display a menu with options for explaining 1) Game Plot, 2) Character Statistics,
#3) Combat, 4) Treasure, 5) Exit
    
    while userChoice != "1" and userChoice != "2" and userChoice != "3" and userChoice != "4" and userChoice != "5":
        print("\nWelcome to the Rules Pub! What do you wish to learn?\n\n1) Game Plot\n2) Character Statistics"
          "\n3) Combat\n4) Treasure\n5) Exit")
        userChoice = input("\nEnter your choice: ")
        #If the user selects 1:
        if userChoice == "1":
            #Display the plot of the game and purpose of the adventure
            print("\nGame Plot:")
            
            #The goal is to collect as much treasure as possible before facing off against the
            #Necro-Ghoul at the end of the Dungeon
            print("\nDeep within the earth, the Necro-Ghoul resides within a foul crypt. Countless adventurers have fallen trying to slay the ghoul and claim its treasure, "
                  "they now shamble along the ever-changing rooms as the undead. You, a plucky adventurer, are willing to test your mettle in the crypt."
                  " Will you survive the crypt, and return with untold gold and glory, or will you meet a grisly end within those stone halls?")

            input("\n\nPress enter to return to the menu.")

        #If the user selects 2:
        elif userChoice == "2":
            #Display the rules of the character's statistics
            print("\nStatistics:")
            
            #Health determines how close the character is to death. If it reaches 0,
            #the game is over.
            print("\nHealth determines how close the character is to death. If it reaches 0, the game is over.")
            
            #Strength is how strong the character is. It determines how much damage an "attack"
            #does.
            print('\nStrength is how strong the character is. It determines how much damage an "attack" does.')
            
            #Endurance determines how sturdy a character is. It determines how well they can
            #avoid an enemy's "maneuver"
            print('\nEndurance determines how sturdy a character is. It determines how well they can avoid an enemy\'s "maneuver".')
            
            #Dexterity determines how nimble a character is. It determines the ability for a
            #character to land attacks, solve some obstacles, and deal damage for "maneuvers"

            print('\nDexterity determines how nimble a character is. It determines the ability for a character to land attacks, solve some obstacles, and deal damage for "maneuvers".')

            #Intelligence determines how witty and smart a character is. It determines the
            #effectiveness of a character's "maneuvers" and is used to solve many obstacles
            print('\nIntelligence determines how witty and smart a character is. It determines the effectiveness of a character\'s "maneuvers" and is used to solve many obstacles.')

            input("\n\nPress enter to return to the menu.")

        #If the user selects 3:
        elif userChoice == "3":
            #Display the rules of combat
            print("\nCombat:")
            
            #The player will always go first, and can choose to "attack" or "maneuver"
            print('\nThe player will always go first, and can choose to "attack" or "maneuver"')

            #An attack has the player strike the enemy. A number from 1 to 10 is generated,
            #   the character's Dexterity is added to the number.
            #   If the result is greater than 5, the attack hits. If the attack hits, then the enemy
            #   take damage equal to a random number from 1 to 10 plus the character's strength.
            print("\nAn attack has the player strike the enemy. A number from 1 to 10 is generated and the character's Dexterity is added to the number. "
                  "If the result is greater than 5, the attack hits. If the attack hits, then the enemy takes damage equal to a random number from 1 to 10 plus the character's strength.")
            
            #A maneuver has the player try to flank the enemy. A number from 1 to 10 is generated,
            #   the enemy's Endurance is added to the number, and then the total is compared
            #   to 5 + the player's intelligence. If the generated number is less than this,
            #   the maneuver succeeds, and the enemy takes damage equal to a random number from
            #   1 to 10 plus the character's dexterity.
            print("\nA maneuver has the player try to flank the enemy. A number from 1 to 10 is generated and the enemy's Endurance is added to the number."
                  " The total of those numbers are compared to 5 + the player's intelligence. If the generated number is less than this, the maneuver succeeds, "
                  "and the enemy takes damage equal to a random number from 1 to 10 plus the character's dexterity.")
            
            #This is a lot. Basically, a Fighter will do better with straight attacks, while a
            #Thief will prefer maneuvers
            print("\nIn essence, a Fighter will do better with straight attacks, while a Thief will prefer maneuvers.")

            input("\n\nPress enter to return to the menu.")
            
        #If the user selects 4:
        elif userChoice == "4":
            #Display rules about treasure
            print("\nTreasure:")
            #Treasure adds to the player's score.
            print("\nTreasure adds to the player's score. It can be obtained by clearing obstacles or defeating enemies.")
            #Treasure can be obtained from clearing obstacles or defeating enemies.

            #Be careful, failing to overcome an obstacle will cause some of the
            #potential treasure to be destroyed.
            print("\nBe careful, failing to overcome an obstacle will cause some of the potential treasure to be destroyed.")

            #The Necro-Ghoul guards a large horde of treasure, but it must be defeated first.
            print("\nThe Necro-Ghoul guards a large horde of treasure, but it must be defeated first.")

            input("\n\nPress enter to return to the menu.")
            
        #If the user selects 5, exit
        elif userChoice == "5":
            break
        
        else:
            print("\nYou must enter a number between 1 and 5. Try again.")
            sleep(1)
        userChoice = 0
            

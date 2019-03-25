########################################################################################################################
# 2019 NEA                                                                                                             #
#                                                                                                                      #
# Created By Shubham Pareek                                                                                            #
#                                                                                                                      #
########################################################################################################################

import random #This import allows values and elements to be randomised
import sys #Maninly used to exit the program in this code

player = []  # A list to contain all of the player cards
computer = []  # A list to contain all of the computer's cards
list_categ = ("1", "2", "3", "4")
name_cate = {1: "exercise", 2: "intelligence", 3: "friendliness", 4: "drool"}


def start_menu(): # This function is the opening menu for the game
    print("\tDog game")
    print("\n1) Play")
    print("2) Quit")
    pORq = input("-->")  # takes player's input to determine a choice
    if pORq == "1":
        initialise()
    elif pORq == "2":
        sys.exit()
    else:
        print("That was not an input choice. \n1 to play, 2 to quit")
        space = input("[Press Any Key To Continue]")
        start_menu()


def initialise():
    print("How many cards do you want in your deck?") # Decides number of cards in total
    ranger = int(input("-->"))
    if (ranger <= 30 and ranger >= 4 and ranger % 2 == 0):  # These are paramiters the user's hoice of number of cards must conform to
        print("Okay that is a good number of cards")
        with open("dogName.txt") as dogData:  # Opens the txt file to get the dog's name
            deck = dogData.read().splitlines()  # Splits each line into separate values
            play_card_num = int(ranger / 2)
            for x in range(play_card_num):  # This for loop iterates half for half of the ranger value
                exercise = random.randint(1, 5)
                intelligence = random.randint(1, 100) # The values for each card is assigned to a dog name per iteration
                friendliness = random.randint(1,10)
                drool = random.randint(1,10)
                player.append([random.choice(deck), exercise, intelligence, friendliness, drool])  # Appends each card as a list in a list- creating a nested list
            for x in range(play_card_num):
                exercise = random.randint(1, 5)
                intelligence = random.randint(1, 100)
                friendliness = random.randint(1,10)
                drool = random.randint(1,10)
                computer.append([random.choice(deck), exercise, intelligence, friendliness, drool])
        # print(player)
        # print(computer)
        play1(1, 1, ranger)  # Since the player's and the computer's decks have been created the turn number of 1, a value determining f the player or the computer playes first and the ranger value
    else:
        print("Keep in mind that the number you pick must be even and between 4 and 30")
        initialise()  # Returns the user to the start of the function if the raneger does not suit the requirements


def play1(turn, compOrPlaye ,ranger):
    print(len(player), "Player")
    print(len(computer), "comp")
    print("Your cards: ", player)
    if len(player) and len(computer) > 0: # Checks per turn if either the player or computer has won
        print("Turn:", turn)
        if compOrPlaye == 1:# Uses the compOrPlaye value to determine who choses a catagory
            print("\nPlayer Goes First!")
            print("What Category do you pick?")
            print("1) exercise")
            print("2) intelligence")
            print("3) friendliness")
            print("4) drool")
            category = input("-->")
            if category == "1" or "2" or "3" or "4":
                play2(category,turn,compOrPlaye,ranger)  # This sends the values category, turn,compOrPlaye  and ranger to the next phase of the game(play2)
            else:
                print("Select a CATEGORY!")
                play1(turn,compOrPlaye,ranger)
        else:
            print("How does it feel. The computer was faster so it goes first...")
            category = random.choice(list_categ)  # A random catagory is selected fron the list(list_categ) to determine a catagory
            space = input("press any key")
            play2(category,turn,compOrPlaye, ranger)
    else:
        print("That's is the end of the game..")
        if len(player) > len(computer): # Checks the number of cards in both the players deck
            print("You Won!")
        elif len(player) < len(computer):
            print("The computer wins")


def play2(category, turn, compOrPlaye , ranger):
    playerCat = player[0]  # This sets the values in the nested list to the first element hence, the fisrt list
    computerCat = computer[0]
    int_cate = int(category)
    print("The category", name_cate[int_cate], "was chosen")
    print("Player Stats:", playerCat[0], playerCat[int_cate],"vs Computer Stats:", computerCat[0], computerCat[int_cate])
    if int_cate == 4:  # If category is drool
        if playerCat[int_cate] > computerCat[int_cate]:
            print("\nThe computer won the round! The computer had the lower score")
            computer.extend([playerCat])  # This adds the loser's card to the winners deck (list)
            player.pop(0)  # This removes the first element in the list
            play1(turn + 1, 2, ranger)  # Sends the values back to the first phase of the game
        elif playerCat[int_cate] == computerCat[int_cate]:
            print("Both values are the same. The player wins")
            player.extend([computerCat])
            computer.pop(0)
            play1(turn + 1, 1, ranger)  # Sends information back to play1 to repeat the process until someone has won
        else:
            print("The player's value was less than the computer's. The player wins the round")
            player.extend([computerCat])
            computer.pop(0)
            play1(turn + 1, 1, ranger)
    else:  # if the category is not drool
        if playerCat[int_cate] > computerCat[int_cate]:
            print("\nWELL WELL WELL WELL WELL")
            print("Seems like the player won this round")
            print("You gain a card!")
            player.extend([computerCat])
            computer.pop(0)
            play1(turn + 1, 1,ranger)
        elif playerCat[int_cate] == computerCat[int_cate]:
            print("Even stevens!?")
            print("That won't do!\n")
            play1(turn,compOrPlaye,ranger)
        else:
            print("\nComputers are the new overlords ")
            print("The computer has won this round!")
            computer.extend([playerCat])
            player.pop(0)
            play1(turn + 1, 2, ranger)


start_menu()  # Tells the program to start from the function start_menu

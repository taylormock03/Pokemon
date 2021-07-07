import json
from pprint import pprint
from random import randint
import math
from enum import Enum
from Lib.Init.ObjectInit import *
from Lib.Init.CharacterInit import *
from Lib.Init.ItemInit import *
from Lib.Gen.Starter import *
from Lib.Gen.Battle import *
from Lib.Gen.Store import *

## Variable set up
global Generation_Number
global pokemon
global player
global locations
#Generation pokemon (it is obsoleted, but will be kept in until the data is sufficiently refactored)
global Generation


def firstload():
    ##I don't know why this needs to be redeclared since Generation_Number is already defined, but whatever
    global Generation_Number
    global player
    global locations
    global pokemon
    ##Figures out which save file needs to be loaded for the object Init file
    while True:
        Generation_Number = "6"
        # Checks if the entered value is not a number
    
        global Generation
        with open('Generations/Generation_'+ Generation_Number +'.txt') as json_file:
            Generation = json.load(json_file)            
        
        ##This is where the game objects are initialised
        pokemon,locations = loadAll(Generation)

        ##Figures out whether a savegame needs to be loaded
        start=input("Do you want to load a game? ")
        if start == "yes":

            # creates the player object which stores all the session's data
            player = loadPlayer(pokemon, Generation_Number,locations)
            
            # Generation data is no longer necessary as it has been loaded into objects
            Generation = None            
            break

        elif start =="no":
            if input("Are you sure? This will permanently delete all previous data ") =="yes":
                # creates an empty player
                player = Player([],[],locations[0],0,0,[])
                starter(player,Generation,pokemon)
                # The generation value can now be removed, as it is no longer useful
                Generation = None
                break
            else:
                # If you ended up here, You decided not to start a new game and you will be 
                # re-prompted to choose a generation
                print("")
        else:
            print("invalid response")

firstload()
###START GAME 
print("")
print("Game has started")

while True:
    game = input("What would you like to do? (general) ")
    if game =="help":
        print("wild - spawns a random pokemon")#Completed
        print("trainer - starts a trainer fight (gym battle)")#Completed
        print("save - saves your progress (only one save can be stored at one time") #Completed
        print("load - loads your last save. (all unsaved progress will be lost)") #Completed
        print("quit - will quit your game (all unsaved progress will be lost)") #Completed
        print("buy - will buy a pokeball for $200") # Completed
        print("pc - will allow you to view and change the pokemon in your PC") #Completed
        print("party - will allow you to view your party pokemon and their stats") #Completed
        print("location - will show you your location, what pokemon can spawn there, and allow you to travel to other towns (as long as you have won enough battles to do so)") #completed
        print("money - will show you your current money") #Completed
        print("arrange - allows you to rearrange your party or swap your party pokemon with ones in your PC") #Completed

    elif game == "wild":
        wildBattleInit(player)

    elif game == "trainer":
        trainerBattleInit(player)

    elif game == "save":
        savePlayer(player,Generation_Number)

    elif game == "load":
        player = loadPlayer(pokemon,Generation_Number,locations)

    elif game == "quit":
        game=input("Would you like to save first? ")
        if game =="yes":
            savePlayer(player,Generation_Number)
            break
        elif game == "no":
            break

    elif game == "buy":
        storeInit(player,pokemon)

    elif game == "pc":
        player.printPc()

    elif game =="party":
        player.printParty()

    elif game =="location":
        player.printLocation()

        while True:
            travel = input("\nWould you like to travel? ")
            if travel == "yes":
                player.travelLocation(locations)
                break

            elif travel == "no":
                break

            else:
                print("Invalid entry")


    elif game =="money":
        print("You have: $" + str(player.getMoney()))

    elif game =="order":
        while True:
            check = input("\nWould you like to swap your party order (party) or put your pc pokemon into your party (pc)? ")
            if check == "party":
                player.partyOrder()
                break
            elif check == "pc":
                player.pcOrder()
                break
            else:
                print("Invalid entry")

    else:
        print("invalid response (input 'help' for a list of commands. This is available on almost any screen)")
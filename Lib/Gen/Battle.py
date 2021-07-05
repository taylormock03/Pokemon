
# This is where wild encounters will be initialised
def wildBattleInit(player):
    # Choose a random pokemon from the location
    # NOTE: this will return an array with a single pokemon
    # this is important as an array is used in the main battle function
    wildPokemon = player.getEncounter()
    
    # initialises all battle stats for the player
    player.battleInit()
    print("You encountered a wild:\n" + str(wildPokemon[0]))
    battle(player,wildPokemon,False)
    
def trainerBattleInit(player):
    # Loads the gym leader from the player's current location and initialises stats
    trainer = player.getGym()
    trainer.battleInit()
    
    # initialises all battle stats for the player
    player.battleInit()

    battle(player, trainer.pokemon,True)

# This is the main function for battling
# gymFight is a boolean that tells the program if you are fighting a gym trainer
# This is mainly used for prevention of the user running and moving to new areas
def battle(player,ai,gymFight):
    
    while True:
        while True:
            try:
                selection = int(input("What would you like to do ?\n#1 Attack\n#2 Switch Pokemon\n#3 Items \n#4 Run\n>"))
                if selection >4 or selection<1:
                    raise
                break
            except:
                print("Invalid entry")

        if selection == 1:
            attack(player,ai)
        elif selection ==2:
            player.partyOrder()
        elif selection == 3:
            items(player)
        elif selection == 4:
            runSuccessful = run(player,ai)
            if runSuccessful:
                print("Got away safely!")
                break
            else:
                print("You tried to run...\nYou could't get away")

        
# Checks to see if all pokemon are dead. 
# Returns True when all pokemon are dead
def checkDead(pokeList):
    for x in pokeList:
        # If any pokemon has a health of >0, then not all pokemon are dead
        if x.getHealth() >0:
            return False
    return True

def attack(player,ai):
    return

def items(player):
    return

def run(player,ai):
    return
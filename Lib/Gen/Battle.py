
# This is where wild encounters will be initialised
def wildBattleInit(player):
    # Choose a random pokemon from the location
    # NOTE: this will return an array with a single pokemon
    # this is important as an array is used in the main battle function
    wildPokemon = player.getEncounter()
    
    # initialises all battle stats for the player
    player.battleInit()
    print("\nYou encountered a wild:\n" + str(wildPokemon[0]))
    battle(player,wildPokemon,False)
    
def trainerBattleInit(player):
    # Loads the gym leader from the player's current location and initialises stats
    trainer = player.getGym()
    trainer.battleInit()
    
    # initialises all battle stats for the player
    player.battleInit()

    print("\nThe Gym leader sends out " + str(trainer.pokemon[0]))
    battle(player, trainer.pokemon,True)

# This is the main function for battling
# gymFight is a boolean that tells the program if you are fighting a gym trainer
# This is mainly used for prevention of the user running and moving to new areas
def battle(player,ai,gymFight):
    # this will return a list of pokemon within the player's party
    playerPokemon = player.getBattlePokemon()

    currentPokemon = 0
    print("Go " + playerPokemon[currentPokemon].name +"!")
    
    # success is a boolean that tells the system whether an action was valid
    # for instance, if someone tried to throw a pokeball at a gym trainer's 
    # pokemon, this would fail as they can't be caught, but would not count as a turn
    success = False
    while not success:
        while True:
            try:
                selection = int(input("What would you like to do ?\n#1 Attack\n#2 Switch Pokemon\n#3 Items \n#4 Run\n>"))
                if selection >4 or selection<1:
                    raise
                break
            except:
                print("Invalid entry")

        if selection == 1:
            success = attack(player,ai)
        elif selection ==2:
            player.partyOrder()
            success = True
        elif selection == 3:
            success = items(player,ai,gymFight,currentPokemon)
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

def items(player,ai,gymFight, currentPokemon):
    print("What would you like to use: ")
    i=1
    for x in player.items:
        print("#" + str(i) + " " +str(x))
        i+=1
    while True:
        try:
            selection = int(input(">"))-1
            if selection<0 or selection>=len(player.items):
                raise
            else:
                break
        except:
            print("Invalid entry")

    # Check what type of item is being used
    if type(player.items[selection]).__name__ == "CatchItem":
        return player.items[selection].effect(ai[0],player,gymFight)

    else: 
        return player.items[selection].effect(player,currentPokemon)


def run(player,ai):
    return
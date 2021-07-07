# This is where wild encounters will be initialised
from Lib.Init.ObjectInit import Pokemon
from random import randint


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
    aiCurrent = 0
    print("Go " + playerPokemon[currentPokemon].name +"!\n")
    
    caughtPokemon = False
    runSuccessful = False
    # success is a boolean that tells the system whether an action was valid
    # for instance, if someone tried to throw a pokeball at a gym trainer's 
    # pokemon, this would fail as they can't be caught, but would not count as a turn
    playerSuccess = False

    # This is the main battle loop. It will only end when either the player passes out, trainer passes out, or player runs
    while True and not runSuccessful and not caughtPokemon:
        
        # This is the player's turn
        while not playerSuccess:
            while True:
                try:
                    selection = int(input("What would you like to do ?\n#1 Attack\n#2 Switch Pokemon\n#3 Items \n#4 Run\n>"))
                    if selection >4 or selection<1:
                        raise
                    break
                except:
                    print("Invalid entry")

            # attack
            if selection == 1:
                playerSuccess = attack(playerPokemon[currentPokemon],ai[aiCurrent])
            
            # swap pokemon
            elif selection ==2:
                try:
                    i=1
                    for x in playerPokemon:
                        print("#" + str(i) + " "+str(x))
                    selection = int(input("Which pokemon would you like to swap in\n>"))-1
                    if selection <0 or selection >len(playerPokemon)-1:
                        raise

                    currentPokemon = selection
                    print("Go " + playerPokemon[currentPokemon].name +'!')  
                    
                    playerSuccess = True
                except:
                    playerSuccess = False
                
            # Use Items
            elif selection == 3:
                playerSuccess,caughtPokemon = items(player,ai,gymFight,currentPokemon)
            
            # Attempt to run away
            elif selection == 4:
                runSuccessful = run(playerPokemon[currentPokemon],ai,gymFight)
                if runSuccessful:
                    print("Got away safely!")
                    break
                else:
                    print("You tried to run...\nYou could't get away")
                    playerSuccess = True

        if caughtPokemon or runSuccessful:
            break
        
        # Applies any burn or poison damage
        statusEffect(ai[aiCurrent])

        # Calculates if the ai's pokemon passed out
        if ai[aiCurrent].battleHealth <=0:
            print(ai[aiCurrent].name + " passes out")
            if checkDead(ai):
                print("You Win!")
                calculateResults(player,playerPokemon,ai,gymFight)
                break
            else:
                aiCurrent+=1
                print("Trainer sends out " + str(ai[aiCurrent])+"\n")
        else:
            print(ai[aiCurrent].name + " has " + str(ai[aiCurrent].battleHealth) + " HP\n")

        # Ai's turn
        aiAttack(ai[aiCurrent],playerPokemon[currentPokemon])
        

        # apply any burn or poison damage to the player
        statusEffect(playerPokemon[currentPokemon])

        # Check if player passed out
        if playerPokemon[currentPokemon].battleHealth <=0:
            print(playerPokemon[currentPokemon].name + " passes out")
            if checkDead(playerPokemon):
                print("You Pass out!\n")
                break
            else:
                # Get player to swap out their pokemon
                i = 1
                for x in playerPokemon:
                    print("#" + str(i) + " " + str(Pokemon))

                while True:
                    try:
                        selection = int(input("Which pokemon would you like to sub in? \n>"))-1
                        if selection<0 or selection>6 or playerPokemon[selection].battleHealth <=0:
                            raise
                        else:
                            currentPokemon = selection
                            print("Go " + playerPokemon[currentPokemon].name)
                            break
                    except:
                        print("That pokemon's already passed out")
        else:
            print(playerPokemon[currentPokemon].name + " has " + str(playerPokemon[currentPokemon].battleHealth) + " HP\n")

        # Reset player's decisions
        playerSuccess = False

# Checks to see if all pokemon are dead. 
# Returns True when all pokemon are dead
def checkDead(pokeList):
    for x in pokeList:
        # If any pokemon has a health of >0, then not all pokemon are dead
        if x.getHealth() >0:
            return False
    return True

def attack(playerPokemon,aiPokemon):
    
    playerMoves = playerPokemon.getMoves()
    print("\nWhat move would you like to use?\n")
    i=1
    for x in playerMoves:
        print("#" +str(i) +" " + str(x))
        i+=1
        
    while True:
        try:
            selection = int(input("> "))-1
            if selection >4 or selection <0:
                raise
            print()
            return playerMoves[selection].attack(playerPokemon,aiPokemon)
            break
        except:
            print("Invalid input")

# runs mostly the same as the attack function, but allows a decision to be made
# without user input. It selects a random move from the ai's moveset and attacks
# the player
def aiAttack(aiPokemon,playerPokemon):
    selection = randint(0,3)
    moves = aiPokemon.getMoves()
    moves[selection].attack(aiPokemon,playerPokemon)

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
        return player.items[selection].effect(player,currentPokemon),False


def run(playerPokemon,ai,gymBattle):
    if gymBattle:
        print("You can't do that right now")
        return False

    if playerPokemon.battleSpeed > ai[0].battleSpeed:
        return True

    escapeOdds = (((playerPokemon.battleSpeed*128)/ai[0].battleSpeed)+30)%256
    randomNumber = randint(0,255)
    return randomNumber < escapeOdds

# Will calculate money rewards and xp gain
def calculateResults(player,playerPokemonList,ai,gymFight):
    # calculate the results for a gym fight
    for x in ai:
        calculateXp(playerPokemonList,x,gymFight)
    
    # Check if any pokemon are leveling up
    for x in playerPokemonList:
        x.levelCheck()

    if gymFight:
        player.addMoney(500)
        print("You earned $500\nYou can now travel to a new location!")
        player.addBattleWon()
    
    else:
        player.addMoney(50)
        print("You earned $50")
                

# this calculates the xp gain from each battle
# Formula sourced from https://bulbapedia.bulbagarden.net/wiki/Experience
def calculateXp(playerPokemonList,defeatedPokemon,gymFight):
    s = 0
    for x in playerPokemonList:
        if x.battleHealth >0:
            s+=1
            
    b = 163
    
    l = defeatedPokemon.getLevel()

    for x in playerPokemonList:
        lP = x.getLevel()

        exp = round((((b*l)/(5*s))*((2*l+10)/(l*lP+10))**2.5))
        
        x.addXp(exp)


def statusEffect(pokemon):
    if pokemon.status == "Burn" or pokemon.status == "Poison":
        damage = pokemon.maxHealth/16
        print(pokemon.name + " lost " + str(damage) + " HP due to " + pokemon.status)
        pokemon.battleHealth-= damage

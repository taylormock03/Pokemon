from Lib.Init.ObjectInit import Pokemon


def starter(player,data, pokemon):

    # Finds the starter pokemon IDs from the Json file
    starterId = []
    starterPokemon = []
    starterId +=(data["Starter1"])
    starterId +=(data["Starter2"])
    starterId +=(data["Starter3"])

    # compiles the starters into pokemon objects
    for x in starterId:
        name, type1, type2, hp, attack, defence, speed, id, learnsets, nextEvolve= pokemon[int(x)].clone()
        newPokemon = Pokemon(name, type1, type2, hp, attack, defence, speed, id, learnsets, nextEvolve)
        starterPokemon.append(newPokemon)
    
    print("")
    print("Welcome to the world of Pokemon. Today you will be given a choice of your first pokemon. Here are your choices")

    print("#1 " + str(starterPokemon[0]))
    print("#2 " + str(starterPokemon[1]))
    print("#3 " + str(starterPokemon[2]))
    
    # This is where the user selects the pokemon
    # If they enter an invalid number, an error will be thrown,
    # and an error will pop up
    while True:
        try:
            starter = int(input("Which number pokemon would you like? "))
            if starter<=3 and starter>=1:
                player.addPc(starterPokemon[starter-1])
                print(starterPokemon[starter-1].name + "! Good Choice")
                break
            else:
                raise()
        except:
            print("Invalid number")
        
        
    print("With your new pokemon you are free to go into the wild. Remember, if you are ever lost just yell HELP")
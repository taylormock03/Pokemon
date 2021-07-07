# This is where the user will first go to the store and be sent to sub areas
from Lib.Init.ObjectInit import Pokemon
from Lib.Init.ItemInit import CatchItem, HealItem, StatusItem


def storeInit(player,pokemon):
    print("\nWelcome Trainer! You have $" + str(player.getMoney()))
    
    selection = ""
    while selection != "leave":
        selection = input("\nWhat are you looking for \n#1 Pokeballs\n#2 Healing Items\n#3 Status Healers\n#4 Pokemon\nOr just type 'leave' to go on your way\n>")

        if selection == "1":
            catchItems(player)
        elif selection == "2":
            healItems(player)
        elif selection == "3":
            statusItems(player)
        elif selection == "4":
            pokeBuy(player,pokemon)
        elif selection == "leave":
            break
        else:
            print("Invalid input")

# This is where items that can catch pokemon are bought (such as pokeballs)
def catchItems(player):
    items = []
    # Add catch items to a list
    items.append(CatchItem("Poke Ball",100,1))
    items.append(CatchItem("Great Ball",200,1.5))
    items.append(CatchItem("Ultra Ball",300,2))
    items.append(CatchItem("Master Ball",1000,1000))

    # iterate through the item list and print out the items
    print("\nWe have:")
    i = 1
    for x in items:
        print ("#" + str(i) + " " + str(x) +"\n")
        i+=1
    
    print("Or enter 0 to leave without anything")
    while True:
        try:
            selection = int(input("What would you like to buy? "))-1

            if selection == -1:
                break
            elif selection >=0 and selection <len(items):
                quanity = int(input("How many would you like? "))
                items[selection].buyItem(quanity,player)
            else:
                raise
        
        except:
            print("Invalid input")

# This is where you buy healing items such as potions
def healItems(player):
    items = []
    # Add catch items to a list
    items.append(HealItem("Potion",100,1))
    items.append(HealItem("Super potion",400,2.5))
    items.append(HealItem("Hyper potion",800,10))
    items.append(HealItem("Full Heal",1000,1000))

    # iterate through the item list and print out the items
    print("\nWe have:")
    i = 1
    for x in items:
        print ("#" + str(i) + " " + str(x) +"\n")
        i+=1
    
    print("Or enter 0 to leave without anything")
    while True:
        try:
            selection = int(input("What would you like? "))-1

            if selection == -1:
                break
            elif selection >=0 and selection <len(items):
                quanity = int(input("How many would you like? "))
                items[selection].buyItem(quanity,player)
            else:
                raise
        
        except:
            print("Invalid input")

# This is where you can buy status heals such as burn heals
def statusItems(player):
    items = []
    # Add catch items to a list
    items.append(StatusItem("Burn Heal",100,"Burn"))
    items.append(StatusItem("Antidote",100,"Poison"))
    items.append(StatusItem("Awakening",100,"Sleep"))
    items.append(StatusItem("Ice Heal",100,"Ice"))
    items.append(StatusItem("Paralysis Heal",100,"Paralysis"))
    items.append(StatusItem("Yellow Flute",100,"Confusion"))


    # iterate through the item list and print out the items
    print("\nWe have:")
    i = 1
    for x in items:
        print ("#" + str(i) + " " + str(x) +"\n")
        i+=1
    
    print("Or enter 0 to leave without anything")
    while True:
        try:
            selection = int(input("What would you like? "))-1

            if selection == -1:
                break
            elif selection >=0 and selection <len(items):
                quanity = int(input("How many would you like? "))
                items[selection].buyItem(quanity,player)
            else:
                raise
        
        except:
            print("Invalid input")

# This is where you can buy pokemon (this doesn't exist AFAIK in the real game so
# the calculation of price is likely not going to be very balanced)
def pokeBuy(player,pokemon):
    selection = input("Please enter the name of the pokemon you would like \n>")
    
    found = False
    for x in pokemon:
        if x.name == selection:
            found = True
            break
    
    if not found:
        print("We couldn't find a pokemon with that name")
        return
    
    while True:
        try:
            level = int(input("What level would you like your pokemon to be? "))
            if level <=0:
                raise
            break
        except:
            print("Invalid input")

    cost = level* 100

    name, type1, type2, hp, attack, defence, speed, id, learnsets, nextEvolve = x.clone()
    newPokemon = Pokemon(name, type1, type2, hp, attack, defence, speed, id, learnsets, nextEvolve)
    newPokemon.randomMoves()
    newPokemon.setLevel(level)
    newPokemon.addXp(level**3)
    print("Your Lvl " + str(newPokemon.getLevel()) + " " + newPokemon.name + " will cost $" + str(cost))
    selection = input("Would you like to buy it? ")
    if selection == "yes" and player.getMoney()>=cost:
        player.addPc(newPokemon)
        player.addMoney(0-cost)
        print("Successfully bought")
    elif player.getMoney()<cost:
        print("Sorry, you don't have enough money to afford this")

    return
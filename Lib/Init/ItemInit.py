# Generic item class which will deal with inventory management and purchases
from random import randint


class Item:
    cost=0
    quantity=0

    def __init__(self):
        self.cost = 0
        self.quantity = 0

    def buyItem(self,quantity,player):
        # the price is equal to the number of items x the cost of 1 item
        price = self.cost * quantity

        # If the player can afford the purchase this gets run
        if price <= player.getMoney():
            # the player gets a negative amount of money added to their account
            player.addMoney(0-price)
            self.quantity += quantity
            # item is added to the user's inventory
            player.addInventory(self)
            print("Successfully bought!\n")
        else:
            print("You do not have enough money to do that")

# Anything that can catch another pokemon (pokeball, greatball,etc.)
# This will deal with any catch related calculation
class CatchItem(Item):
    ballBonus = 1
    name = ""

    def __init__(self,name,cost,ballBonus):
        self.ballBonus = ballBonus
        self.name = name
        self.cost = cost
        self.quantity = 0

    # This is what will calculate whether you catch a pokemon or not
    def effect(self,pokemon,player,gymFight):
        
        # Check if the player is currently in a gym fight where pokemon
        # can't be caught
        if gymFight:
            print("You can't do that now")
            return False

        if self.quantity<=0:
            return False
        self.quantity-=1

    #    This formula is from https://www.dragonflycave.com/mechanics/gen-vi-vii-capturing

        captureRate = ((3*pokemon.maxHealth-2*pokemon.battleHealth)*0.5*self.ballBonus)/3*pokemon.maxHealth

        escapeNumber = 65536/((255/captureRate)**(3/16)) 
        escape = False
        i = 0
        while i<4:
            if randint(0,65535)<escapeNumber:
                escape = True
                break
            i+=1
        
        if captureRate>255 or escape == False:
            player.addPc(pokemon)
            print("Successfully caught " + pokemon.name)
        else:
            print("It got out")

        return True
    
    # This will store the object as a dictionary so it can be saved
    def saveValues(self):
        valueDict ={
            "Class":"CatchItem",
            "ballBonus":self.ballBonus,
            "name":self.name,
            "cost":self.cost,
            "quantity":self.quantity
        }
        return valueDict


    def __str__(self):
        return self.name + "\n    Cost: $" + str(self.cost) + "\n    Catch Bonus: " + str(self.ballBonus) 

# These items will restore HP (but not status effects)
class HealItem(Item):
    healBonus = 1
    cost = 0
    name = ""

    def __init__(self, name,cost,healBonus) :
        self.cost  = cost
        self.name = name
        self.healBonus = healBonus
        self.quantity = 0

    # ignore is just a boolean value that is not used by this function but is used by catchItems
    def effect(self,player,currentPokemon):
        # Choose the pokemon from 
        pokemon = player.getPokemon(currentPokemon)
        
        if self.quantity>0:
            healAmount = self.healBonus *20
            if healAmount <pokemon.maxHealth:
                pokemon.battleHealth += healAmount
                print(pokemon.name + " healed: " + str(healAmount) +"HP")
            else:
                pokemon.battleHealth = pokemon.maxHealth
                print(pokemon.name + " is now fully healed")
            
            print(pokemon.name +" has " + str(pokemon.battleHealth) +'HP')
            
            self.quantity-=1
            return True
        else:
            print("You do not have enough " + self.name + " to do this")
            return False
        

    # This will store the object as a dictionary so it can be saved
    def saveValues(self):
        valueDict ={
            "Class":"HealItem",
            "healBonus":self.healBonus,
            "name":self.name,
            "cost":self.cost,
            "quantity":self.quantity
        }
        return valueDict
    
    def __str__(self):
        return self.name + "\n    Cost: $" + str(self.cost) + "\n    Heal Bonus: " + str(self.healBonus) 

class StatusItem(Item):
    statusType = ""
    cost = 0
    name = ""

    def __init__(self,name,cost,status):
        self.cost = cost
        self.statusType = status
        self.name = name
        self.quantity = 0
    
     # This is what will heal status effects
    def effect(self,player, currentPokemon):
        if self.quantity<=0:
            return False
        self.quantity-=1
        currentPokemon = player.getPokemon(currentPokemon)

        if self.statusType == currentPokemon.status:
            currentPokemon.status = ""
            print(self.statusType + " Cured")
            return True
        else:
            print(currentPokemon.name + " is not currently " + self.statusType + "ed")
            return False

    # This will store the object as a dictionary so it can be saved
    def saveValues(self):
        valueDict ={
            "Class":"StatusItem",
            "status":self.statusType,
            "name":self.name,
            "cost":self.cost,
            "quantity":self.quantity
        }
        return valueDict

    def __str__(self):
        return self.name + "\n    Cost: $" + str(self.cost) + "\n    Status type: " + str(self.statusType) 
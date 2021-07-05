# Generic item class which will deal with inventory management and purchases
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

    def attemptCatch():
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

    def heal():
        return

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
    
    def cure():
        return

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
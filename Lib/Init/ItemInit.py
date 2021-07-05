# Generic item class which will deal with inventory management and purchases
class Item:
    cost=0
    quantity=0

    def buyItem(self,quantity,player):
        # the price is equal to the number of items x the cost of 1 item
        price = self.cost * quantity

        # If the player can afford the purchase this gets run
        if price < player.getMoney():
            # the player gets a negative amount of money added to their account
            player.addMoney(0-price)
            self.quantity = quantity
            # item is added to the user's inventory
            player.addInventory(self)
            print("Successfully bought!")
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

    def attemptCatch():
        return True
    
    def __str__(self):
        return self.name + "\n    Cost: $" + str(self.cost) + "\n    Catch Bonus: " + str(self.ballBonus) 

# These items will restore HP (but not status effects)
class HealItem(Item):
    healBonus = 1
    cost = 0
    name = ""

    def __init__(self, healBonus,cost,name) :
        self.cost  = cost
        self.name = name
        self.healBonus = healBonus

    def heal():
        return

class StatusItem(Item):
    statusType = ""
    cost = 0
    name = ""

    def __init__(self,status,cost,name):
        self.cost = cost
        self.statusType = status
        self.name = name
    
    def cure():
        return
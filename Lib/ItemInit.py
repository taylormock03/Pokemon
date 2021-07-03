# Generic item class which will deal with inventory management and purchases
class Item:
    cost=0
    quantity=0

    def buyItem():
        return

# Anything that can catch another pokemon (pokeball, greatball,etc.)
# This will deal with any catch related calculation
class CatchItem(Item):
    ballBonus = 1
    name = ""

    def __init__(self,ballBonus,cost,name):
        self.ballBonus = ballBonus
        self.name = name
        self.cost = cost

    def attemptCatch():
        return True

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
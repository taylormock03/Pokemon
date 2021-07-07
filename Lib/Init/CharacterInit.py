from Lib.Init.ObjectInit import Pokemon
from Lib.Init.ItemInit import CatchItem, HealItem, StatusItem
import json
from random import randint
import math

class Player:
    __party=[]
    __pc=[]
    __currentLocation = 0
    __battleWon = 0
    __money = 0
    items = []

    def __init__(self, party,pc,currentLocation,battleWon,money,items):
        self.__party=party
        self.__pc=pc
        self.__currentLocation=currentLocation
        self.__battleWon=battleWon
        self.__money=money
        self.items=items

    def getLocationId(self):
        return self.__currentLocation.id
    
    def getBattleWon(self):
        return self.__battleWon

    def addBattleWon(self):
        self.__battleWon +=1
        
    def getMoney(self):
        return self.__money
    
    def getItems(self):
        itemDict ={}
        i=0
        for x in self.items:
            itemDict[i] = x.saveValues()
            i+=1
        return itemDict

    # Turns the PC within a player object into an array of strings 
    # that can be sent to the savefil
    def getPc(self):
        fullArray = self.__pc + self.__party
        fullId = []
        fullLevel = []
        fullMoves = []
        fullXp = []
        for x in fullArray:
            fullId.append(x.id)
            fullLevel.append(x.getLevel())
            fullXp.append(x.getXp())
            movesetString =""
            for move in x.getMoves():
                movesetString +=str(move.id) + "-"
            fullMoves.append(movesetString[:-1])

        return fullId,fullLevel,fullXp,fullMoves

    def getParty(self):
        fullArray = self.__pc + self.__party
        partyPosition=[]
        for pokemon in self.__party:
            index = 0
            for position in fullArray:
                if pokemon == position:
                    partyPosition.append(index)
                index+=1
        return partyPosition

    # This is used during the battle to keep track of all the party pokemon
    def getBattlePokemon(self):
        return self.__party

    def addPc(self,pokemon):
        
        if len(self.__party)<6:
            self.__party.append(pokemon)
        else:
            self.__pc.append(pokemon)
    
    # will show all pokemon within user's party
    def printParty(self):
        print("\nYOUR PARTY:")
        i = 0
        for x in self.__party:
            print("#" + str(i) + " " + str(x))
            i+=1
        print()

    # will show all pokemon within user's PC
    def printPc(self):
        print("\nYOUR PC:")
        i = 0
        for x in self.__pc:
            print("#" + str(i) + " " + str(x))
            i+=1
        if i ==0:
            print("There's nothing here")
        print()

    # This will show the player where they are and what they can catch
    def printLocation(self):
        print(str(self.__currentLocation))


    # The order of the party can be changed
    # e.g [1,2,3] will become [1,3,2]
    def partyOrder(self):
        self.printParty()

        # Select the index of the first pokemon within the party
        while True:
            try:
                swap1 = int(input("\nWhat is your first pokemon you would like to swap? "))

                # Checks if the chosen number is larger than the party size
                if swap1>=len(self.__party):
                    raise
                break
            except:
                print("Invalid entry")
        
        # Select the index of the second pokemon within the party
        while True:
            try:
                swap2 = int(input("\nWhat is your first pokemon you would like to swap? "))
                # Checks if the chosen number is larger than the party size or is the same as the previous number
                if swap2>=len(self.__party):
                    raise
                break
            except:
                print("Invalid entry")

        # swaps pokemon here
        tempPokemon = self.__party[swap1]
        self.__party[swap1] = self.__party[swap2]
        self.__party[swap2] = tempPokemon

        print("Swapped Successfully!")

    # allows pokemon within the pc to trade places with the party pokemon
    def pcOrder(self):
        self.printParty()

        # Select the index of the  pokemon within the party
        while True:
            try:
                swap1 = int(input("\nWhich party pokemon would you like to swap out? "))

                # Checks if the chosen number is larger than the max party size (6)
                if swap1>=6:
                    raise
                break
            except:
                print("Invalid entry")

        self.printPc()

        # Select the index of the first pokemon within the party
        while True:
            try:
                swap2 = int(input("\nWhich PC pokemon would you like to swap in? "))

                # Checks if the chosen number is larger than the pc size
                if swap2>=len(self.__pc):
                    raise
                break
            except:
                print("Invalid entry")

        return

    # This will show where the player can travel and move them
    def travelLocation(self,locations):
        print("You can travel to: ")
        i = 0
        while i<=self.__battleWon:
            print("#" + str(i) + " " +locations[i].name)
            i+=1

        while True:
            try:
                destination = int(input("Which Town would you like to visit? "))
                if destination >= i or destination<0:
                    raise
                
                print("You are now at: " + locations[destination].name) 
                self.__currentLocation = locations[destination]
                break
            except:
                print("Invalid entry")

    def getEncounter(self):
        # chooses a random pokemon from the pokemon in the location
        encounterPokemon = self.__currentLocation.getEncounter()
        name, type1, type2, hp, attack, defence, speed, id, learnsets, nextEvolve= encounterPokemon.clone()
        
        # The encounter pokemon is a pointer to the pokemon in the pokemon list
        # If I don't run this line, anything that happens to encounterPokemon,
        # will happen to the pokemon within the pokemon list
        newPokemon = Pokemon(name, type1, type2, hp, attack, defence, speed, id, learnsets, nextEvolve)
        # set level of pokemon within +- 10% of player's first party pokemon's
        level = self.getPartyLevel()
        newPokemon.setLevel(level)

        # set the moves of the pokemon
        newPokemon.randomMoves()

        # set the health and pp of the wild pokemon
        newPokemon.battleInit()

        return [newPokemon]

    # gets a random level within 10% of the first pokemon in the party
    def getPartyLevel(self):
        originalLevel=self.__party[0].getLevel()
        newLevel = randint(
            round(originalLevel*0.9),
            round(originalLevel*1.1)
        )
        return newLevel

    # This will run the battleInit method within the pokemon class
    # for every pokemon within the player's party
    def battleInit(self):
        for x in self.__party:
            x.battleInit()

    def getGym(self):
        return self.__currentLocation.gym

    # This will add bought items into the player's __item list
    def addInventory(self,item):
        # This is checking if an item of the same name exists already
        # if it does, the new quantity will be added on top of the existing
        # quantity of items
        found = False
        for x in self.items:
            if x.name == item.name:
                found=True
                break
        if not found:
            # If this line gets run, it means that the user does not have
            # any of that item and it will be added onto the end of the items list
            self.items.append(item)

    def addMoney(self,amount):
        self.__money +=amount

    def catch(self,pokemon):
        return

    def getPokemon(self,id):
        return self.__party[id]



# This will allow for the player to be loaded from the gamedata file
# The file uses many pointers in a dictionary, so this function needs to 
# parse it so that it can be used
def loadPlayer(pokemon,genNumber,location):
    with open('gamesaves/gamedata_'+ genNumber +'.txt') as json_file:
        gamedata = json.load(json_file)
    
    # Load in the items
    items = []
    for x in gamedata["Items"]:
        x = gamedata["Items"][x]
        if x["Class"] == "CatchItem":
            newObject = CatchItem(
                                    x["name"],
                                    x["cost"],
                                    x["ballBonus"],
                                            )
            newObject.quantity = x["quantity"]
            items.append(newObject)

        elif x["Class"] == "HealItem":
            newObject = HealItem(
                                    x["name"],
                                    x["cost"],
                                    x["healBonus"],
                                            )
            newObject.quantity = x["quantity"]
            items.append(newObject)

        elif x["Class"] == "StatusItem":
            newObject = StatusItem(
                                    x["name"],
                                    x["cost"],
                                    x["status"],
                                            )
            newObject.quantity = x["quantity"]
            items.append(newObject)


    pc = []
    i=0
    # load in the pokemon within the player's PC
    for id in gamedata["Pc"]:
        # loads in pokemon object
        name, type1, type2, hp, attack, defence, speed, id,learnsets,nextEvolve =pokemon[int(id)].clone()
        newPokemon= Pokemon(name, type1, type2, hp, attack, defence, speed, id, learnsets,nextEvolve)
        pc.append(newPokemon)

        # sets pokemon object's level
        pc[i].setLevel(gamedata["PcLevel"][i])

        # Parses gamedata's moves into ids which are given to the pokemon object
        tempMoves = gamedata["PcMoves"][i].split("-")
        for moveId in tempMoves:
            pc[i].setMoves(int(moveId))
        
        # set xp to correct value
        pc[i].setXp(gamedata["xp"][i])
        i+=1

    # Assign party members
    # This will act based on the pointers within the save file
    # e.g party:0 means that the first pokemon in the pc is in the party
    party=[]
    indexOffset=0
    for x in gamedata["party"]:
        if x == "":
            pass
        else:
            party.append(pc[x+indexOffset])
            # remove the pokemon from the party once it has been added to the pc
            pc.pop(x+indexOffset)
            indexOffset-=1
    print("Loaded Successfully")
    return Player(  party,
                    pc,
                    location[gamedata["CurrentLocation"]],
                    gamedata["BattleWon"],
                    gamedata["money"],
                    items)


def savePlayer(player,genNumber):
    saveData={}
    id,level,xp,moves=player.getPc()
    party = player.getParty()
    saveData["party"]=party
    saveData["Pc"]=id
    saveData["PcLevel"]=level
    saveData["xp"]=xp
    saveData["PcMoves"]=moves
    saveData["CurrentLocation"]=player.getLocationId()
    saveData["BattleWon"]=player.getBattleWon()
    saveData["money"]=player.getMoney()
    saveData["Items"] = player.getItems()

    print("Saved Successfully")
    with open('gamesaves/gamedata_' + genNumber + '.txt', 'w') as outfile:  
        json.dump(saveData, outfile, indent=1)
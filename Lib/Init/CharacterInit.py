import json

class Player:
    __party=[]
    __pc=[]
    __currentLocation = 0
    __battleWon = 0
    __money = 0
    __items = []

    def __init__(self, party,pc,currentLocation,battleWon,money,items):
        self.__party=party
        self.__pc=pc
        self.__currentLocation=currentLocation
        self.__battleWon=battleWon
        self.__money=money
        self.__items=items

    def getLocationId(self):
        return self.__currentLocation.id
    
    def getBattleWon(self):
        return self.__battleWon

    def getMoney(self):
        return self.__money
    
    def getItems(self):
        return self.__items

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

    def addPc(self,pokemon):
        pokemon.setInitMoves()
        
        if len(self.__party)<6:
            self.__party.append(pokemon)
        else:
            self.__pc.append(pokemon)

# This will allow for the player to be loaded from the gamedata file
# The file uses many pointers in a dictionary, so this function needs to 
# parse it so that it can be used
def loadPlayer(pokemon,genNumber,location):
    with open('gamesaves/gamedata_'+ genNumber +'.txt') as json_file:
        gamedata = json.load(json_file)
    
    pc = []
    i=0
    # load in the pokemon within the player's PC
    for id in gamedata["Pc"]:
        # loads in pokemon object
        pc.append(pokemon[int(id)])

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
                    gamedata["pokeballs"])


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
    saveData["pokeballs"] = player.getItems()

    print("Saved Successfully")
    with open('gamesaves/gamedata_' + genNumber + '.txt', 'w') as outfile:  
        json.dump(saveData, outfile, indent=1)
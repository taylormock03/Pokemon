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
    party=[]
    indexOffset=0
    for x in gamedata["party"]:
        if x == "":
            pass
        else:
            party.append(pc[x+indexOffset])
            pc.pop(x+indexOffset)
            indexOffset-=1

    return Player(  party,
                    pc,
                    location[gamedata["CurrentLocation"]],
                    gamedata["BattleWon"],
                    gamedata["money"],
                    gamedata["pokeballs"])

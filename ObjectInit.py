class Pokemon:
    name =""
    __type1 = ""
    __type2 = ""
    __hp = 0
    __attack = 0
    __defence = 0 
    __speed = 0
    __status = ""
    __moveset = []
    
    __nextEvolve = []
    __xp = 0
    __level = 1

    # NOTE: nextEvolve, moveset, learnsets, xp, and level are not included in this constructor
    # this is because next evolve won't work until all pokemon are already loaded
    # and the moveset, xp and levels are generated at the time of an encounter
    # the learnsets don't have a fixed length, so it makes it easier to add through a seperate method

    def __init__(self, name, type1,type2,hp,attack,defence,speed):
        self.name = name
        self.__type1 = type1
        self.__type2 = type2
        self.__hp = hp
        self.__attack = attack
        self.__defence = defence
        self.__speed = speed
        self.learnsets = []
        return

    def addLearnset(self,move):
        self.learnsets.append(move)
        return

class Move:
    name = ""
    __accuracy = 0
    __damage = 0
    __type = ""

    ##Currently no data exists in the generation files. This will hopefully be rectified, but not yet
    __status = None

    def __init__(self, name, accuracy, damage, type):
        self.name = name
        self.__damage = damage
        self.__accuracy = accuracy
        self.__type = type
        return

class Location:
    name = ""
    gym = ""
    locationPokemon = []

class GymTrainer:
    pokemon = []

def loadPokemon(data,moves):
    pokeList = []
    i = 0
    for x in data["pokemon"]:
        pokeList.append(Pokemon(x, 
                            data["type_1"][i],
                            data["type_2"][i],
                            data["HP"][i],
                            data["attack"][i],
                            data["defence"][i],
                            data["speed"][i],
                            ))
        try:
            learnset = data["learnsets"][i].split("-")
        except:
            print(pokeList[i-1].name + pokeList[i-1].learnsets[0].name)
        for y in learnset:
            try:
                pokeList[i].addLearnset(moves[int(y)])
            except:
                print("Pokemon that fucked up: " + pokeList[i].name)
                break
        i+=1
    return pokeList


##This will initialise all the moves from the generation text file
def loadMoves(data):
    moveList = []
    i = 0
    for x in data["moveset"]:
        moveList.append(Move(x, 
                            data["accuracy"][i],
                            data["damage"][i],
                            data["typeMove"][i]
                            ))
        i+=1
    return moveList

def loadGym(data,pokemon):
    trainers = []
    return trainers

def loadLocations(data,gyms,pokemon):
    locations = []
    return locations

def loadAll(data):
    moves = loadMoves(data)
    pokemon = loadPokemon(data,moves)
    gyms = loadGym(data,pokemon)
    locations = loadLocations(data,gyms,pokemon)
    foo =""
    return pokemon,locations
    
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
    __learnsets = []
    __nextEvolve = []
    __xp = 0
    __level = 1

class Moves:
    name = ""
    __accuracy = 0
    __damage = 0
    __type = ""
    __status = None

class Locations:
    name = ""
    gym = ""
    locationPokemon = []

class GymTrainer:
    pokemon = []

def loadPokemon(data,moves):
    pokeList = []
    return pokeList

def loadMoves(data):
    moveList = []
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
    
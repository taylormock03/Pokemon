import numpy as np
from random import randint

class Pokemon:
    id=0
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

    # Health is calculated as a function of the base HP and level
    # This variable will store the health of the pokemon
    # this applies to all stats
    __battleHealth = 0
    __battleAttack = 0
    __battleDefence = 0
    __battleSpeed = 0
    # NOTE: moveset, xp, and level are not included in this constructor
    # this is because next evolve won't work until all pokemon are already loaded
    # and the moveset, xp and levels are generated at the time of an encounter
    # the learnsets don't have a fixed length, so it makes it easier to add through a seperate method
    # during initial loading, learnsets and next evolve will be blank, but will be passed a value
    # when creating a clone

    def __init__(self, name, type1,type2,hp,attack,defence,speed,id,learnsets,nextEvolve):
        self.name = name
        self.__type1 = type1
        self.__type2 = type2
        self.__hp = hp
        self.__attack = attack
        self.__defence = defence
        self.__speed = speed
        self.learnsets = learnsets
        self.__moveset = []
        self.__nextEvolve = nextEvolve
        self.id=id
        self.__level = 1
        self.__battleHealth = 0
        self.__battleAttack = 0
        self.__battleDefence = 0
        self.__battleSpeed = 0
        return

    # Because the pokemon exist as templates on a list, I need to create new pokemon objects with the same data
    # This function will pass all of the data
    def clone(self):
        return self.name,self.__type1,self.__type2,self.__hp,self.__attack,self.__defence,self.__speed,self.id,self.learnsets,self.__nextEvolve

    def addLearnset(self,move):
        self.learnsets.append(move)
        return

    def setNextEvolve(self,evolution):
        evolution.__nextEvolve = self

    def setLevel(self,level):
        self.__level = level

    def getLevel(self):
        return self.__level

    def setXp(self,xp):
        self.__xp = xp

    def getXp(self):
        return self.__xp
    
    # return battle health (note: not HP, these are two seperate values)
    def getHealth(self):
        return self.__battleHealth

    def CalculateStats():
        return

    # This will add a single move based on an id that is passed through
    def setMoves(self,id):
        for move in self.learnsets:
            # if the id passed is equal to the move's id, they are the same move
            if move.id == id:
                name, accuracy, damage, type, id, pp, status = move.clone()
                newMove= Move(name, accuracy, damage, type, id, pp, status)
                self.__moveset.append(move)
                break
    
    # This will be used to set up a pokemon's initial moveset (this pretty much
    # is only used when a pokemon does not have any moves such as at the beginning
    # of the game with the starter pokemon)
    
    def setInitMoves(self):
        i=0
        while len(self.__moveset)<4:
            self.__moveset.append(self.learnsets[i])
            i+=1
        

    def getMoves(self):
        return self.__moveset

    # Prints out the pokemon and its stats 
    # can be used as str(foo) where foo is a pokemon object
    def __str__(self):
        return ("Pokemon: " + self.name + " Lvl: " + str(self.__level) + "\n    Type 1: " + self.__type1 + "\n    Type 2: " + self.__type2)
        
    # calculates the Health and PP of the pokemon for battles
    def battleInit(self):
        ev = 181
        iv = 24
        # this calculation comes from bulbapedia
        self.__battleHealth = round((((2*self.__hp)+ iv + (ev/4))/100)+self.__level+10)

        self.__battleAttack = round(((((2*self.__attack)+ iv + (ev/4)) * self.__level)/100 )+5 )
        self.__battleDefence = round(((((2*self.__defence)+ iv + (ev/4)) * self.__level)/100 )+5)
        self.__battleSpeed = round(((((2*self.__speed)+ iv + (ev/4)) * self.__level)/100 )+5)

        for x in self.__moveset:
            x.battleInit()

    # This will give the pokemon 4 random moves from within its learnsets
    def randomMoves(self):
        i=0
        while i<4:
            # Chooses a random move within learnsets
            movePos = randint(0,len(self.learnsets))
            
            # clones it here so a new instance of each move can be istantiated
            name, accuracy, damage, type, id, pp, status =self.learnsets[movePos].clone()
            newMove = Move(name, accuracy, damage, type, id, pp, status)
            
            # adds it to the moveset
            self.__moveset.append(newMove)
            i+=1

class Move:
    name = ""
    id=0
    __accuracy = 0
    __damage = 0
    __type = ""
    __pp = 0

    # The __pp variable shows the base stat (the maximum number of uses)
    # but the battlePp variable will decrement each fight and be reset at 
    # the beginning of a new fight
    __battlePp=0

    # This stores if this move does anything special e.g burn the target, heal user, etc.
    __status = None

    def __init__(self, name, accuracy, damage, type,id,pp,status):
        self.name = name
        self.__damage = damage
        self.__accuracy = accuracy
        self.__type = type
        self.__pp = pp
        self.id=id
        self.__battlePp = 0
        self.__status = status
        return

    # returns the data within the object so a new move can be created (see pokemon.clone())
    def clone(self):
        return self.name, self.__accuracy, self.__damage, self.__type,self.id,self.__pp,self.__status

    # sets PP of moves
    def battleInit(self):
        self.__battlePp = self.__pp

class Location:
    name = ""
    gym = ""
    locationPokemon = []
    id = ''

    def __init__(self, name, gym, locationPokemon,id):
        self.name = name
        self.gym = gym
        self.locationPokemon = locationPokemon
        self.id = id

    def __str__(self):
        string = "\nYou are in: " + self.name + '\nYou can catch:'

        printedPokemon = []
        for x in self.locationPokemon:
            if x not in printedPokemon:
                string+=("\n" + str(x))
                printedPokemon.append(x)
        return string

    def getEncounter(self):
        randomIndex = randint(0,len(self.locationPokemon)-1)
        return self.locationPokemon[randomIndex]

class GymTrainer:
    
    def __init__(self,pokemon):
        self.pokemon = pokemon
        
    # This will set up all the battle stats for the gym leader
    def battleInit(self):
        for x in self.pokemon:
            x.randomMoves()
            x.battleInit()


def loadPokemon(data,moves):
    pokeList = []
    i = 0
    for x in data["pokemon"]:
        try:
            pokeList.append(Pokemon(x, 
                                data["PokemonType"][str(i)][0],
                                data["PokemonType"][str(i)][1],
                                data["HP"][i],
                                data["attack"][i],
                                data["defence"][i],
                                data["speed"][i],
                                i,
                                learnsets=[],
                                nextEvolve=[]
                                ))
            try:
                learnset = data["learnsets"][str(i)]
                for y in learnset:
                    pokeList[i].addLearnset(moves[int(y)])
            except:
                m=1
            i+=1
        
        except:
            break
    # This is where the next evolve will be added in. This had to be added last
    # as the next evolution would not have been created when we were initially 
    # creating the objects
    index=0
    for x in data["next_evolve"]:
        if not np.isnan(x):
            pokeList[index].setNextEvolve(pokeList[int(x)])
        index+=1


    return pokeList


##This will initialise all the moves from the generation text file
def loadMoves(data):
    moveList = []
    i = 0
    for x in data["moveset"]:
        moveList.append(Move(x, 
                            data["accuracy"][i],
                            data["damage"][i],
                            data["typeMove"][i],
                            i,
                            data["pp"][i],
                            data["moveEffect"][i]
                            ))
        i+=1
    return moveList

def loadGym(data,pokemon):
    gyms = []
    
    i=0
    for x in data["TrainerPokemon"]:
        lineUp = []
        for PokeId in data["TrainerPokemon"][x]:
            if not np.isnan(PokeId):
                name, type1, type2, hp, attack, defence, speed, id, learnsets, nextEvolve =pokemon[int(PokeId)-1].clone()
                newPokemon = Pokemon(name, type1, type2, hp, attack, defence, speed, id, learnsets, nextEvolve)
                lineUp.append(newPokemon)

        levels = data["TrainerLevel"][i].split("-")
        y=0
        for x in lineUp:
            x.setLevel(int(levels[y]))
            y+=1
        
        gyms.append(GymTrainer(lineUp))
        i+=1
    return gyms

def loadLocations(data,gyms,pokemon):
    locations = []
    i=0
    for x in data["LocationPokemon"]:
        locationPokemonId=data["LocationPokemon"][x]
        locationPokemon =[]
        for id in locationPokemonId:
            locationPokemon.append(pokemon[int(id)])
        locations.append(Location(
                                    x,
                                    gyms[i],
                                    locationPokemon,
                                    i
        ))
        i+=1

    return locations

def loadAll(data):
    moves = loadMoves(data)
    pokemon = loadPokemon(data,moves)
    gyms = loadGym(data,pokemon)
    locations = loadLocations(data,gyms,pokemon)
    return pokemon,locations
    
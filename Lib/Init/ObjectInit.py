import numpy as np
from random import randint
import math

class Pokemon:
    id=0
    name =""
    __type1 = ""
    __type2 = ""
    __hp = 0
    __attack = 0
    __defence = 0 
    __speed = 0
    status = ""
    __moveset = []
    __nextEvolve = []
    __xp = 0
    __level = 1

    # Health is calculated as a function of the base HP and level
    # This variable will store the health of the pokemon
    # this applies to all stats
    battleHealth = 0
    battleAttack = 0
    battleDefence = 0
    battleSpeed = 0
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
        self.battleHealth = 0
        self.battleAttack = 0
        self.battleDefence = 0
        self.battleSpeed = 0
        self.status = ""
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

    def getAttack(self):
        return self.__attack

    def getDefence(self):
        return self.__defence

    def getTypes(self):
        return[self.__type1,self.__type2]

    def addXp(self,xp):
        self.__xp += xp

    def getXp(self):
        return self.__xp
    
    # return battle health (note: not HP, these are two seperate values)
    def getHealth(self):
        return self.battleHealth

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
        self.battleHealth = round((((2*self.__hp)+ iv + (ev/4))/100)+self.__level+10)

        self.battleAttack = round(((((2*self.__attack)+ iv + (ev/4)) * self.__level)/100 )+5 )
        self.battleDefence = round(((((2*self.__defence)+ iv + (ev/4)) * self.__level)/100 )+5)
        self.battleSpeed = round(((((2*self.__speed)+ iv + (ev/4)) * self.__level)/100 )+5)

        # This is to stop you from healing above your maximum health
        self.maxHealth = self.battleHealth

        # reset statuses
        self.status = ""
        for x in self.__moveset:
            x.battleInit()

    # This will give the pokemon 4 random moves from within its learnsets
    def randomMoves(self):
        i=0
        while i<4:
            # Chooses a random move within learnsets
            movePos = randint(0,len(self.learnsets)-1)
            
            # clones it here so a new instance of each move can be istantiated
            name, accuracy, damage, type, id, pp, status =self.learnsets[movePos].clone()
            newMove = Move(name, accuracy, damage, type, id, pp, status)
            
            # adds it to the moveset
            self.__moveset.append(newMove)
            i+=1

    # Calculates whether the pokemon should level up and what should happen
    def levelCheck(self):
        newLevel = math.floor(self.__xp**(1/3))
        oldLevel = self.__level
        if newLevel>oldLevel:
            self.setLevel(newLevel)
            print(self.name + " levels up to lvl " + str(newLevel))

            for x in range(oldLevel+1, newLevel+1):
                # every 2 levels, a pokemon can learn a new move
                if x % 2 == 0:
                    self.learnMove()

                # every 25 levels, a pokemon can evolve (if it has something to evolve into) 
                if x % 25 == 0:
                    self.evolve()

    def learnMove(self):
        randomMove = self.learnsets[randint(0,len(self.learnsets)-1)]
        print("\n" + self.name + " wants to learn: " + str(randomMove))
        selection =""
        while selection != "yes" and selection != "no":
            selection = input("Would you like to learn this move?\n>")
        
        if selection =="yes":
            name, accuracy, damage, type, id, pp, status =randomMove.clone()
            newMove = Move(name, accuracy, damage, type, id, pp, status)

            print("What move would you like to forget?\n")
            i=1
            for x in self.__moveset:
                print("#" + str(i)+" " + str(x))
                i+=1
            
            while True:
                try:
                    selection = int(input(">"))-1
                    if selection <0 or selection >4:
                        raise
                    break
                except:
                    print("Invalid input")

            print(self.name + " forgot " + self.__moveset[selection].name + " and learned " + newMove.name )
            self.__moveset[selection] = newMove

    def evolve(self):
        if self.__nextEvolve != []:
            name, type1, type2, hp, attack, defence, speed, id, learnsets, nextEvolve =self.__nextEvolve[0].clone()

            self.name = name
            self.__type1 = type1
            self.__type2 = type2
            self.__hp = hp
            self.__attack = attack
            self.__defence = defence
            self.__speed = speed
            self.id = id
            self.learnsets = learnsets
            self.__nextEvolve = nextEvolve


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

    def __str__(self):
        return ("Name: " + self.name + "\nAccuracy: " + str(self.__accuracy) + "\nDamage: " + str(self.__damage) + "\nType: " + self.__type + "\nPP: " + str(self.__battlePp) + "\nSpecial Effect: " + self.__status + "\n")

    # calculates the move's effects. if it returns false, it means that the move can't be done
    def attack(self,userPokemon,targetPokemon):
        if self.__battlePp<0:
            print("You have insufficient PP to use this move")
            return False

        self.__battlePp -=1

        print(userPokemon.name + " uses " + self.name)
        
        # Calculate whether move will hit or not
        moveHit = randint(0,100) <self.__accuracy
        if not moveHit and not np.isnan(self.__accuracy) :
            print(userPokemon.name + " missed")
            return True

        # Calculate move's special effects
        if self.__status in ["Sleep", "Poison", "Burn", "Freeze", "Paralysis", "Confuse"]:
            self.inflictStatus(self.__status,targetPokemon)
        
        elif self.__status == "Self-Destruct":
            self.selfDestruct(userPokemon)

        elif self.__status == "AttackUp":
            self.attackUp(userPokemon)

        elif self.__status == "DefenceUp":
            self.defenceUp(userPokemon)

        elif self.__status == "SpeedUp":
            self.speedUp(userPokemon)

        elif self.__status == "AttackDown":
            self.attackDown(targetPokemon)

        elif self.__status == "DefenceDown":
            self.defenceDown(targetPokemon)

        elif self.__status == "SpeedDown":
            self.speedDown(targetPokemon)

        elif self.__status == "Heal":
            self.heal(userPokemon)

        elif self.__status == "Drain":
            self.drain(userPokemon,targetPokemon)

        elif self.__status == "Recoil":
            self.recoil(userPokemon,targetPokemon)

        

        # Calculate the damage dealt to the target pokemon
        damage = self.damageCalculation(userPokemon,targetPokemon)
        
        if np.isnan(damage):
            damage = 0
        
        damage = round(damage)

        if userPokemon.status in ["Sleep","Paralysis"]:
            if randint(1,3) == 1:
                print(userPokemon.name + " is no longer suffering from " + userPokemon.status)
                userPokemon.status = ""
            else:
                print(userPokemon.name + " couldn't attack due to " + userPokemon.status)
                return True
            
        elif userPokemon.status == "Confusion":
            randomNumber = randint(1,3)
            if randomNumber == 1:
                print(userPokemon.name + " hurt itself " + str(round(damage) + " HP in its confusion"))
                return True

            randomNumber = randint(1,3)
            if randomNumber == 1:
                print(userPokemon.name + " is no longer suffering from " + userPokemon.status)
                userPokemon.status = ""

        print(targetPokemon.name + " took " + str(round(damage)) +" damage") 
        targetPokemon.battleHealth -= round(damage)
        return True

    # This will calculate how much hp the target pokemon should lose
    def damageCalculation(self,userPokemon,targetPokemon):
        try:
            damage = (((((((2*userPokemon.getLevel()/5)+2)* userPokemon.getAttack()*self.__damage)/targetPokemon.getDefence())/50)+2)*self.typeCalculation(targetPokemon))*randint(217,255)/255
            return damage
        except:
            return 0

    # This calculates whether a move is effective or not e.g fire is not effective against water types 
    def typeCalculation(self,targetPokemon):
        targetTypes = targetPokemon.getTypes()
        # This is where the type matchups are stored
        typeChart = {"normal":{   "weak":["rock"],
                                "strong":[],
                                "noeffect":["ghost"]    
                            },
                    "fire":{   "weak":["fire","water","rock","dragon"],
                                "strong":["grass","ice","bug","steel"],
                                "noeffect":[]    
                            },
                    "qater":{   "weak":["water","grass","dragon"],
                                "strong":["fire","ground","rock"],
                                "noeffect":[]    
                            },
                    "electric":{   "weak":["electric","grass","dragon"],
                                "strong":["water","flying"],
                                "noeffect":["ground"]    
                            },
                    "grass":{   "weak":["fire","grass","poison","flying","bug","dragon","steel"],
                                "strong":["water","ground","rock",],
                                "noeffect":[]    
                            },
                    "ice":{   "weak":["fire","water","ice","steel"],
                                "strong":["grass","ground","fly","dragon"],
                                "noeffect":[]    
                            },
                    "fighting":{   "weak":["poison","fly","psychic","bug","fairy"],
                                "strong":["normal","ice","rock","dark","steel"],
                                "noeffect":["ghost"]    
                            },
                    "poison":{   "weak":["poison","ground","rock","ghost"],
                                "strong":["grass","fairy"],
                                "noeffect":["steel"]    
                            },
                    "ground":{   "weak":["grass","bug"],
                                "strong":["fire","electric","poison","rock","steel"],
                                "noeffect":["flying"]    
                            },
                    "flying":{   "weak":["electric","rock","steel"],
                                "strong":["grass","fighting","bug"],
                                "noeffect":[]    
                            },
                    "psychic":{   "weak":["psychic","steel"],
                                "strong":["fighting","ground"],
                                "noeffect":["dark"]    
                            },
                    "bug":{   "weak":["fire","fighting","poison","flying"],
                                "strong":["grass","psychic","dark"],
                                "noeffect":[]    
                            },
                    "rock":{   "weak":["fighting","ground","steel"],
                                "strong":["fire","ice","flying","bug"],
                                "noeffect":[]    
                            },
                    "ghost":{   "weak":["dark"],
                                "strong":["psychic","ghost"],
                                "noeffect":["normal"]    
                            },
                    "dragon":{   "weak":["steel"],
                                "strong":["dragon"],
                                "noeffect":["fairy"]    
                            },
                    "dark":{   "weak":["fighting","dark","fairy"],
                                "strong":["psychic","ghost"],
                                "noeffect":[]    
                            },
                    "steel":{   "weak":["fire","water","electric","steel"],
                                "strong":["ice","rock","fairy"],
                                "noeffect":[]    
                            },
                    "fairy":{   "weak":["fire","poison","steel"],
                                "strong":["fighting","dragon","dark"],
                                "noeffect":[]    
                            }
        }

        for x in targetTypes:
            check = (typeChart[self.__type]['weak']) 
            if x in check:
                print("It was not very effective")
                return 0.5

            check = typeChart[self.__type]['noeffect']
            if x in check:
                print("It had no effect")
                return 0

            check = typeChart[self.__type]['strong']
            if x in check:
                print("It was super effective")
                return 2

        else: 
            return 1

    # will calculate whether a status effect (burn, paralysis, etc.) should be applied
    def inflictStatus(self,status,targetPokemon):
        randomNumber = randint(1,3)
        # This gives a 33% chance of inflicting a status onto the targetPokemon 
        if randomNumber == 3:
            print(targetPokemon.name + " now suffers from " + status)
            targetPokemon.status = status
        
        else:
            print(targetPokemon.name + " doesn't suffer from " + status)

    def selfDestruct (self,userPokemon):
        userPokemon.battleHealth = 0

    def attackUp(self,userPokemon):
        userPokemon.battleAttack *=1.1
        print(userPokemon.name + "'s attack rose")

    def defenceUp(self,userPokemon):
        userPokemon.battleDefence *=1.1
        print(userPokemon.name + "'s defence rose")

    def speedUp(self,userPokemon):
        userPokemon.battleSpeed *=1.1
        print(userPokemon.name + "'s speed rose")

    def attackDown(self,targetPokemon):
        targetPokemon.battleAttack *=0.9
        print(targetPokemon.name + "'s attack fell")

    def defenceDown(self,targetPokemon):
        targetPokemon.battleDefence *=0.9
        print(targetPokemon.name + "'s defence fell")

    def speedDown(self,targetPokemon):
        targetPokemon.battleSpeed *=0.9
        print(targetPokemon.name + "'s speed fell")

    # Heals 30% of max HP
    def heal(self,userPokemon):
        userPokemon.battleHealth += round(userPokemon.maxHealth*0.3)

        print(userPokemon.name +" healed " + str(round(userPokemon.maxHealth*0.3)) + " HP")
        if userPokemon.battleHealth> userPokemon.maxHealth:
            userPokemon.battleHealth = userPokemon.maxHealth

    # Heals 50% of damage dealt to target pokemon
    def drain(self,userPokemon,targetPokemon):
        damage = self.damageCalculation(userPokemon,targetPokemon)

        print(userPokemon.name +" healed " + str(round(userPokemon.maxHealth*0.5)) + " HP")
        userPokemon.battleHealth += round(damage *0.5)
        if userPokemon.battleHealth> userPokemon.maxHealth:
            userPokemon.battleHealth = userPokemon.maxHealth

    # Damages user by 25% of damage dealt to target pokemon
    def recoil(self,userPokemon,targetPokemon):
        damage = self.damageCalculation(userPokemon,targetPokemon)
        print(userPokemon.name + " hurt itself " + str(round(damage*0.25)) + " HP in recoil")
        userPokemon.battleHealth -= round(damage *0.25)



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
    
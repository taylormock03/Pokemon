import pandas as pd
import numpy as np
import json

xls = pd.ExcelFile('pokemon.xlsx')

Pokemon_stats = pd.read_excel(xls,"pokemon")
moves =  pd.read_excel(xls,"Moves")
Next_evolve =  pd.read_excel(xls,"Evolution")
Learn_sets = pd.read_excel(xls,"Learnsets")
Pokemon_Types = pd.read_excel(xls,"Pokemon Types")
Pokemon_Locations = pd.read_excel(xls,"Locations")
Gym_Pokemon = pd.read_excel(xls,"Gym-Locations")

xls = None

PokeNames = Pokemon_stats["Name"].tolist()
HP = Pokemon_stats["HP"].tolist()
Attack = Pokemon_stats["attack"].tolist()
Defence = Pokemon_stats["Defence"].tolist()
Speed = Pokemon_stats["Speed"].tolist()
MoveIds = moves["id"].tolist()
i=0
for x in MoveIds:
    MoveIds[i]=x-1
    i+=1

MoveNames = moves["identifier"].tolist()
MoveTypes = moves["Type_move"].tolist()
MovePower = moves["power"].tolist()
MovePP = moves["pp"].tolist()
MoveAccuracy = moves["accuracy"].tolist()
EvolveFrom =Next_evolve["evolves_from_species_id"].tolist()

i=0
for x in EvolveFrom:
    EvolveFrom[i]=x-1
    i+=1

locations={}
previousLocation = ""
for index,row in Pokemon_Locations.iterrows():
    if np.isnan(row["Poke_ID"]):
        previousLocation = row["Pokemon"]
        locations[previousLocation]=[]
    else:
        locations[previousLocation].append(row["Poke_ID"]-1)

learnsets={}
for index,row in Learn_sets.iterrows():
    #print(row["pokemon_id"],row["move_id"])
    if index ==0:
        pass
    if int(row[0]-1)>720:
        row[0]=row[0]-9280 
    try:
        learnsets[row[0]-1].append(row[1]-1)
    except:
        learnsets[row[0]-1] = [row[1]-1]

Gyms ={}
i=0
for index,row in Gym_Pokemon.iterrows():
    Gyms[i]=[]
    for x in range(0,6):
        Gyms[i].append(row[x])

    i+=1

pokeTypes ={}
previousSlot = -1
for index,row in Pokemon_Types.iterrows():
    if int(row[0]-1)>720:
        row[0]=row[0]-9280 

    if row["slot"] == previousSlot:
        pokeTypes[previousId].append("None")
    
    previousSlot = row["slot"]
    previousId = row["pokemon_id"]-1
    if previousSlot == 1:
        pokeTypes[row["pokemon_id"]-1] = [row["Type_name"]]

    else:
        pokeTypes[row["pokemon_id"]-1].append(row["Type_name"])
    

with open('Generations/Generation_6.txt') as json_file:
                Generation = json.load(json_file)   

Generation["moveset"] = MoveNames
Generation["typeMove"] = MoveTypes
Generation["TrainerPokemon"] = Gyms
Generation["LocationPokemon"] = locations
Generation["learnsets"] = learnsets
Generation["accuracy"] = MoveAccuracy
Generation["damage"] = MovePower
Generation["pp"] = MovePP
Generation["speed"] = Speed
Generation["defence"] = Defence
Generation["attack"] = Attack
Generation["HP"] = HP
Generation["next_evolve"] = EvolveFrom
Generation["PokemonType"] = pokeTypes
Generation["pokemon"] = PokeNames

'''
Generation.pop("location")
Generation.pop("Ai_health")
Generation.pop("Player_health")
Generation.pop("type_1")
Generation.pop("type_2")
'''
with open('Generations/Generation_6.txt', 'w') as outfile:  
        json.dump(Generation, outfile, indent=1)
print ("test")


import json
from pprint import pprint
from random import randint
import math
from enum import Enum

print("test")
## Variable set up
global Generation_Number

#Generation pokemon
global Generation

##gamesaves
gamedata={}
gamedata["party"] = ["","","","","",""]
gamedata["Pc"]=[]
gamedata["PcLevel"]=[]
gamedata["CurrentLocation"] = 0
gamedata["PcMoves"] = []
gamedata["BattleWon"]=0
gamedata["money"]=0
gamedata["pokeballs"] = 0
gamedata["xp"] = []


def firstload():
    global Generation_Number
    while True:
        Generation_Number = input("Which generation would you like to play?")
        if not Generation_Number.isdigit():
            print("invalid response")
        else:
            global Generation
            with open('Generations/Generation_'+ Generation_Number +'.txt') as json_file:
                Generation = json.load(json_file)            
            
            start=input("Do you want to load a game? ")
            if start == "yes":
                load()
                break
            elif start =="no":
                if input("Are you sure? This will permanently delete all previous data ") =="yes":
                    starter()
                    break
                else:
                    print("")
            else:
                print("invalid response")

## Load Gamesave
def load():
    global Generation_Number
    global gamedata
    with open('gamesaves/gamedata_'+ Generation_Number +'.txt') as json_file:
        gamedata = json.load(json_file)

    print("Loaded successfully")

## Save Gamesave
def save():
    global Generation_Number
    with open('gamesaves/gamedata_' + Generation_Number + '.txt', 'w') as outfile:  
        json.dump(gamedata, outfile, indent=1)

    print("Saved successfully")

def starter():
    global PcLevel
    print("")
    print("Welcome to the world of Pokemon. Today you will be given a choice of your first pokemon. Here are your choices")

    print("#1 " + Generation["pokemon"][Generation["Starter1"][0]] + " Type: " + Generation["type_1"][Generation["Starter1"][0]] +" " + Generation["type_2"][Generation["Starter1"][0]])
    print("#2 " + Generation["pokemon"][Generation["Starter2"][0]] + " Type: " + Generation["type_1"][Generation["Starter2"][0]] + " " + Generation["type_2"][Generation["Starter2"][0]])
    print("#3 " + Generation["pokemon"][Generation["Starter3"][0]] + " Type: " + Generation["type_1"][Generation["Starter3"][0]] + " " + Generation["type_2"][Generation["Starter3"][0]])
    while True:
        starter = input("which number pokemon would you like ")
        if starter == "1":
            gamedata["Pc"].append(Generation["Starter1"][0])
            gamedata["party"][0]=0
            gamedata["PcLevel"].append(1)
            print(Generation["pokemon"][gamedata["Pc"][0]]+ " a great choice!")
            temp1=Generation["learnsets"][0].split("-")
            gamedata["PcMoves"].append(temp1[0]+"-"+temp1[1])
            gamedata["xp"].append(0)
            break

        elif starter == "2":
            gamedata["Pc"].append(Generation["Starter2"][0])
            gamedata["party"][0]=0
            gamedata["PcLevel"].append(1)
            print(Generation["pokemon"][gamedata["Pc"][0]]+ " a great choice!")
            temp1=Generation["learnsets"][3].split("-")
            gamedata["PcMoves"].append(temp1[0]+"-"+temp1[1])    
            gamedata["xp"].append(0)        
            break

        elif starter == "3":
            gamedata["Pc"].append(Generation["Starter3"][0])
            gamedata["party"][0]=0
            gamedata["PcLevel"].append(1)
            print(Generation["pokemon"][gamedata["Pc"][0]]+ " a great choice!")
            temp1=Generation["learnsets"][6].split("-")
            gamedata["PcMoves"].append(temp1[0]+"-"+temp1[1])
            gamedata["xp"].append(0)
            break
    print("With your new pokemon you are free to go into the wild. Remember, if you are ever lost just yell HELP")

def buy():
    print("")
    quit =""
    while quit !="yes":
        game = input("What would you like to buy? (pokemon or pokeball) ")
        
        ##Pokeball purchasing
        if game == "pokeball":
            while True:
                buyamount=input("How many pokeballs would you like to buy ")
                if buyamount.isalpha():
                    print("Invalid response")

                elif int(buyamount)*200> gamedata["money"]:
                    print("insufficient funds")

                elif int(buyamount)<0:
                    print("You can not buy negative pokeballs. That's not how this works")

                else:
                    gamedata["money"]-=int(buyamount)*200
                    gamedata["pokeballs"]+=int(buyamount)
                    print(buyamount+" pokeballs bought for $" + str(int(buyamount)*200))
                    break
            break

        ##Pokemon purchasing
        elif game == "pokemon":
            quit = ""
            while quit != "yes":
                selected_pokemon = input("Which pokemon would you like? ")
                
                i=0
                for x in Generation["pokemon"]:
                    if selected_pokemon.lower() == x.lower():
                        Pokemon= Generation["pokemon"][i]
                        pokeid = i
                        
                        print()
                        
                        level_pokemon = int(input("What level would you like? ")) 

                        print()

                        available_moves = Generation["learnsets"][i].split("-")

                        ##global Generation
                        attack1 = round(Generation["attack"][i]*2 + level_pokemon/100+5+10)
                        health1 = round(Generation["HP"][i]*2+level_pokemon/100+level_pokemon+10)
                        speed1 = round(Generation["speed"][i]*2 + level_pokemon/100+5+10)
                        defence1 = round(Generation["defence"][i]*2 + level_pokemon/100+5+10)

                        print()

                        print(Pokemon + " Attack: " + str(attack1) + " HP " + str(health1) + " Speed: " + str(speed1) + " Defence " + str(defence1))
                        print(Pokemon + " Knows:")

                        pokemon_moves= ""
                        i=0
                        while i<4:
                            print(Generation["moveset"][int(available_moves[i])])
                            pokemon_moves+=str(available_moves[i]) + "-"
                            i+=1


                        cost = 50* level_pokemon
                        buy = input(Pokemon + " Costs $" + str(cost) + ". Would you still like to buy it? ")

                        while True:
                            
                            if buy =="yes":
                                if gamedata["money"]>=cost:
                                    gamedata["Pc"].append(pokeid)
                                    gamedata["money"] -= cost
                                    gamedata["PcLevel"].append(level_pokemon)
                                    gamedata["xp"].append(level_pokemon*250)
                                    gamedata["PcMoves"].append(pokemon_moves[:-1])
                                    print(Pokemon + "Bought for " + str(cost))
                                    break
                                else:
                                    print("insufficient funds")
                                    buy = input(Pokemon + " Costs $" + str(cost) + ". Would you still like to buy it? ")

                            elif buy == "no":
                                break

                            else:
                                buy = input(Pokemon + " Costs $" + str(cost) + ". Would you still like to buy it? ")

                        break
                    i+=1
                
                while True:
                    quit = input("Would you like to leave? ")
                    if quit == "yes" or quit =="no":
                        break

                    else:
                        print("invalid response")


    print("")

def LocationFind():
    temp2=[]
    print("")
    temp1=Generation["LocationPokemon"][gamedata["CurrentLocation"]].split("-")
    for x in temp1:
        temp2.append(Generation["pokemon"][int(x)])
    print("Current Location: " + Generation["location"][gamedata["CurrentLocation"]])
    print("")
    print("Here you can find:")
    for x in temp2:
        print(x)
    print("")

    game = input("Would you like to travel? ")
    if game == "yes":
        i=0
        for x in Generation["location"]:
            print("#" + str(i)+":" + x)
            i+=1
        game = int(input("Where would you like to travel? (int only)" ))
        if gamedata["BattleWon"] >= game:
            gamedata["CurrentLocation"] = game
            print("You travelled to " + Generation["location"][gamedata["CurrentLocation"]])
            print("")
        else: 
            print("You have not yet won enough gym battles to get there yet. ")
            print("")

    else:
        print("")

def debug():
    print(Generation)

def Party():
    print("")
    i=0
    for x in gamedata["party"]:
        if x != "":
            temp = gamedata["Pc"][x]
            print("#" +str(i))
            print ("Pokemon: " + Generation["pokemon"][temp]) 
            print("Level: " + str(gamedata["PcLevel"][x]))
            print("Type: " + Generation["type_1"][temp] + " " + Generation["type_2"][temp])
            
            temp2 = gamedata["PcMoves"][x].split("-")
            for z in temp2:
                print("Move learnt: " + Generation["moveset"][int(z)])

            print("")
            i+=1

def PartyOrder():
    Party()
    Pokemon1 = input("What is your first pokemon you want to swap out?")
    Pokemon2 = input("What is your second pokemon you want to swap out?")

    Party1 = gamedata["party"][int(Pokemon1)] 
    Party2 = gamedata["party"][int(Pokemon2)]

    gamedata["party"][int(Pokemon1)] = Party2
    gamedata["party"][int(Pokemon2)] = Party1

    print("successfully swapped pokemon!")

def pc():
    print("")
    i=0
    print("Party:")
    Party()
    
    print("PC:")
    print("")
    
    for x in gamedata["Pc"]:
        print("#"+str(i))
        print('pokemon: ' + Generation["pokemon"][x])
        print('Level: ' + str(gamedata["PcLevel"][i]))
        print("Type: " + Generation["type_1"][x] + " " + Generation["type_2"][x])
        temp = gamedata["PcMoves"][i].split("-")
        for z in temp:
            print("Move learnt: " + Generation["moveset"][int(z)])
        i+=1
        print("")

    print("")
    while True:
        game = int(input("Which party pokemon would you like to switch out? "))
        print("")
        
        if game <= -1:
            break

        game2 = int(input("Which PC pokemon would you like to put in? "))
        print("")

        if game2 in gamedata["party"]:
            print("That pokemon is already in the party")
        
        elif game>5:
            print("You can't have that many party pokemon")

        elif game2>len(gamedata["party"]):
            print("Pokemon not found")

        else:
            if gamedata["party"][game]!= "":
                temp = gamedata["party"][game]
                print(Generation["pokemon"][gamedata["Pc"][game2]] + " replaces " + Generation["pokemon"][gamedata["Pc"][temp]])
            gamedata["party"][game] = game2


        print("")
        game = input("would you like to leave?" )
        if game =="yes":
            break
    print("")

def PokeBattle():
    print("")
    temp1 = Generation["LocationPokemon"][gamedata["CurrentLocation"]].split("-")
    x = randint(0,len(temp1)-1)
    
    ##establish Ai stats
    Ai_Pokemon= int(temp1[x])
    Ai_level = randint(math.ceil(0.9*gamedata["PcLevel"][gamedata["party"][0]]), round(1.1*gamedata["PcLevel"][gamedata["party"][0]]))
    Ai_attack = round(Generation["attack"][Ai_Pokemon]*2 + Ai_level/100+5+10)
    Generation["Ai_health"] = round(Generation["HP"][Ai_Pokemon]*2+Ai_level/100+Ai_level+10)
    Ai_speed = round(Generation["speed"][Ai_Pokemon]*2 + Ai_level/100+5+10)
    Ai_defence = round(Generation["defence"][Ai_Pokemon]*2 + Ai_level/100+5+10)
    Ai_evasion = 100
    Ai_moves = []
    Ai_status = ""
    Ai_status_length = 0

    i=0
    temp = Generation["learnsets"][Ai_Pokemon+1].split("-")
    while i<4:
        temp2 =temp[randint(0,len(temp)-1)]
        if temp2 not in Ai_moves:
            Ai_moves.append(temp2)
            i+=1

    ##establish player stats
    currentPokemon = 0
    Generation["Player_health"] = []
    Player_speed = []
    Player_defence = []
    Player_attack = []
    run_attempts = 0
    Player_evasion = 100
    Player_status = ''
    Player_status_length = 0

    i=0
    for x in gamedata["party"]:
        if x!="":
            Generation["Player_health"].append(round(Generation["HP"][gamedata["Pc"][x]]*2 + gamedata["PcLevel"][x]/100+gamedata["PcLevel"][x]+10))
            Player_speed.append(round(Generation["speed"][gamedata["Pc"][x]]*2 + gamedata["PcLevel"][x]/100+5+10))
            Player_defence.append(round(Generation["defence"][gamedata["Pc"][x]]*2 + gamedata["PcLevel"][x]/100+5+10))
            Player_attack.append(round(Generation["attack"][gamedata["Pc"][x]]*2 + gamedata["PcLevel"][x]/100+5+10))


    print("A wild level " + str(Ai_level)+ " " + Generation["pokemon"][Ai_Pokemon] + " appears!")
    print("Go " + Generation["pokemon"][gamedata["Pc"][gamedata["party"][currentPokemon]]] + "!")

    ##start battle
    while True:
        Player_move= -1
        damage_dealt = 0
        Ai_damage_dealt = 0
        switch = False
        escaped = False
        attacked = False
        caught = False
        paralysed = False
        Ai_paralysed = False
        modifier = 0
        A_modifier = 0

        
        ##Player move
        while True:
            print("")
            game = input("What would you like to do? (fight) ")
            print("")
            if game =="help":
                print("Attack - allows you to attack")
                print("Switch - allows you to swap in a new pokemon")
                print("Item - allows you to use a pokeball")
                print("Run - allows you to run away")
                print("Current - shows your currentPokemon")
            
            ##Attack
            elif game == "attack":
                print("")
                print("Moves:")
                moves = gamedata["PcMoves"][gamedata["party"][currentPokemon]].split("-")
                i=0
                for x in moves:
                    print ("#" + str(i) +" " + Generation["moveset"][int(x)] + " Damage: " + str(Generation["damage"][int(x)]) + " Accuracy: " + str(Generation["accuracy"][int(x)]) + " Type: " + Generation["typeMove"][int(x)])
                    i+=1
                game = input("Which attack would you like to do?" )
                if game == "quit":
                    print("")
                elif game.isnumeric:
                    if int(game)<=len(moves)-1:
                        Player_move = int(moves[int(game)])
                        print("You choose " + Generation["moveset"][Player_move])
                        attacked = True
                        print("")
                        break
                    else: 
                        print("invalid response")
                else:
                    print("invalid response")
            
            ##Swap
            elif game == "switch":
                i=0
                for x in gamedata["party"]:
                    if x!="":
                        print("#" +str(i) + " " + Generation["pokemon"][gamedata["Pc"][x]] + " Health: " + str(Generation["Player_health"][i]) + " Type: " + Generation["type_1"][gamedata["Pc"][x]] + " " + Generation["type_2"][gamedata["Pc"][x]])
                        i+=1
            
                game = input("Which pokemon would you like to put in?" )
                if game == "quit":
                    print("")
                elif game.isnumeric:
                    currentPokemon = int(game)
                    print("You choose " + Generation["pokemon"][gamedata["Pc"][gamedata["party"][currentPokemon]]])
                    switch = True
                    break

                else:
                    print("invalid response")

            ##Catch
            elif game == "item":
                if gamedata["pokeballs"]>0:
                    gamedata["pokeballs"]-=1
                    f = round((Generation["HP"][Ai_Pokemon]*2+Ai_level/100+Ai_level+10 * 255 * 4) / (Generation["Ai_health"] * 10))*10
                    M = randint(0,255)
                    if f>=M:
                        print("The wild " + Generation["pokemon"][Ai_Pokemon] + " was caught")
                        gamedata["Pc"].append(Ai_Pokemon)
                        temp = ""
                        for x in Ai_moves:
                            temp+=x + "-"
                        gamedata["PcMoves"].append(temp[:-1])
                        gamedata["PcLevel"].append(Ai_level)
                        caught = True

                    else:
                        print("Pokemon escaped")
                        break

                else:
                    print("You do not have enough pokeballs`")

            ##Run Away
            elif game == "run":
                run_attempts +=1
                F = round((Player_speed[currentPokemon]*32)/(Ai_speed/4) + 30 * run_attempts)
                N = randint(0,255)
                if N<F:
                    print("Escaped successfully")
                    print("")
                    escaped = True
                    break
                else:
                    print("You attempted to run... ")
                    print("Escape failed")
                    break

            ##Show current Generation["pokemon"]
            elif game =="current":
                print(Generation["pokemon"][gamedata["Pc"][gamedata["party"][currentPokemon]]])

            elif game =="stats":
                print(Generation["Ai_health"])

            elif game =="die":
                Generation["Player_health"][currentPokemon] = 0
                attacked = True

            elif game =="kill":
                Generation["Ai_health"] = 0
                attacked = True
                break

        ##Calculate effects
        if Player_status in "healing Sleep poison paralysis":
            if Player_status == "healing":
                Generation["Player_health"][currentPokemon] += round(1/5*Generation["HP"][gamedata["Pc"][currentPokemon]]*2 + gamedata["PcLevel"][currentPokemon]/100+gamedata["PcLevel"][currentPokemon]+10)
                print("Player is healed: " + str(round(1/5*(round(Generation["HP"][gamedata["Pc"][currentPokemon]]*2 + gamedata["PcLevel"][currentPokemon]/100+gamedata["PcLevel"][currentPokemon]+10)))) + "HP")

            elif Player_status == "poison":
                Generation["Player_health"][currentPokemon] -= round(1/16*Generation["HP"][gamedata["Pc"][currentPokemon]]*2 + gamedata["PcLevel"][currentPokemon]/100+gamedata["PcLevel"][currentPokemon]+10)
                print("Player is poisoned: " + str(round(1/16*(round(Generation["HP"][gamedata["Pc"][currentPokemon]]*2 + gamedata["PcLevel"][currentPokemon]/100+gamedata["PcLevel"][currentPokemon]+10)))) + "HP")

            elif Player_status == "Sleep" or Player_status =="paralysis":
                P = randint(0,1)
                if P == 0:
                    print("Player can not move")
                    paralysed=True
            
            ##Reset player statuses
            if Player_status_length>=2:
                Player_status = "None"


        if Ai_status in "healing Sleep poison paralysis":
            if Ai_status == "healing":
                Generation["Ai_health"] += round(1/5*Generation["HP"][Ai_Pokemon]*2 + Ai_level/100+Ai_level+10)
                print("Ai is healed: " + str(round(1/5*Generation["HP"][Ai_Pokemon]*2 + Ai_level/100+Ai_level+10) + "HP"))

            elif Ai_status == "poison":
                Generation["Ai_health"] -= round(1/16*Generation["HP"][Ai_Pokemon]*2 + Ai_level/100+Ai_level+10)
                print("Player is poisoned: " + str(round(1/5*Generation["HP"][Ai_Pokemon]*2 + Ai_level/100+Ai_level+10)) + "HP")

            elif Ai_status == "Sleep" or Ai_status =="paralysis":
                P = randint(0,1)
                if P == 0:
                    print("AI can not move")
                    Ai_paralysed=True

            ##Reset Ai statuses
            
            if Ai_status_length>=2:
                Ai_status = "None"


        ##AI Move
        Ai_turn = int(Ai_moves[randint(0,3)])

        if escaped==True or caught==True:
            break


        elif attacked ==True and paralysed==False:
    
            ##Move effect calculation
        
                ##Check if hits
            P =Generation["accuracy"][Player_move] * (Player_evasion/Ai_evasion)
            hit_chance = randint(0,100)
            if P>=hit_chance:

                ## Regular Moves
                if Generation["moveset"][Player_move] not in ["Hypnosis", "Lovely Kiss", "Sing", "Sleep Powder", "Spore", "Agility", "Double Team", "Teleport", "Recover", "Soft-Boiled", "Haze", "Leech Seed", "Rest", "Substitute", "Acid Armor", "Amnesia", "Barrier", "Conversion", "Defense Curl", "Disable", "Harden", "Withdraw", "Focus Energy", "Growth", "Meditate", "Sharpen", "Swords Dance", "Metronome", "Transform", "Mimic", "Mirror Move", "Poison Gas", "Poison Powder", "Toxic", "Confuse Ray", "Glare", "Stun Spore", "Supersonic", "Thunder Wave", "Splash", "String Shot", "Whirlwind", "Leer", "Screech", "Tail Whip", "Growl", "Light Screen", "Mist", "Reflect", "Roar", "Flash", "Kinesis", "Minimize", "Sand Attack", "Smokescreen"]:    
                    
                    ##innefective move
                    if (Generation["typeMove"][Player_move] in "normal" and (Generation["type_1"][Ai_Pokemon] in "rock" or Generation["type_2"][Ai_Pokemon] in "rock")) or (Generation["typeMove"][Player_move] in "fire" and (Generation["type_1"][Ai_Pokemon] in "firewaterrockdragon" or Generation["type_2"][Ai_Pokemon] in "firewaterrockdragon")) or (Generation["typeMove"][Player_move] in "water" and (Generation["type_1"][Ai_Pokemon] in "watergrassdragon" or Generation["type_2"][Ai_Pokemon] in "watergrassdragon")) or (Generation["typeMove"][Player_move] in "electric" and (Generation["type_1"][Ai_Pokemon] in "electricgrassdragon" or Generation["type_2"][Ai_Pokemon] in "electricgrassdragon")) or (Generation["typeMove"][Player_move] in "grass" and (Generation["type_1"][Ai_Pokemon] in "firegrasspoisonflyingbugdragon" or Generation["type_2"][Ai_Pokemon] in "firegrasspoisonflyingbugdragon")) or (Generation["typeMove"][Player_move] in "ice" and (Generation["type_1"][Ai_Pokemon] in "fireice" or Generation["type_2"][Ai_Pokemon] in "fireice")) or (Generation["typeMove"][Player_move] in "fighting" and (Generation["type_1"][Ai_Pokemon] in "poisonflyingpsychicbug" or Generation["type_2"][Ai_Pokemon] in "poisonflyingpsychicbug")) or (Generation["typeMove"][Player_move] in "poison" and (Generation["type_1"][Ai_Pokemon] in "poisongroundrockghost" or Generation["type_2"][Ai_Pokemon] in "poisongroundrockghost")) or (Generation["typeMove"][Player_move] in "ground" and (Generation["type_1"][Ai_Pokemon] in "grassbug" or Generation["type_2"][Ai_Pokemon] in "grassbug")) or (Generation["typeMove"][Player_move] in "flying" and (Generation["type_1"][Ai_Pokemon] in "electricrock" or Generation["type_2"][Ai_Pokemon] in "electricrock")) or (Generation["typeMove"][Player_move] in "psychic" and (Generation["type_1"][Ai_Pokemon] in "psychic" or Generation["type_2"][Ai_Pokemon] in "psychic")) or (Generation["typeMove"][Player_move] in "bug" and (Generation["type_1"][Ai_Pokemon] in "firefightingflyingghost" or Generation["type_2"][Ai_Pokemon] in "firefightingflyingghost")) or (Generation["typeMove"][Player_move] in "rock" and (Generation["type_1"][Ai_Pokemon] in "fightingground" or Generation["type_2"][Ai_Pokemon] in "fightingground")):
                        modifier=0.5

                    ##Effective move
                    elif (Generation["typeMove"][Player_move] in "fire" and (Generation["type_1"][Ai_Pokemon] in "grassicebug" or Generation["type_2"][Ai_Pokemon] in "grassicebug")) or (Generation["typeMove"][Player_move] in "water" and (Generation["type_1"][Ai_Pokemon] in "firegroundrock" or Generation["type_2"][Ai_Pokemon] in "firegroundrock")) or (Generation["typeMove"][Player_move] in "electric" and (Generation["type_1"][Ai_Pokemon] in "waterflying" or Generation["type_2"][Ai_Pokemon] in "waterflying")) or (Generation["typeMove"][Player_move] in "grass" and (Generation["type_1"][Ai_Pokemon] in "watergroundrock" or Generation["type_2"][Ai_Pokemon] in "watergroundrock")) or (Generation["typeMove"][Player_move] in "ice" and (Generation["type_1"][Ai_Pokemon] in "grassgroundflyingdragon" or Generation["type_2"][Ai_Pokemon] in "grassgroundflyingdragon")) or (Generation["typeMove"][Player_move] in "fighting" and (Generation["type_1"][Ai_Pokemon] in "normalicerock" or Generation["type_2"][Ai_Pokemon] in "normalicerock")) or (Generation["typeMove"][Player_move] in "poison" and (Generation["type_1"][Ai_Pokemon] in "grassbug" or Generation["type_2"][Ai_Pokemon] in "grassbug")) or (Generation["typeMove"][Player_move] in "ground" and (Generation["type_1"][Ai_Pokemon] in "fireelectricpoisonrock" or Generation["type_2"][Ai_Pokemon] in "fireelectricpoisonrock")) or (Generation["typeMove"][Player_move] in "flying" and (Generation["type_1"][Ai_Pokemon] in "grassfightingbug" or Generation["type_2"][Ai_Pokemon] in "grassfightingbug")) or (Generation["typeMove"][Player_move] in "psychic" and (Generation["type_1"][Ai_Pokemon] in "fightingpoison" or Generation["type_2"][Ai_Pokemon] in "fightingpoison")) or (Generation["typeMove"][Player_move] in "bug" and (Generation["type_1"][Ai_Pokemon] in "grasspoisonpsychic" or Generation["type_2"][Ai_Pokemon] in "grasspoisonpsychic")) or (Generation["typeMove"][Player_move] in "rock" and (Generation["type_1"][Ai_Pokemon] in "fireiceflyingbug" or Generation["type_2"][Ai_Pokemon] in "fireiceflyingbug")) or (Generation["typeMove"][Player_move] in "ghost" and (Generation["type_1"][Ai_Pokemon] in "ghost" or Generation["type_2"][Ai_Pokemon] in "ghost")) or (Generation["typeMove"][Player_move] in "dragon" and (Generation["type_1"][Ai_Pokemon] in "dragon" or Generation["type_2"][Ai_Pokemon] in "dragon")):
                        modifier = 2

                    ## No Effect move
                    elif (Generation["typeMove"][Player_move] in "normal" and (Generation["type_1"][Ai_Pokemon] in "ghost" or Generation["type_2"][Ai_Pokemon] in "ghost")) or (Generation["typeMove"][Player_move] in "electric" and (Generation["type_1"][Ai_Pokemon] in "ground" or Generation["type_2"][Ai_Pokemon] in "ground")) or (Generation["typeMove"][Player_move] in "fighting" and (Generation["type_1"][Ai_Pokemon] in "ghost" or Generation["type_2"][Ai_Pokemon] in "ghost")) or (Generation["typeMove"][Player_move] in "ground" and (Generation["type_1"][Ai_Pokemon] in "flying" or Generation["type_2"][Ai_Pokemon] in "flying")) or (Generation["typeMove"][Player_move] in "ghost" and (Generation["type_1"][Ai_Pokemon] in "normalpsychic" or Generation["type_2"][Ai_Pokemon] in "normalpsychic")):
                        modifier = 0

                    ##Normal effect move
                    else:
                        modifier = 1

                    damage_dealt = math.ceil(((2*gamedata["PcLevel"][gamedata["party"][currentPokemon]]/5+2) * Generation["damage"][Player_move] * (Player_attack[currentPokemon]/Ai_defence)/50+2) *modifier)


                    ##Status effects
        
                else:
                    if Generation["moveset"][Player_move] in "Hypnosis Lovely Kiss Sing Sleep Powder Spore":
                        ##sleep
                        Ai_status = "Sleep"
                        Ai_status_length = 0
                        print(Generation["pokemon"][Ai_Pokemon] + " is now asleep")
                        print()
                    

                    elif Generation["moveset"][Player_move] in "Agility Double Team Teleport":
                        ##self-Generation["speed"]
                        Player_speed[currentPokemon] = round(float(Player_speed[currentPokemon])* 1.05)
                        print(Generation["pokemon"][gamedata["Pc"][gamedata["party"][currentPokemon]]] + "'s speed rose")
                        print()
                    
                    
                    elif Generation["moveset"][Player_move] in "Recover Soft-Boiled":
                        ##Self-heal half
                        if Generation["Player_health"][currentPokemon] <= 1/2*(round(Generation["HP"][gamedata["Pc"][currentPokemon]]*2 + gamedata["PcLevel"][currentPokemon]/100+gamedata["PcLevel"][currentPokemon]+10)):
                            Generation["Player_health"][currentPokemon] += 1/2*(round(Generation["HP"][gamedata["Pc"][currentPokemon]]*2 + gamedata["PcLevel"][currentPokemon]/100+gamedata["PcLevel"][currentPokemon]+10))
                        else: 
                            Generation["Player_health"][currentPokemon] = round(Generation["HP"][gamedata["Pc"][currentPokemon]]*2 + gamedata["PcLevel"][currentPokemon]/100+gamedata["PcLevel"][currentPokemon]+10)
                        
                        print(Generation["pokemon"][gamedata["Pc"][gamedata["party"][currentPokemon]]] + "'s healed")
                        print()

                    
                    elif Generation["moveset"][Player_move] in "Haze Leech Seed Rest Substitute":
                        ##self-heal
                        player_status="healing"
                        player_status_length = 0
                        
                        print(Generation["pokemon"][gamedata["Pc"][gamedata["party"][currentPokemon]]] + " is healing itself")
                        print()

                    
                    elif Generation["moveset"][Player_move] in "Acid Armor Amnesia Barrier Conversion Defense Curl Disable Harden Withdraw":
                        ##self-defense
                        Player_defence[currentPokemon] = round(float(Player_defence[currentPokemon])* 1.05)
                        
                        print(Generation["pokemon"][gamedata["Pc"][gamedata["party"][currentPokemon]]] + "'s defense rose")
                        print()

                    
                    elif Generation["moveset"][Player_move] in "Focus Energy Growth Meditate Sharpen Swords Dance":
                        ##self-Generation["attack"]
                        Player_attack[currentPokemon] = round(float(Player_attack[currentPokemon])* 1.05)
                        
                        print(Generation["pokemon"][gamedata["Pc"][gamedata["party"][currentPokemon]]] + "'s attack rose")
                        print()

                    
                    elif Generation["moveset"][Player_move] in "Metronome Transform Mimic Mirror Move":
                        ##random move
                        Player_move = randint(0,len(Generation["moveset"])-1)
                        if Generation["moveset"][Player_move] not in "Acid Armor Agility Amnesia Barrier Confuse Ray Conversion Defense Curl Disable Double Team Flash Focus Energy Glare Growl Growth Harden Haze Hypnosis Kinesis Leech Seed Leer Light Screen Lovely Kiss Meditate Metronome Mimic Minimize Mirror Move Mist Poison Gas Poison Powder Recover Reflect Rest Roar Sand Attack Screech Sharpen Sing Sleep Powder Smokescreen Soft-Boiled Splash Spore String Shot Stun Spore Substitute Supersonic Swords Dance Tail Whip Teleport Thunder Wave Toxic Transform Whirlwind Withdraw":    
                            print(Generation["pokemon"][gamedata["Pc"][gamedata["party"][currentPokemon]]] + " uses " + Generation["moveset"][Player_move])
                            ##innefective move
                            if (Generation["typeMove"][Player_move] == "normal" and (Generation["type_1"][Ai_Pokemon] == "rock" or Generation["type_2"][Ai_Pokemon] == "rock")) or (Generation["typeMove"][Player_move] == "fire" and (Generation["type_1"][Ai_Pokemon] in "firewaterrockdragon" or Generation["type_2"][Ai_Pokemon] in "firewaterrockdragon")) or (Generation["typeMove"][Player_move] == "water" and (Generation["type_1"][Ai_Pokemon] in "watergrassdragon" or Generation["type_2"][Ai_Pokemon] in "watergrassdragon")) or (Generation["typeMove"][Player_move] == "electric" and (Generation["type_1"][Ai_Pokemon] in "electricgrassdragon" or Generation["type_2"][Ai_Pokemon] in "electricgrassdragon")) or (Generation["typeMove"][Player_move] == "grass" and (Generation["type_1"][Ai_Pokemon] in "firegrasspoisonflyingbugdragon" or Generation["type_2"][Ai_Pokemon] in "firegrasspoisonflyingbugdragon")) or (Generation["typeMove"][Player_move] == "ice" and (Generation["type_1"][Ai_Pokemon] in "fireice" or Generation["type_2"][Ai_Pokemon] in "fireice")) or (Generation["typeMove"][Player_move] == "fighting" and (Generation["type_1"][Ai_Pokemon] in "poisonflyingpsychicbug" or Generation["type_2"][Ai_Pokemon] in "poisonflyingpsychicbug")) or (Generation["typeMove"][Player_move] == "poison" and (Generation["type_1"][Ai_Pokemon] in "poisongroundrockghost" or Generation["type_2"][Ai_Pokemon] in "poisongroundrockghost")) or (Generation["typeMove"][Player_move] == "ground" and (Generation["type_1"][Ai_Pokemon] in "grassbug" or Generation["type_2"][Ai_Pokemon] in "grassbug")) or (Generation["typeMove"][Player_move] == "flying" and (Generation["type_1"][Ai_Pokemon] in "electricrock" or Generation["type_2"][Ai_Pokemon] in "electricrock")) or (Generation["typeMove"][Player_move] == "psychic" and (Generation["type_1"][Ai_Pokemon] in "psychic" or Generation["type_2"][Ai_Pokemon] in "psychic")) or (Generation["typeMove"][Player_move] == "bug" and (Generation["type_1"][Ai_Pokemon] in "firefightingflyingghost" or Generation["type_2"][Ai_Pokemon] in "firefightingflyingghost")) or (Generation["typeMove"][Player_move] == "rock" and (Generation["type_1"][Ai_Pokemon] in "fightingground" or Generation["type_2"][Ai_Pokemon] in "fightingground")):
                                print("not very effective")
                                modifier=0.5

                            elif (Generation["typeMove"][Player_move] == "fire" and (Generation["type_1"][Ai_Pokemon] == "grassicebug" or Generation["type_2"][Ai_Pokemon] == "grassicebug")) or (Generation["typeMove"][Player_move] == "water" and (Generation["type_1"][Ai_Pokemon] == "firegroundrock" or Generation["type_2"][Ai_Pokemon] == "firegroundrock")) or (Generation["typeMove"][Player_move] == "electric" and (Generation["type_1"][Ai_Pokemon] == "waterflying" or Generation["type_2"][Ai_Pokemon] == "waterflying")) or (Generation["typeMove"][Player_move] == "grass" and (Generation["type_1"][Ai_Pokemon] == "watergroundrock" or Generation["type_2"][Ai_Pokemon] == "watergroundrock")) or (Generation["typeMove"][Player_move] == "ice" and (Generation["type_1"][Ai_Pokemon] == "grassgroundflyingdragon" or Generation["type_2"][Ai_Pokemon] == "grassgroundflyingdragon")) or (Generation["typeMove"][Player_move] == "fighting" and (Generation["type_1"][Ai_Pokemon] == "normalicerock" or Generation["type_2"][Ai_Pokemon] == "normalicerock")) or (Generation["typeMove"][Player_move] == "poison" and (Generation["type_1"][Ai_Pokemon] == "grassbug" or Generation["type_2"][Ai_Pokemon] == "grassbug")) or (Generation["typeMove"][Player_move] == "ground" and (Generation["type_1"][Ai_Pokemon] == "fireelectricpoisonrock" or Generation["type_2"][Ai_Pokemon] == "fireelectricpoisonrock")) or (Generation["typeMove"][Player_move] == "flying" and (Generation["type_1"][Ai_Pokemon] == "grassfightingbug" or Generation["type_2"][Ai_Pokemon] == "grassfightingbug")) or (Generation["typeMove"][Player_move] == "psychic" and (Generation["type_1"][Ai_Pokemon] == "fightingpoison" or Generation["type_2"][Ai_Pokemon] == "fightingpoison")) or (Generation["typeMove"][Player_move] == "bug" and (Generation["type_1"][Ai_Pokemon] == "grasspoisonpsychic" or Generation["type_2"][Ai_Pokemon] == "grasspoisonpsychic")) or (Generation["typeMove"][Player_move] == "rock" and (Generation["type_1"][Ai_Pokemon] == "fireiceflyingbug" or Generation["type_2"][Ai_Pokemon] == "fireiceflyingbug")) or (Generation["typeMove"][Player_move] == "ghost" and (Generation["type_1"][Ai_Pokemon] == "ghost" or Generation["type_2"][Ai_Pokemon] == "ghost")) or (Generation["typeMove"][Player_move] == "dragon" and (Generation["type_1"][Ai_Pokemon] == "dragon" or Generation["type_2"][Ai_Pokemon] == "dragon")):
                                print("Very effective")
                                modifier = 2

                            elif (Generation["typeMove"][Player_move] == "normal" and (Generation["type_1"][Ai_Pokemon] == "ghost" or Generation["type_2"][Ai_Pokemon] == "ghost")) or (Generation["typeMove"][Player_move] == "electric" and (Generation["type_1"][Ai_Pokemon] == "ground" or Generation["type_2"][Ai_Pokemon] == "ground")) or (Generation["typeMove"][Player_move] == "fighting" and (Generation["type_1"][Ai_Pokemon] == "ghost" or Generation["type_2"][Ai_Pokemon] == "ghost")) or (Generation["typeMove"][Player_move] == "ground" and (Generation["type_1"][Ai_Pokemon] == "flying" or Generation["type_2"][Ai_Pokemon] == "flying")) or (Generation["typeMove"][Player_move] == "ghost" and (Generation["type_1"][Ai_Pokemon] == "normalpsychic" or Generation["type_2"][Ai_Pokemon] == "normalpsychic")):
                                print("No effect")
                                modifier = 0

                            else:
                                print("yes")
                                modifier = 1
                            
                            damage_dealt = round(((2*gamedata["PcLevel"][gamedata["party"][currentPokemon]]/5+2) * Generation["damage"][Player_move] * (Player_attack[currentPokemon]/Ai_defence)/50+2) *modifier)
                            Generation["Ai_health"]-=damage_dealt
                            print("Damage dealt: " + str(damage_dealt) + " " + Generation["pokemon"][Ai_Pokemon] + " has " + str(Generation["Ai_health"]) + " left")

                        else:
                            print("No effect")

                    
                    elif Generation["moveset"][Player_move] in "Poison Gas Poison Powder Toxic":
                        ##poison
                        Ai_status = "poison"
                        Ai_status_length = 0
                        
                        print(Generation["pokemon"][Ai_Pokemon] + " is now poisoned")
                        print()
                    

                    elif Generation["moveset"][Player_move] in "Confuse Ray Glare Stun Spore Supersonic Thunder Wave":
                        ##paralysis
                        Ai_status = "paralysis"
                        Ai_status_length = 0
                        print(Generation["pokemon"][Ai_Pokemon] + " is now paralysed")
                        print()


                    elif Generation["moveset"][Player_move] in "Splash":
                        ##none
                        print("Has no effect whatsoever.")
                        print()
                    

                    elif Generation["moveset"][Player_move] in "String Shot Whirlwind":
                        ##enemy-Generation["speed"]
                        Ai_speed= round(float(Ai_speed)* 0.95)
                        print(Generation["pokemon"][Ai_Pokemon] + " is now slower")
                        print()

                    
                    elif Generation["moveset"][Player_move] in "Leer Screech Tail Whip":
                        ##enemy-Generation["defence"]
                        Ai_defence= round(float(Ai_defence)* 0.95)
                        print(Generation["pokemon"][Ai_Pokemon] + "'s defence fell")
                        print()

                    
                    elif Generation["moveset"][Player_move] in "Growl Light Screen Mist Reflect Roar":
                        ##enemy-Generation["attack"]
                        Ai_attack= round(float(Ai_attack)* 0.95)
                        print(Generation["pokemon"][Ai_Pokemon] + "'s attack fell")
                        print()
                
                    elif Generation["moveset"][Player_move] in "Flash Kinesis Minimize Sand Attack Smokescreen":
                        ##enemy-Generation["accuracy"]
                        Ai_evasion= round(float(Ai_evasion)* 0.95)
                        print(Generation["pokemon"][Ai_Pokemon] + "'s accuracy fell")
                        print()

            else:
                print(Generation["pokemon"][gamedata["Pc"][gamedata["party"][currentPokemon]]] + " misses.")
                print()

        
        ## Ai Move calculation
        if Ai_paralysed == False:
            P =Generation["accuracy"][Ai_turn] * (Ai_evasion/Player_evasion)
            hit_chance = randint(0,100)

            if P>=hit_chance or Generation["moveset"][Ai_turn] in ["Hypnosis", "Lovely Kiss", "Sing", "Sleep Powder", "Spore", "Agility", "Double Team", "Teleport", "Recover", "Soft-Boiled", "Haze", "Leech Seed", "Rest", "Substitute", "Acid Armor", "Amnesia", "Barrier", "Conversion", "Defense Curl", "Disable", "Harden", "Withdraw", "Focus Energy", "Growth", "Meditate", "Sharpen", "Swords Dance", "Metronome", "Transform", "Mimic", "Mirror Move", "Poison Gas", "Poison Powder", "Toxic", "Confuse Ray", "Glare", "Stun Spore", "Supersonic", "Thunder Wave", "Splash", "String Shot", "Whirlwind", "Leer", "Screech", "Tail Whip", "Growl", "Light Screen", "Mist", "Reflect", "Roar", "Flash", "Kinesis", "Minimize", "Sand Attack", "Smokescreen"]:

                ## Regular Moves
                if Generation["moveset"][Ai_turn] not in ["Hypnosis", "Lovely Kiss", "Sing", "Sleep Powder", "Spore", "Agility", "Double Team", "Teleport", "Recover", "Soft-Boiled", "Haze", "Leech Seed", "Rest", "Substitute", "Acid Armor", "Amnesia", "Barrier", "Conversion", "Defense Curl", "Disable", "Harden", "Withdraw", "Focus Energy", "Growth", "Meditate", "Sharpen", "Swords Dance", "Metronome", "Transform", "Mimic", "Mirror Move", "Poison Gas", "Poison Powder", "Toxic", "Confuse Ray", "Glare", "Stun Spore", "Supersonic", "Thunder Wave", "Splash", "String Shot", "Whirlwind", "Leer", "Screech", "Tail Whip", "Growl", "Light Screen", "Mist", "Reflect", "Roar", "Flash", "Kinesis", "Minimize", "Sand Attack", "Smokescreen"]:    
                    
                    ##innefective move
                    if (Generation["typeMove"][Ai_turn] in "normal" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "rock" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "rock")) or (Generation["typeMove"][Ai_turn] in "fire" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "firewaterrockdragon" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "firewaterrockdragon")) or (Generation["typeMove"][Ai_turn] in "water" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "watergrassdragon" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "watergrassdragon")) or (Generation["typeMove"][Ai_turn] in "electric" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "electricgrassdragon" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "electricgrassdragon")) or (Generation["typeMove"][Ai_turn] in "grass" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "firegrasspoisonflyingbugdragon" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "firegrasspoisonflyingbugdragon")) or (Generation["typeMove"][Ai_turn] in "ice" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "fireice" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "fireice")) or (Generation["typeMove"][Ai_turn] in "fighting" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "poisonflyingpsychicbug" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "poisonflyingpsychicbug")) or (Generation["typeMove"][Ai_turn] in "poison" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "poisongroundrockghost" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "poisongroundrockghost")) or (Generation["typeMove"][Ai_turn] in "ground" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "grassbug" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "grassbug")) or (Generation["typeMove"][Ai_turn] in "flying" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "electricrock" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "electricrock")) or (Generation["typeMove"][Ai_turn] in "psychic" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "psychic" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "psychic")) or (Generation["typeMove"][Ai_turn] in "bug" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "firefightingflyingghost" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "firefightingflyingghost")) or (Generation["typeMove"][Ai_turn] in "rock" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "fightingground" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "fightingground")):                        
                        A_modifier=0.5

                    ##Effective move
                    elif (Generation["typeMove"][Ai_turn] in "fire" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "grassicebug" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "grassicebug")) or (Generation["typeMove"][Ai_turn] in "water" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "firegroundrock" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "firegroundrock")) or (Generation["typeMove"][Ai_turn] in "electric" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "waterflying" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "waterflying")) or (Generation["typeMove"][Ai_turn] in "grass" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "watergroundrock" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "watergroundrock")) or (Generation["typeMove"][Ai_turn] in "ice" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "grassgroundflyingdragon" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "grassgroundflyingdragon")) or (Generation["typeMove"][Ai_turn] in "fighting" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "normalicerock" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "normalicerock")) or (Generation["typeMove"][Ai_turn] in "poison" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "grassbug" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "grassbug")) or (Generation["typeMove"][Ai_turn] in "ground" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "fireelectricpoisonrock" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "fireelectricpoisonrock")) or (Generation["typeMove"][Ai_turn] in "flying" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "grassfightingbug" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "grassfightingbug")) or (Generation["typeMove"][Ai_turn] in "psychic" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "fightingpoison" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "fightingpoison")) or (Generation["typeMove"][Ai_turn] in "bug" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "grasspoisonpsychic" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "grasspoisonpsychic")) or (Generation["typeMove"][Ai_turn] in "rock" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "fireiceflyingbug" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "fireiceflyingbug")) or (Generation["typeMove"][Ai_turn] in "ghost" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "ghost" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "ghost")) or (Generation["typeMove"][Ai_turn] in "dragon" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "dragon" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "dragon")):                        
                        A_modifier = 2

                    ## No Effect move
                    elif (Generation["typeMove"][Ai_turn] in "normal" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "ghost" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "ghost")) or (Generation["typeMove"][Ai_turn] in "electric" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "ground" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "ground")) or (Generation["typeMove"][Ai_turn] in "fighting" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "ghost" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "ghost")) or (Generation["typeMove"][Ai_turn] in "ground" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "flying" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "flying")) or (Generation["typeMove"][Ai_turn] in "ghost" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "normalpsychic" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "normalpsychic")):
                        A_modifier = 0

                    ##Normal effect move
                    else:
                        A_modifier = 1

                    Ai_damage_dealt = math.ceil(((2*Ai_level/5+2) * Generation["damage"][Ai_turn] * (Ai_attack/Player_defence[currentPokemon])/50+2) *A_modifier)


                    ##Status effects
        
                ## Special Moves
                else:
                    if Generation["moveset"][Ai_turn] in "Hypnosis Lovely Kiss Sing Sleep Powder Spore":
                        ##sleep
                        Player_status = "Sleep"
                        Player_status_length = 0
                        print("you are now asleep")

                    elif Generation["moveset"][Ai_turn] in "Agility Double Team Teleport":
                        ##self-Generation["speed"]
                        Ai_speed = round(float(Ai_speed)* 1.05)
                    elif Generation["moveset"][Ai_turn] in "Recover Soft-Boiled":
                        ##Self-heal half
                        if Generation["Ai_health"] <= round(1/2*(Generation["HP"][Ai_Pokemon]*2 + Ai_level/100+Ai_level+10)):
                            Generation["Ai_health"]= Generation["Ai_health"] + round(1/2*(Generation["HP"][Ai_Pokemon]*2 + Ai_level/100+Ai_level+10))
                        else: 
                            Generation["Ai_health"] = (round(Generation["HP"][Ai_Pokemon]*2 + Ai_level/100+Ai_level+10))

                        print("Ai Heals itself")

                    elif Generation["moveset"][Ai_turn] in "Haze Leech Seed Rest Substitute":
                        ##self-heal
                        Ai_status="healing"
                        Ai_status_length = 0
                        print("The Ai is healing itself")

                    elif Generation["moveset"][Ai_turn] in "Acid Armor Amnesia Barrier Conversion Defense Curl Disable Harden Withdraw":
                        ##self-defense
                        Ai_defence  = round(float(Ai_defence)* 1.05)
                        print("The Ai's defence rose")

                    elif Generation["moveset"][Ai_turn] in "Focus Energy Growth Meditate Sharpen Swords Dance":
                        ##self-Generation["attack"]
                        Ai_attack  = round(float(Ai_attack)* 1.05)
                        print("The Ai's attack rose")

                    elif Generation["moveset"][Ai_turn] in "Metronome Transform Mimic Mirror Move":
                        ##random move
                        Ai_turn = randint(0,len(Generation["moveset"])-1)
                        if Generation["moveset"][Ai_turn] not in "Acid Armor Agility Amnesia Barrier Confuse Ray Conversion Defense Curl Disable Double Team Flash Focus Energy Glare Growl Growth Harden Haze Hypnosis Kinesis Leech Seed Leer Light Screen Lovely Kiss Meditate Metronome Mimic Minimize Mirror Move Mist Poison Gas Poison Powder Recover Reflect Rest Roar Sand Attack Screech Sharpen Sing Sleep Powder Smokescreen Soft-Boiled Splash Spore String Shot Stun Spore Substitute Supersonic Swords Dance Tail Whip Teleport Thunder Wave Toxic Transform Whirlwind Withdraw":    
                            
                            
                            ##innefective move
                            if (Generation["typeMove"][Ai_turn] in "normal" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "rock" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "rock")) or (Generation["typeMove"][Ai_turn] in "fire" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "firewaterrockdragon" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "firewaterrockdragon")) or (Generation["typeMove"][Ai_turn] in "water" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "watergrassdragon" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "watergrassdragon")) or (Generation["typeMove"][Ai_turn] in "electric" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "electricgrassdragon" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "electricgrassdragon")) or (Generation["typeMove"][Ai_turn] in "grass" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "firegrasspoisonflyingbugdragon" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "firegrasspoisonflyingbugdragon")) or (Generation["typeMove"][Ai_turn] in "ice" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "fireice" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "fireice")) or (Generation["typeMove"][Ai_turn] in "fighting" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "poisonflyingpsychicbug" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "poisonflyingpsychicbug")) or (Generation["typeMove"][Ai_turn] in "poison" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "poisongroundrockghost" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "poisongroundrockghost")) or (Generation["typeMove"][Ai_turn] in "ground" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "grassbug" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "grassbug")) or (Generation["typeMove"][Ai_turn] in "flying" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "electricrock" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "electricrock")) or (Generation["typeMove"][Ai_turn] in "psychic" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "psychic" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "psychic")) or (Generation["typeMove"][Ai_turn] in "bug" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "firefightingflyingghost" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "firefightingflyingghost")) or (Generation["typeMove"][Ai_turn] in "rock" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "fightingground" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "fightingground")):                        
                                A_modifier=0.5

                            ##Effective move
                            elif (Generation["typeMove"][Ai_turn] in "fire" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "grassicebug" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "grassicebug")) or (Generation["typeMove"][Ai_turn] in "water" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "firegroundrock" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "firegroundrock")) or (Generation["typeMove"][Ai_turn] in "electric" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "waterflying" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "waterflying")) or (Generation["typeMove"][Ai_turn] in "grass" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "watergroundrock" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "watergroundrock")) or (Generation["typeMove"][Ai_turn] in "ice" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "grassgroundflyingdragon" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "grassgroundflyingdragon")) or (Generation["typeMove"][Ai_turn] in "fighting" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "normalicerock" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "normalicerock")) or (Generation["typeMove"][Ai_turn] in "poison" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "grassbug" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "grassbug")) or (Generation["typeMove"][Ai_turn] in "ground" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "fireelectricpoisonrock" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "fireelectricpoisonrock")) or (Generation["typeMove"][Ai_turn] in "flying" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "grassfightingbug" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "grassfightingbug")) or (Generation["typeMove"][Ai_turn] in "psychic" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "fightingpoison" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "fightingpoison")) or (Generation["typeMove"][Ai_turn] in "bug" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "grasspoisonpsychic" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "grasspoisonpsychic")) or (Generation["typeMove"][Ai_turn] in "rock" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "fireiceflyingbug" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "fireiceflyingbug")) or (Generation["typeMove"][Ai_turn] in "ghost" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "ghost" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "ghost")) or (Generation["typeMove"][Ai_turn] in "dragon" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "dragon" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "dragon")):                        
                                A_modifier = 2

                            ## No Effect move
                            elif (Generation["typeMove"][Ai_turn] in "normal" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "ghost" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "ghost")) or (Generation["typeMove"][Ai_turn] in "electric" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "ground" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "ground")) or (Generation["typeMove"][Ai_turn] in "fighting" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "ghost" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "ghost")) or (Generation["typeMove"][Ai_turn] in "ground" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "flying" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "flying")) or (Generation["typeMove"][Ai_turn] in "ghost" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "normalpsychic" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "normalpsychic")):
                                A_modifier = 0

                            ##Normal effect move
                            else:
                                A_modifier = 1

                            Ai_damage_dealt = round(((2*Ai_level/5+2) * Generation["damage"][Ai_turn] * (Ai_attack/Player_defence[currentPokemon])/50+2) *A_modifier)

                        else:
                            A_modifier = 0 

                    elif Generation["moveset"][Ai_turn] in "Poison Gas Poison Powder Toxic":
                        ##poison
                        Player_status = "poison"
                        Player_status_length = 0
                        print("You are now poisoned")

                    elif Generation["moveset"][Ai_turn] in "Confuse Ray Glare Stun Spore Supersonic Thunder Wave":
                        ##paralysis
                        Player_status = "paralysis"
                        Player_status_length = 0
                        print("You are now asleep")

                    elif Generation["moveset"][Ai_turn] in "Splash":
                        ##none
                        print("Has no effect whatsoever.")

                    elif Generation["moveset"][Ai_turn] in "String Shot Whirlwind":
                        ##enemy-Generation["speed"]
                        Player_speed[currentPokemon] = round(float(Player_speed[currentPokemon])*0.95)
                        print("Your speed fell")

                    elif Generation["moveset"][Ai_turn] in "Leer Screech Tail Whip":
                        ##enemy-defence
                        Player_defence[currentPokemon]= round(float(Player_defence[currentPokemon])*0.95)
                        print("Your defence fell")

                    elif Generation["moveset"][Ai_turn] in "Growl Light Screen Mist Reflect Roar":
                        ##enemy-Generation["attack"]
                        Player_attack[currentPokemon]= round(float(Player_attack[currentPokemon])*0.95)
                        print("Your attack fell")

                    elif Generation["moveset"][Player_move] in "Flash Kinesis Minimize Sand Attack Smokescreen":
                        ##enemy-Generation["accuracy"]
                        print("Your accuracy fell")
                        Player_evasion[currentPokemon]= round(float(Player_evasion[currentPokemon])*0.95)

            else:
                print(Generation["pokemon"][Ai_Pokemon] + " misses.")
                print()

        ##Move order
        
        if Player_speed[currentPokemon]>Ai_speed and Player_move!=-1:
            print(Generation["pokemon"][gamedata["Pc"][gamedata["party"][currentPokemon]]] + " uses " + Generation["moveset"][Player_move])
            Generation["Ai_health"]-=damage_dealt
        
            if modifier == 0.5:
                print("Not very effective")
            elif modifier == 2:
                print("Very Effective")
            elif modifier == 0:
                print("No effect")

            print("Damage dealt: " + str(damage_dealt) + " " + Generation["pokemon"][Ai_Pokemon] + " has " + str(Generation["Ai_health"]) + " left")
            print()

            if Generation["Ai_health"]>0:
                print(Generation["pokemon"][Ai_Pokemon] + " uses " + Generation["moveset"][Ai_turn])
                Generation["Player_health"][currentPokemon]-=Ai_damage_dealt
                
                if A_modifier == 0.5:
                    print("Not very effective")
                elif A_modifier == 2:
                    print("Very Effective")
                elif A_modifier == 0:
                    print("No effect")

                print("Damage dealt: " + str(Ai_damage_dealt) + " " + Generation["pokemon"][gamedata["Pc"][gamedata["party"][currentPokemon]]] + " has " + str(Generation["Player_health"][currentPokemon]) + " left")
                
                
                if Generation["Player_health"][currentPokemon] <= 0:    
                    ##Choose next Generation["pokemon"]
                    print(Generation["pokemon"][gamedata["Pc"][gamedata["party"][currentPokemon]]] + " Fainted")
                    i=0
                    for x in Generation["Player_health"]:
                        if x>0:
                            currentPokemon=i
                            print("Go " + Generation["pokemon"][gamedata["Pc"][gamedata["party"][currentPokemon]]] + "!")
                            break
                        i+=1
                    if Generation["Player_health"][currentPokemon] <= 0:
                        print("You black out")
                        break

            else:
                ### Calculate XP
                print("XP")
                xp_recieved = round((1000*Ai_level/5)*(((2*Ai_level+10)**2.5)/(Ai_level + gamedata["PcLevel"][gamedata["party"][currentPokemon]] + 10)**2.5+1))

                print("xp Earned: " + str(xp_recieved))
                gamedata["xp"][gamedata["party"][currentPokemon]]+=xp_recieved

                ##Required xp to level up
                xp_table = [8,19,37,61,91,127,169,217,271,331,397,469,547,631,721,817,919,1027,1141,1261,1387,1519,1657,1801,1951,2107,2269,2437,2611,2791,2977,3169,3367,3571,3781,3997,4219,4447,4681,4921,5167,5419,5677,5941,6211,6487,6769,7057,7351,7651,7957,8269,8587,8911,9241,9577,9919,10267,10621,10981,11347,11719,12097,12481,12871,13267,13669,14077,14491,14911,15337,15769,16207,16651,17101,17557,18019,18487,18961,19441,19927,20419,20917,21421,21931,22447,22969,23497,24031,24571,25117,25669,26227,26791,27361,27937,28519,29107,29701,9999999999999999999999]
                
                ##Level up
                if gamedata["xp"][gamedata["party"][currentPokemon]] >= xp_table[gamedata["PcLevel"][gamedata["party"][currentPokemon]]-1]:
                    
                    gamedata["xp"][gamedata["party"][currentPokemon]] -= xp_table[gamedata["PcLevel"][gamedata["party"][currentPokemon]]-1]
                    gamedata["PcLevel"][gamedata["party"][currentPokemon]]+=1
                    
                    print(Generation["pokemon"][gamedata["Pc"][gamedata["party"][currentPokemon]]] + " Levelled Up! They are now level " + str(gamedata["PcLevel"][gamedata["party"][currentPokemon]]))
                    
                    ##New move
                    if gamedata["PcLevel"][gamedata["party"][currentPokemon]]%2 ==0:
                        temp = Generation["learnsets"][gamedata["Pc"][gamedata["party"][currentPokemon]]].split("-")

                        while True:
                            new_move = randint(0,len(temp)-1)
                            
                            if temp[new_move] not in gamedata["PcMoves"][gamedata["party"][currentPokemon]]:
                                
                                print(Generation["pokemon"][gamedata["Pc"][gamedata["party"][currentPokemon]]] + " would like to learn the move:")
                                print(Generation["moveset"][int(temp[new_move])] + " Damage: " + str(Generation["damage"][int(temp[new_move])]) + " Accuracy: " + str(Generation["accuracy"][int(temp[new_move])]) + " Type: " + Generation["typeMove"][int(temp[new_move])])

                                game = 0
                                ##Learn move
                                while game != "yes" and game != "no":
                                    game = input("would you like to learn it? ")
                                    if game == 'no':
                                        print(Generation["pokemon"][gamedata["Pc"][gamedata["party"][currentPokemon]]] + " does not learn the move")

                                    elif game == "yes":
                                        i=0

                                        gamedata["PcMoves"][gamedata["party"][currentPokemon]].split("-")
                                        for x in gamedata["PcMoves"][gamedata["party"][currentPokemon]].split("-"):
                                            print("#"+str(i)+ " " + Generation[
                                                  "moveset"][int(x)] + " Damage: " + str(Generation["damage"][int(x)]) + " Accuracy: " + str(Generation["accuracy"][int(x)]) + " Type: " + Generation["typeMove"][int(x)])
                                            i+=1

                                        remove_move = int(input("Which move would you like to forget? "))
                                        
                                        if remove_move>len(gamedata["PcMoves"][gamedata["party"][currentPokemon]].split("-"))-1:
                                            gamedata["PcMoves"][gamedata["party"][currentPokemon]] += "-" + temp[new_move]
                                        
                                        else:
                                            banned_move = gamedata["PcMoves"][gamedata["party"][currentPokemon]].split("-")[remove_move]
                                            new_list = []

                                            for x in gamedata["PcMoves"][gamedata["party"][currentPokemon]].split("-"):
                                                if banned_move != x:
                                                    new_list.append(x)
                                                else:
                                                    new_list.append(temp[new_move])
                                            
                                            x = "-".join(new_list)

                                            gamedata["PcMoves"][gamedata["party"][currentPokemon]] = x
                                    break
                                break

                    ##Evolve
                    if ((gamedata["PcLevel"][gamedata["party"][currentPokemon]] == 25 or gamedata["PcLevel"][gamedata["party"][currentPokemon]] == 50 or gamedata["PcLevel"][gamedata["party"][currentPokemon]] >= 75) and Generation["next_evolve"][gamedata["Pc"][gamedata["party"][currentPokemon]]] != 0 ):

                        gamedata["pc"][gamedata["party"][currentPokemon]]=Generation["next_evolve"][gamedata["Pc"][gamedata["party"][currentPokemon]]]
                        print( Generation["pokemon"][gamedata["Pc"][gamedata["party"][currentPokemon]]-1] + " Evolves! They are now " + Generation["pokemon"][gamedata["Pc"][gamedata["party"][currentPokemon]]])
                
                gamedata["money"] += 100
                print("You earned $100! You now have $" + str(gamedata["money"]))
                save()
                break
        

        ##Ai Moves first
        else:
            print(Generation["pokemon"][Ai_Pokemon] + " uses " + Generation["moveset"][Ai_turn])
            Generation["Player_health"][currentPokemon]-=Ai_damage_dealt
                
            if A_modifier == 0.5:
                print("Not very effective")
            elif A_modifier == 2:
                print("Very Effective")
            elif A_modifier == 0:
                print("No effect")

            print("Damage dealt: " + str(Ai_damage_dealt) + " " + Generation["pokemon"][gamedata["Pc"][gamedata["party"][currentPokemon]]] + " has " + str(Generation["Player_health"][currentPokemon]) + " left")
            print()

            if Generation["Player_health"][currentPokemon]>0 and Player_move!=-1:
                print(Generation["pokemon"][gamedata["Pc"][gamedata["party"][currentPokemon]]] + " uses " + Generation["moveset"][Player_move])
                Generation["Ai_health"]-=damage_dealt
                
                if modifier == 0.5:
                    print("Not very effective")
                elif modifier == 2:
                    print("Very Effective")
                elif modifier == 0:
                    print("No effect")

                print("Damage dealt: " + str(damage_dealt) + " " + Generation["pokemon"][Ai_Pokemon] + " has " + str(Generation["Ai_health"]) + " left")

                if Generation["Ai_health"]<=0:
                    ### Calculate XP
                    print("XP")
                    xp_recieved = round((1000*Ai_level/5)*(((2*Ai_level+10)**2.5)/(Ai_level + gamedata["PcLevel"][gamedata["party"][currentPokemon]] + 10)**2.5+1))

                    print("xp Earned: " + str(xp_recieved))
                    gamedata["xp"][gamedata["party"][currentPokemon]]+=xp_recieved

                    ##Required xp to level up
                    xp_table = [8,19,37,61,91,127,169,217,271,331,397,469,547,631,721,817,919,1027,1141,1261,1387,1519,1657,1801,1951,2107,2269,2437,2611,2791,2977,3169,3367,3571,3781,3997,4219,4447,4681,4921,5167,5419,5677,5941,6211,6487,6769,7057,7351,7651,7957,8269,8587,8911,9241,9577,9919,10267,10621,10981,11347,11719,12097,12481,12871,13267,13669,14077,14491,14911,15337,15769,16207,16651,17101,17557,18019,18487,18961,19441,19927,20419,20917,21421,21931,22447,22969,23497,24031,24571,25117,25669,26227,26791,27361,27937,28519,29107,29701,9999999999999999999999]
                    
                    ##Level up
                    if gamedata["xp"][gamedata["party"][currentPokemon]] >= xp_table[gamedata["PcLevel"][gamedata["party"][currentPokemon]]-1]:
                        
                        gamedata["xp"][gamedata["party"][currentPokemon]] -= xp_table[gamedata["PcLevel"][gamedata["party"][currentPokemon]]-1]
                        gamedata["PcLevel"][gamedata["party"][currentPokemon]]+=1
                        
                        print(Generation["pokemon"][gamedata["Pc"][gamedata["party"][currentPokemon]]] + " Levelled Up! They are now level " + str(gamedata["PcLevel"][gamedata["party"][currentPokemon]]))
                        
                        ##New move
                        if gamedata["PcLevel"][gamedata["party"][currentPokemon]]%2 ==0:
                            temp = Generation["learnsets"][gamedata["Pc"][gamedata["party"][currentPokemon]]].split("-")

                            while True:
                                new_move = randint(0,len(temp)-1)
                                
                                if temp[new_move] not in gamedata["PcMoves"][gamedata["party"][currentPokemon]]:
                                    
                                    print(Generation["pokemon"][gamedata["Pc"][gamedata["party"][currentPokemon]]] + " would like to learn the move:")
                                    print(Generation["moveset"][int(temp[new_move])] + " Damage: " + str(Generation["damage"][int(temp[new_move])]) + " Accuracy: " + str(Generation["accuracy"][int(temp[new_move])]) + " Type: " + Generation["typeMove"][int(temp[new_move])])

                                    game = 0
                                    ##Learn move
                                    while game != "yes" and game != "no":
                                        game = input("would you like to learn it? ")
                                        if game == 'no':
                                            print(Generation["pokemon"][gamedata["Pc"][gamedata["party"][currentPokemon]]] + " does not learn the move")

                                        elif game == "yes":
                                            i=0

                                            gamedata["PcMoves"][gamedata["party"][currentPokemon]].split("-")
                                            for x in gamedata["PcMoves"][gamedata["party"][currentPokemon]].split("-"):
                                                print("#"+str(i)+ " " + Generation["moveset"][int(x)] + " Damage: " + str(Generation["damage"][int(x)]) + " Accuracy: " + str(Generation["accuracy"][int(x)]) + " Type: " + Generation["typeMove"][int(x)])
                                                i+=1

                                            remove_move = int(input("Which move would you like to forget? "))
                                            if remove_move>len(gamedata["PcMoves"][gamedata["party"][currentPokemon]].split("-"))-1:
                                                gamedata["PcMoves"][gamedata["party"][currentPokemon]] += "-" + temp[new_move]
                                            
                                            else:
                                                banned_move = gamedata["PcMoves"][gamedata["party"][currentPokemon]].split("-")[remove_move]
                                                new_list = []

                                                for x in gamedata["PcMoves"][gamedata["party"][currentPokemon]].split("-"):
                                                    if banned_move != x:
                                                        new_list.append(x)
                                                    else:
                                                        new_list.append(temp[new_move])
                
                                                x = "-".join(new_list)

                                                gamedata["PcMoves"][gamedata["party"][currentPokemon]] = x
                                        break
                                    break


                        ##Evolve
                        if ((gamedata["PcLevel"][gamedata["party"][currentPokemon]] == 25 or gamedata["PcLevel"][gamedata["party"][currentPokemon]] == 50 or gamedata["PcLevel"][gamedata["party"][currentPokemon]] >= 75) and Generation["next_evolve"][gamedata["Pc"][gamedata["party"][currentPokemon]]] != 0 ):

                            gamedata["Pc"][gamedata["party"][currentPokemon]]=Generation["next_evolve"][gamedata["Pc"][gamedata["party"][currentPokemon]]]
                            print( Generation["pokemon"][gamedata["Pc"][gamedata["party"][currentPokemon]]-1] + " Evolves! They are now " + Generation["pokemon"][gamedata["Pc"][gamedata["party"][currentPokemon]]])
                    
                    gamedata["money"] += 100
                    print("You earned $100! You now have $" + str(gamedata["money"]))
                    save()
                    break

            elif Generation["Player_health"][currentPokemon] <= 0:
                ##Choose next Generation["pokemon"]
                print(Generation["pokemon"][gamedata["Pc"][gamedata["party"][currentPokemon]]] + " Fainted")
                i=0
                for x in Generation["Player_health"]:
                    if x>0:
                        currentPokemon=i
                        print("Go " + Generation["pokemon"][gamedata["Pc"][gamedata["party"][currentPokemon]]] + "!")
                        break
                    i+=1
                if Generation["Player_health"][currentPokemon] <= 0:
                    print("You black out")
                    break

    
        Player_status_length+=1
        Ai_status_length+=1

def TrainerBattle():
    print()
    previous_ai = 1
    Ai_moves = []
    Ai_Pokemon= Generation["TrainerPokemon"][gamedata["BattleWon"]].split("-")
    Ai_level = Generation["TrainerLevel"][gamedata["BattleWon"]].split("-")
    AiCurrentPokemon = 0

    Ai_attack = []
    Generation["Ai_health"] = []
    Ai_speed = []
    Ai_defence = []

    i=0
    for x in Ai_Pokemon:
        x = int(x)
        if x != 1000:
            y = int(Ai_level[i])
            Ai_attack.append(round(Generation["attack"][x]*2 + y/100+5+10))
            Generation["Ai_health"].append(round(Generation["HP"][x]*2+y/100+y+10))
            Ai_speed.append(round(Generation["speed"][x]*2 + y/100+5+10))
            Ai_defence.append(round(Generation["defence"][x]*2 + y/100+5+10))
        i+=1
    
    Ai_evasion = 100
    Ai_status = ""
    Ai_status_length = 0


    ##establish player stats
    currentPokemon = 0
    Generation["Player_health"] = []
    Player_speed = []
    Player_defence = []
    Player_attack = []
    run_attempts = 0
    Player_evasion = 100
    Player_status = ''
    Player_status_length = 0

    i=0
    for x in gamedata["party"]:
        if x!="":
            Generation["Player_health"].append(round(Generation["HP"][gamedata["Pc"][x]]*2 + gamedata["PcLevel"][x]/100+gamedata["PcLevel"][x]+10))
            Player_speed.append(round(Generation["speed"][gamedata["Pc"][x]]*2 + gamedata["PcLevel"][x]/100+5+10))
            Player_defence.append(round(Generation["defence"][gamedata["Pc"][x]]*2 + gamedata["PcLevel"][x]/100+5+10))
            Player_attack.append(round(Generation["attack"][gamedata["Pc"][x]]*2 + gamedata["PcLevel"][x]/100+5+10))


    print("The Trainer sends out " + Generation["pokemon"][int(Ai_Pokemon[AiCurrentPokemon])])
    print("Go " + Generation["pokemon"][gamedata["Pc"][gamedata["party"][currentPokemon]]] + "!")

    ##start battle
    while True:
        #global Generation
        Player_move= -1
        damage_dealt = 0
        Ai_damage_dealt = 0
        switch = False
        escaped = False
        attacked = False
        caught = False
        paralysed = False
        Ai_paralysed = False
        modifier = 0
        
        
        ##Calculate Ai Moves
        if AiCurrentPokemon != previous_ai:
            i=0
            x = int(Ai_Pokemon[currentPokemon])
            temp = Generation["learnsets"][x].split("-")
            while i<4:
                temp2 =temp[randint(0,len(temp)-1)]
                if temp2 not in Ai_moves:
                    Ai_moves.append(temp2)
                    i+=1
            previous_ai = AiCurrentPokemon 

        ##Player move
        while True:
            print("")
            game = input("What would you like to do? (fight) ")
            print("")
            if game =="help":
                print("Attack - allows you to attack")
                print("Switch - allows you to swap in a new pokemon")
                print("Item - allows you to use a pokeball")
                print("Run - allows you to run away")
                print("Current - shows your currentPokemon")
            
            ##Attack
            elif game == "attack":
                print("")
                print("Moves:")
                moves = gamedata["PcMoves"][gamedata["party"][currentPokemon]].split("-")
                i=0
                for x in moves:
                    print ("#" + str(i) +" " + Generation["moveset"][int(x)] + " Damage: " + str(Generation["damage"][int(x)]) + " Accuracy: " + str(Generation["accuracy"][int(x)]) + " Type: " + Generation["typeMove"][int(x)])
                    i+=1
                while True:
                    game = input("Which attack would you like to do?" )
                    if game == "quit":
                        print("")
                    else:
                        try:
                            if int(game)<=len(moves)-1:
                                Player_move = int(moves[int(game)])
                                print("You choose " + Generation["moveset"][Player_move])
                                attacked = True
                                print("")
                                ##While break
                                break
                            else: 
                                print("invalid response")
                       
                        except:
                            print("invalid response")
                
                ##Function break
                break
            
            ##Swap
            elif game == "switch":
                i=0
                for x in gamedata["party"]:
                    if x!="":
                        print("#" +str(i) + " " + Generation["pokemon"][gamedata["Pc"][x]] + " Health: " + str(Generation["Player_health"][i]) + " Type: " + Generation["type_1"][gamedata["Pc"][x]] + " " + Generation["type_2"][gamedata["Pc"][x]])
                        i+=1
            
                game = input("Which pokemon would you like to put in?" )
                if game == "quit":
                    print("")
                elif game.isnumeric:
                    currentPokemon = int(game)
                    print("You choose " + Generation["pokemon"][gamedata["Pc"][gamedata["party"][currentPokemon]]])
                    switch = True
                    break

                else:
                    print("invalid response")


            ##Run Away
            elif game == "run":
                run_attempts +=1
                F = round((Player_speed[currentPokemon]*32)/(int(Ai_speed[AiCurrentPokemon])/4) + 30 * run_attempts)
                N = randint(0,255)
                if N<F:
                    print("Escaped successfully")
                    print("")
                    escaped = True
                    break
                else:
                    print("You attempted to run... ")
                    print("Escape failed")
                    break

            ##Show current Generation["pokemon"]
            elif game =="current":
                print(Generation["pokemon"][gamedata["Pc"][gamedata["party"][currentPokemon]]])

            elif game =="stats":
                print(Generation["Ai_health"])

            elif game =="die":
                Generation["Player_health"][currentPokemon] = 0
                attacked = True

            elif game =="kill":
                Generation["Ai_health"][AiCurrentPokemon] = 0
                attacked = True

            elif game =="debug":
                pprint(Ai_defence)


        ##Calculate effects
        if Player_status in "healing Sleep poison paralysis":
            if Player_status == "healing":
                Generation["Player_health"][currentPokemon] += round(1/5*Generation["HP"][gamedata["Pc"][currentPokemon]]*2 + gamedata["PcLevel"][currentPokemon]/100+gamedata["PcLevel"][currentPokemon]+10)
                print("Player is healed: " + str(round(1/5*(round(Generation["HP"][gamedata["Pc"][currentPokemon]]*2 + gamedata["PcLevel"][currentPokemon]/100+gamedata["PcLevel"][currentPokemon]+10)))) + "HP")

            elif Player_status == "poison":
                Generation["Player_health"][currentPokemon] -= round(1/16*Generation["HP"][gamedata["Pc"][currentPokemon]]*2 + gamedata["PcLevel"][currentPokemon]/100+gamedata["PcLevel"][currentPokemon]+10)
                print("Player is poisoned: " + str(round(1/16*(round(Generation["HP"][gamedata["Pc"][currentPokemon]]*2 + gamedata["PcLevel"][currentPokemon]/100+gamedata["PcLevel"][currentPokemon]+10)))) + "HP")

            elif Player_status == "Sleep" or Player_status =="paralysis":
                P = randint(0,1)
                if P == 0:
                    print("Player can not move")
                    paralysed=True
            
            ##Reset player statuses
            if Player_status_length>=2:
                Player_status = "None"


        if Ai_status in "healing Sleep poison paralysis":
            if Ai_status == "healing":
                Generation["Ai_health"][AiCurrentPokemon] += round(1/5*Generation["HP"][Ai_Pokemon[AiCurrentPokemon]]*2 + Ai_level[AiCurrentPokemon]/100+Ai_level[AiCurrentPokemon]+10)
                print("Ai is healed: " + str(round(1/5*Generation["HP"][Ai_Pokemon[AiCurrentPokemon]]*2 + Ai_level[AiCurrentPokemon]/100+Ai_level[AiCurrentPokemon]+10) + "HP"))

            elif Ai_status == "poison":
                Generation["Ai_health"] -= round(1/16*Generation["HP"][Ai_Pokemon[AiCurrentPokemon]]*2 + Ai_level[AiCurrentPokemon]/100+Ai_level[AiCurrentPokemon]+10)
                print("Player is poisoned: " + str(round(1/16*Generation["HP"][Ai_Pokemon[AiCurrentPokemon]]*2 + Ai_level[AiCurrentPokemon]/100+Ai_level[AiCurrentPokemon]+10)) + "HP")

            elif Ai_status == "Sleep" or Ai_status =="paralysis":
                P = randint(0,1)
                if P == 0:
                    print("AI can not move")
                    Ai_paralysed=True

            ##Reset Ai statuses
            
            if Ai_status_length>=2:
                Ai_status = "None"


        ##AI Move
        Ai_turn = int(Ai_moves[randint(0,len(Ai_moves)-1)])

        if escaped==True or caught==True:
            break


        elif attacked ==True and paralysed==False:
    
            ##Move effect calculation
        
                ##Check if hits
            P =Generation["accuracy"][Player_move] * (Player_evasion/Ai_evasion)
            hit_chance = randint(0,100)
            if P>=hit_chance:

                ## Regular Moves
                if Generation["moveset"][Player_move] not in ["Hypnosis", "Lovely Kiss", "Sing", "Sleep Powder", "Spore", "Agility", "Double Team", "Teleport", "Recover", "Soft-Boiled", "Haze", "Leech Seed", "Rest", "Substitute", "Acid Armor", "Amnesia", "Barrier", "Conversion", "Defense Curl", "Disable", "Harden", "Withdraw", "Focus Energy", "Growth", "Meditate", "Sharpen", "Swords Dance", "Metronome", "Transform", "Mimic", "Mirror Move", "Poison Gas", "Poison Powder", "Toxic", "Confuse Ray", "Glare", "Stun Spore", "Supersonic", "Thunder Wave", "Splash", "String Shot", "Whirlwind", "Leer", "Screech", "Tail Whip", "Growl", "Light Screen", "Mist", "Reflect", "Roar", "Flash", "Kinesis", "Minimize", "Sand Attack", "Smokescreen"]:    
                    
                    ##innefective move
                    if (Generation["typeMove"][Player_move] in "normal" and (Generation["type_1"][int(Ai_Pokemon[AiCurrentPokemon])] in "rock" or Generation["type_2"][int(Ai_Pokemon[AiCurrentPokemon])] in "rock")) or (Generation["typeMove"][Player_move] in "fire" and (Generation["type_1"][int(Ai_Pokemon[AiCurrentPokemon])] in "firewaterrockdragon" or Generation["type_2"][int(Ai_Pokemon[AiCurrentPokemon])] in "firewaterrockdragon")) or (Generation["typeMove"][Player_move] in "water" and (Generation["type_1"][int(Ai_Pokemon[AiCurrentPokemon])] in "watergrassdragon" or Generation["type_2"][int(Ai_Pokemon[AiCurrentPokemon])] in "watergrassdragon")) or (Generation["typeMove"][Player_move] in "electric" and (Generation["type_1"][int(Ai_Pokemon[AiCurrentPokemon])] in "electricgrassdragon" or Generation["type_2"][int(Ai_Pokemon[AiCurrentPokemon])] in "electricgrassdragon")) or (Generation["typeMove"][Player_move] in "grass" and (Generation["type_1"][int(Ai_Pokemon[AiCurrentPokemon])] in "firegrasspoisonflyingbugdragon" or Generation["type_2"][int(Ai_Pokemon[AiCurrentPokemon])] in "firegrasspoisonflyingbugdragon")) or (Generation["typeMove"][Player_move] in "ice" and (Generation["type_1"][int(Ai_Pokemon[AiCurrentPokemon])] in "fireice" or Generation["type_2"][int(Ai_Pokemon[AiCurrentPokemon])] in "fireice")) or (Generation["typeMove"][Player_move] in "fighting" and (Generation["type_1"][int(Ai_Pokemon[AiCurrentPokemon])] in "poisonflyingpsychicbug" or Generation["type_2"][int(Ai_Pokemon[AiCurrentPokemon])] in "poisonflyingpsychicbug")) or (Generation["typeMove"][Player_move] in "poison" and (Generation["type_1"][int(Ai_Pokemon[AiCurrentPokemon])] in "poisongroundrockghost" or Generation["type_2"][int(Ai_Pokemon[AiCurrentPokemon])] in "poisongroundrockghost")) or (Generation["typeMove"][Player_move] in "ground" and (Generation["type_1"][int(Ai_Pokemon[AiCurrentPokemon])] in "grassbug" or Generation["type_2"][int(Ai_Pokemon[AiCurrentPokemon])] in "grassbug")) or (Generation["typeMove"][Player_move] in "flying" and (Generation["type_1"][int(Ai_Pokemon[AiCurrentPokemon])] in "electricrock" or Generation["type_2"][int(Ai_Pokemon[AiCurrentPokemon])] in "electricrock")) or (Generation["typeMove"][Player_move] in "psychic" and (Generation["type_1"][int(Ai_Pokemon[AiCurrentPokemon])] in "psychic" or Generation["type_2"][int(Ai_Pokemon[AiCurrentPokemon])] in "psychic")) or (Generation["typeMove"][Player_move] in "bug" and (Generation["type_1"][int(Ai_Pokemon[AiCurrentPokemon])] in "firefightingflyingghost" or Generation["type_2"][int(Ai_Pokemon[AiCurrentPokemon])] in "firefightingflyingghost")) or (Generation["typeMove"][Player_move] in "rock" and (Generation["type_1"][int(Ai_Pokemon[AiCurrentPokemon])] in "fightingground" or Generation["type_2"][int(Ai_Pokemon[AiCurrentPokemon])] in "fightingground")):
                        modifier=0.5

                    ##Effective move
                    elif (Generation["typeMove"][Player_move] in "fire" and (Generation["type_1"][int(Ai_Pokemon[AiCurrentPokemon])] in "grassicebug" or Generation["type_2"][int(Ai_Pokemon[AiCurrentPokemon])] in "grassicebug")) or (Generation["typeMove"][Player_move] in "water" and (Generation["type_1"][int(Ai_Pokemon[AiCurrentPokemon])] in "firegroundrock" or Generation["type_2"][int(Ai_Pokemon[AiCurrentPokemon])] in "firegroundrock")) or (Generation["typeMove"][Player_move] in "electric" and (Generation["type_1"][int(Ai_Pokemon[AiCurrentPokemon])] in "waterflying" or Generation["type_2"][int(Ai_Pokemon[AiCurrentPokemon])] in "waterflying")) or (Generation["typeMove"][Player_move] in "grass" and (Generation["type_1"][int(Ai_Pokemon[AiCurrentPokemon])] in "watergroundrock" or Generation["type_2"][int(Ai_Pokemon[AiCurrentPokemon])] in "watergroundrock")) or (Generation["typeMove"][Player_move] in "ice" and (Generation["type_1"][int(Ai_Pokemon[AiCurrentPokemon])] in "grassgroundflyingdragon" or Generation["type_2"][int(Ai_Pokemon[AiCurrentPokemon])] in "grassgroundflyingdragon")) or (Generation["typeMove"][Player_move] in "fighting" and (Generation["type_1"][int(Ai_Pokemon[AiCurrentPokemon])] in "normalicerock" or Generation["type_2"][int(Ai_Pokemon[AiCurrentPokemon])] in "normalicerock")) or (Generation["typeMove"][Player_move] in "poison" and (Generation["type_1"][int(Ai_Pokemon[AiCurrentPokemon])] in "grassbug" or Generation["type_2"][int(Ai_Pokemon[AiCurrentPokemon])] in "grassbug")) or (Generation["typeMove"][Player_move] in "ground" and (Generation["type_1"][int(Ai_Pokemon[AiCurrentPokemon])] in "fireelectricpoisonrock" or Generation["type_2"][int(Ai_Pokemon[AiCurrentPokemon])] in "fireelectricpoisonrock")) or (Generation["typeMove"][Player_move] in "flying" and (Generation["type_1"][int(Ai_Pokemon[AiCurrentPokemon])] in "grassfightingbug" or Generation["type_2"][int(Ai_Pokemon[AiCurrentPokemon])] in "grassfightingbug")) or (Generation["typeMove"][Player_move] in "psychic" and (Generation["type_1"][int(Ai_Pokemon[AiCurrentPokemon])] in "fightingpoison" or Generation["type_2"][int(Ai_Pokemon[AiCurrentPokemon])] in "fightingpoison")) or (Generation["typeMove"][Player_move] in "bug" and (Generation["type_1"][int(Ai_Pokemon[AiCurrentPokemon])] in "grasspoisonpsychic" or Generation["type_2"][int(Ai_Pokemon[AiCurrentPokemon])] in "grasspoisonpsychic")) or (Generation["typeMove"][Player_move] in "rock" and (Generation["type_1"][int(Ai_Pokemon[AiCurrentPokemon])] in "fireiceflyingbug" or Generation["type_2"][int(Ai_Pokemon[AiCurrentPokemon])] in "fireiceflyingbug")) or (Generation["typeMove"][Player_move] in "ghost" and (Generation["type_1"][int(Ai_Pokemon[AiCurrentPokemon])] in "ghost" or Generation["type_2"][int(Ai_Pokemon[AiCurrentPokemon])] in "ghost")) or (Generation["typeMove"][Player_move] in "dragon" and (Generation["type_1"][int(Ai_Pokemon[AiCurrentPokemon])] in "dragon" or Generation["type_2"][int(Ai_Pokemon[AiCurrentPokemon])] in "dragon")):
                        modifier = 2

                    ## No Effect move
                    elif (Generation["typeMove"][Player_move] in "normal" and (Generation["type_1"][int(Ai_Pokemon[AiCurrentPokemon])] in "ghost" or Generation["type_2"][int(Ai_Pokemon[AiCurrentPokemon])] in "ghost")) or (Generation["typeMove"][Player_move] in "electric" and (Generation["type_1"][int(Ai_Pokemon[AiCurrentPokemon])] in "ground" or Generation["type_2"][int(Ai_Pokemon[AiCurrentPokemon])] in "ground")) or (Generation["typeMove"][Player_move] in "fighting" and (Generation["type_1"][int(Ai_Pokemon[AiCurrentPokemon])] in "ghost" or Generation["type_2"][int(Ai_Pokemon[AiCurrentPokemon])] in "ghost")) or (Generation["typeMove"][Player_move] in "ground" and (Generation["type_1"][int(Ai_Pokemon[AiCurrentPokemon])] in "flying" or Generation["type_2"][int(Ai_Pokemon[AiCurrentPokemon])] in "flying")) or (Generation["typeMove"][Player_move] in "ghost" and (Generation["type_1"][int(Ai_Pokemon[AiCurrentPokemon])] in "normalpsychic" or Generation["type_2"][int(Ai_Pokemon[AiCurrentPokemon])] in "normalpsychic")):
                        modifier = 0
                    ##Normal effect move
                    else:
                        modifier = 1

                    damage_dealt = round(((2*gamedata["PcLevel"][gamedata["party"][currentPokemon]]/5+2) * Generation["damage"][Player_move] * (Player_attack[currentPokemon]/Ai_defence[AiCurrentPokemon])/50+2) *modifier)


                    ##Status effects
        
                else:
                    if Generation["moveset"][Player_move] in "Hypnosis Lovely Kiss Sing Sleep Powder Spore":
                        ##sleep
                        Ai_status = "Sleep"
                        Ai_status_length = 0
                        print(Generation["pokemon"][Ai_Pokemon] + " is now asleep")
                        print()
                    

                    elif Generation["moveset"][Player_move] in "Agility Double Team Teleport":
                        ##self-Generation["speed"]
                        Player_speed[currentPokemon] = round(float(Player_speed[currentPokemon])* 1.05)
                        print(Generation["pokemon"][gamedata["Pc"][gamedata["party"][currentPokemon]]] + "'s speed rose")
                        print()
                    
                    
                    elif Generation["moveset"][Player_move] in "Recover Soft-Boiled":
                        ##Self-heal half
                        if Generation["Player_health"][currentPokemon] <= 1/2*(round(Generation["HP"][gamedata["Pc"][currentPokemon]]*2 + gamedata["PcLevel"][currentPokemon]/100+gamedata["PcLevel"][currentPokemon]+10)):
                            Generation["Player_health"][currentPokemon] += 1/2*(round(Generation["HP"][gamedata["Pc"][currentPokemon]]*2 + gamedata["PcLevel"][currentPokemon]/100+gamedata["PcLevel"][currentPokemon]+10))
                        else: 
                            Generation["Player_health"][currentPokemon] = round(Generation["HP"][gamedata["Pc"][currentPokemon]]*2 + gamedata["PcLevel"][currentPokemon]/100+gamedata["PcLevel"][currentPokemon]+10)
                        
                        print(Generation["pokemon"][gamedata["Pc"][gamedata["party"][currentPokemon]]] + "'s healed")
                        print()

                    
                    elif Generation["moveset"][Player_move] in "Haze Leech Seed Rest Substitute":
                        ##self-heal
                        player_status="healing"
                        player_status_length = 0
                        
                        print(Generation["pokemon"][gamedata["Pc"][gamedata["party"][currentPokemon]]] + " is healing itself")
                        print()

                    
                    elif Generation["moveset"][Player_move] in "Acid Armor Amnesia Barrier Conversion Defense Curl Disable Harden Withdraw":
                        ##self-defense
                        Player_defence[currentPokemon] = round(float(Player_defence[currentPokemon])* 1.05)
                        
                        print(Generation["pokemon"][gamedata["Pc"][gamedata["party"][currentPokemon]]] + "'s defense rose")
                        print()

                    
                    elif Generation["moveset"][Player_move] in "Focus Energy Growth Meditate Sharpen Swords Dance":
                        ##self-Generation["attack"]
                        Player_attack[currentPokemon] = round(float(Player_attack[currentPokemon])* 1.05)
                        
                        print(Generation["pokemon"][gamedata["Pc"][gamedata["party"][currentPokemon]]] + "'s attack rose")
                        print()

                    
                    elif Generation["moveset"][Player_move] in "Metronome Transform Mimic Mirror Move":
                        ##random move
                        Player_move = randint(0,len(Generation["moveset"])-1)
                        if Generation["moveset"][Player_move] not in "Acid Armor Agility Amnesia Barrier Confuse Ray Conversion Defense Curl Disable Double Team Flash Focus Energy Glare Growl Growth Harden Haze Hypnosis Kinesis Leech Seed Leer Light Screen Lovely Kiss Meditate Metronome Mimic Minimize Mirror Move Mist Poison Gas Poison Powder Recover Reflect Rest Roar Sand Attack Screech Sharpen Sing Sleep Powder Smokescreen Soft-Boiled Splash Spore String Shot Stun Spore Substitute Supersonic Swords Dance Tail Whip Teleport Thunder Wave Toxic Transform Whirlwind Withdraw":    
                            print(Generation["pokemon"][gamedata["Pc"][gamedata["party"][currentPokemon]]] + " uses " + Generation["moveset"][Player_move])
                            ##innefective move
                            if (Generation["typeMove"][Player_move] == "normal" and (Generation["type_1"][Ai_Pokemon] == "rock" or Generation["type_2"][Ai_Pokemon] == "rock")) or (Generation["typeMove"][Player_move] == "fire" and (Generation["type_1"][Ai_Pokemon] in "firewaterrockdragon" or Generation["type_2"][Ai_Pokemon] in "firewaterrockdragon")) or (Generation["typeMove"][Player_move] == "water" and (Generation["type_1"][Ai_Pokemon] in "watergrassdragon" or Generation["type_2"][Ai_Pokemon] in "watergrassdragon")) or (Generation["typeMove"][Player_move] == "electric" and (Generation["type_1"][Ai_Pokemon] in "electricgrassdragon" or Generation["type_2"][Ai_Pokemon] in "electricgrassdragon")) or (Generation["typeMove"][Player_move] == "grass" and (Generation["type_1"][Ai_Pokemon] in "firegrasspoisonflyingbugdragon" or Generation["type_2"][Ai_Pokemon] in "firegrasspoisonflyingbugdragon")) or (Generation["typeMove"][Player_move] == "ice" and (Generation["type_1"][Ai_Pokemon] in "fireice" or Generation["type_2"][Ai_Pokemon] in "fireice")) or (Generation["typeMove"][Player_move] == "fighting" and (Generation["type_1"][Ai_Pokemon] in "poisonflyingpsychicbug" or Generation["type_2"][Ai_Pokemon] in "poisonflyingpsychicbug")) or (Generation["typeMove"][Player_move] == "poison" and (Generation["type_1"][Ai_Pokemon] in "poisongroundrockghost" or Generation["type_2"][Ai_Pokemon] in "poisongroundrockghost")) or (Generation["typeMove"][Player_move] == "ground" and (Generation["type_1"][Ai_Pokemon] in "grassbug" or Generation["type_2"][Ai_Pokemon] in "grassbug")) or (Generation["typeMove"][Player_move] == "flying" and (Generation["type_1"][Ai_Pokemon] in "electricrock" or Generation["type_2"][Ai_Pokemon] in "electricrock")) or (Generation["typeMove"][Player_move] == "psychic" and (Generation["type_1"][Ai_Pokemon] in "psychic" or Generation["type_2"][Ai_Pokemon] in "psychic")) or (Generation["typeMove"][Player_move] == "bug" and (Generation["type_1"][Ai_Pokemon] in "firefightingflyingghost" or Generation["type_2"][Ai_Pokemon] in "firefightingflyingghost")) or (Generation["typeMove"][Player_move] == "rock" and (Generation["type_1"][Ai_Pokemon] in "fightingground" or Generation["type_2"][Ai_Pokemon] in "fightingground")):
                                print("not very effective")
                                modifier=0.5

                            elif (Generation["typeMove"][Player_move] == "fire" and (Generation["type_1"][Ai_Pokemon] == "grassicebug" or Generation["type_2"][Ai_Pokemon] == "grassicebug")) or (Generation["typeMove"][Player_move] == "water" and (Generation["type_1"][Ai_Pokemon] == "firegroundrock" or Generation["type_2"][Ai_Pokemon] == "firegroundrock")) or (Generation["typeMove"][Player_move] == "electric" and (Generation["type_1"][Ai_Pokemon] == "waterflying" or Generation["type_2"][Ai_Pokemon] == "waterflying")) or (Generation["typeMove"][Player_move] == "grass" and (Generation["type_1"][Ai_Pokemon] == "watergroundrock" or Generation["type_2"][Ai_Pokemon] == "watergroundrock")) or (Generation["typeMove"][Player_move] == "ice" and (Generation["type_1"][Ai_Pokemon] == "grassgroundflyingdragon" or Generation["type_2"][Ai_Pokemon] == "grassgroundflyingdragon")) or (Generation["typeMove"][Player_move] == "fighting" and (Generation["type_1"][Ai_Pokemon] == "normalicerock" or Generation["type_2"][Ai_Pokemon] == "normalicerock")) or (Generation["typeMove"][Player_move] == "poison" and (Generation["type_1"][Ai_Pokemon] == "grassbug" or Generation["type_2"][Ai_Pokemon] == "grassbug")) or (Generation["typeMove"][Player_move] == "ground" and (Generation["type_1"][Ai_Pokemon] == "fireelectricpoisonrock" or Generation["type_2"][Ai_Pokemon] == "fireelectricpoisonrock")) or (Generation["typeMove"][Player_move] == "flying" and (Generation["type_1"][Ai_Pokemon] == "grassfightingbug" or Generation["type_2"][Ai_Pokemon] == "grassfightingbug")) or (Generation["typeMove"][Player_move] == "psychic" and (Generation["type_1"][Ai_Pokemon] == "fightingpoison" or Generation["type_2"][Ai_Pokemon] == "fightingpoison")) or (Generation["typeMove"][Player_move] == "bug" and (Generation["type_1"][Ai_Pokemon] == "grasspoisonpsychic" or Generation["type_2"][Ai_Pokemon] == "grasspoisonpsychic")) or (Generation["typeMove"][Player_move] == "rock" and (Generation["type_1"][Ai_Pokemon] == "fireiceflyingbug" or Generation["type_2"][Ai_Pokemon] == "fireiceflyingbug")) or (Generation["typeMove"][Player_move] == "ghost" and (Generation["type_1"][Ai_Pokemon] == "ghost" or Generation["type_2"][Ai_Pokemon] == "ghost")) or (Generation["typeMove"][Player_move] == "dragon" and (Generation["type_1"][Ai_Pokemon] == "dragon" or Generation["type_2"][Ai_Pokemon] == "dragon")):
                                print("Very effective")
                                modifier = 2

                            elif (Generation["typeMove"][Player_move] == "normal" and (Generation["type_1"][Ai_Pokemon] == "ghost" or Generation["type_2"][Ai_Pokemon] == "ghost")) or (Generation["typeMove"][Player_move] == "electric" and (Generation["type_1"][Ai_Pokemon] == "ground" or Generation["type_2"][Ai_Pokemon] == "ground")) or (Generation["typeMove"][Player_move] == "fighting" and (Generation["type_1"][Ai_Pokemon] == "ghost" or Generation["type_2"][Ai_Pokemon] == "ghost")) or (Generation["typeMove"][Player_move] == "ground" and (Generation["type_1"][Ai_Pokemon] == "flying" or Generation["type_2"][Ai_Pokemon] == "flying")) or (Generation["typeMove"][Player_move] == "ghost" and (Generation["type_1"][Ai_Pokemon] == "normalpsychic" or Generation["type_2"][Ai_Pokemon] == "normalpsychic")):
                                print("No effect")
                                modifier = 0

                            else:
                                print("yes")
                                modifier = 1
                            
                            damage_dealt = round(((2*gamedata["PcLevel"][gamedata["party"][currentPokemon]]/5+2) * Generation["damage"][Player_move] * (Player_attack[currentPokemon]/Ai_defence)/50+2) *modifier)
                            Generation["Ai_health"]-=damage_dealt
                            print("Damage dealt: " + str(damage_dealt) + " " + Generation["pokemon"][Ai_Pokemon[AiCurrentPokemon]] + " has " + str(Generation["Ai_health"][AiCurrentPokemon]) + " left")

                        else:
                            print("No effect")

                    
                    elif Generation["moveset"][Player_move] in "Poison Gas Poison Powder Toxic":
                        ##poison
                        Ai_status = "poison"
                        Ai_status_length = 0
                        
                        print(Generation["pokemon"][int(Ai_Pokemon[AiCurrentPokemon])] + " is now poisoned")
                        print()
                    

                    elif Generation["moveset"][Player_move] in "Confuse Ray Glare Stun Spore Supersonic Thunder Wave":
                        ##paralysis
                        Ai_status = "paralysis"
                        Ai_status_length = 0
                        print(Generation["pokemon"][int(Ai_Pokemon[AiCurrentPokemon])] + " is now paralysed")
                        print()


                    elif Generation["moveset"][Player_move] in "Splash":
                        ##none
                        print("Has no effect whatsoever.")
                        print()
                    

                    elif Generation["moveset"][Player_move] in "String Shot Whirlwind":
                        ##enemy-Generation["speed"]
                        Ai_speed[AiCurrentPokemon]= round(float(Ai_speed[AiCurrentPokemon])* 0.95)
                        print(Generation["pokemon"][int(Ai_Pokemon[AiCurrentPokemon])] + " is now slower")
                        print()

                    
                    elif Generation["moveset"][Player_move] in "Leer Screech Tail Whip":
                        ##enemy-Generation["defence"]
                        Ai_defence[AiCurrentPokemon]= round(float(Ai_defence[AiCurrentPokemon])* 0.95)
                        print(Generation["pokemon"][int(Ai_Pokemon[AiCurrentPokemon])] + "'s defence fell")
                        print()

                    
                    elif Generation["moveset"][Player_move] in "Growl Light Screen Mist Reflect Roar":
                        ##enemy-Generation["attack"]
                        Ai_attack[AiCurrentPokemon]= round(float(Ai_attack[AiCurrentPokemon])* 0.95)
                        print(Generation["pokemon"][int(Ai_Pokemon[AiCurrentPokemon])] + "'s attack fell")
                        print()
                
                    elif Generation["moveset"][Player_move] in "Flash Kinesis Minimize Sand Attack Smokescreen":
                        ##enemy-Generation["accuracy"]
                        Ai_evasion[AiCurrentPokemon]= round(float(Ai_evasion[AiCurrentPokemon])* 0.95)
                        print(Generation["pokemon"][int(Ai_Pokemon[AiCurrentPokemon])] + "'s accuracy fell")
                        print()

            else:
                print(Generation["pokemon"][gamedata["Pc"][gamedata["party"][currentPokemon]]] + " misses.")
                print()

        
        ## Ai Move calculation
        if Ai_paralysed == False:
            A_modifier = 1
            P =Generation["accuracy"][Ai_turn] * (Ai_evasion/Player_evasion)
            hit_chance = randint(0,100)

            if P>=hit_chance or Generation["moveset"][Ai_turn] in ["Hypnosis", "Lovely Kiss", "Sing", "Sleep Powder", "Spore", "Agility", "Double Team", "Teleport", "Recover", "Soft-Boiled", "Haze", "Leech Seed", "Rest", "Substitute", "Acid Armor", "Amnesia", "Barrier", "Conversion", "Defense Curl", "Disable", "Harden", "Withdraw", "Focus Energy", "Growth", "Meditate", "Sharpen", "Swords Dance", "Metronome", "Transform", "Mimic", "Mirror Move", "Poison Gas", "Poison Powder", "Toxic", "Confuse Ray", "Glare", "Stun Spore", "Supersonic", "Thunder Wave", "Splash", "String Shot", "Whirlwind", "Leer", "Screech", "Tail Whip", "Growl", "Light Screen", "Mist", "Reflect", "Roar", "Flash", "Kinesis", "Minimize", "Sand Attack", "Smokescreen"]:

                ## Regular Moves
                if Generation["moveset"][Ai_turn] not in ["Hypnosis", "Lovely Kiss", "Sing", "Sleep Powder", "Spore", "Agility", "Double Team", "Teleport", "Recover", "Soft-Boiled", "Haze", "Leech Seed", "Rest", "Substitute", "Acid Armor", "Amnesia", "Barrier", "Conversion", "Defense Curl", "Disable", "Harden", "Withdraw", "Focus Energy", "Growth", "Meditate", "Sharpen", "Swords Dance", "Metronome", "Transform", "Mimic", "Mirror Move", "Poison Gas", "Poison Powder", "Toxic", "Confuse Ray", "Glare", "Stun Spore", "Supersonic", "Thunder Wave", "Splash", "String Shot", "Whirlwind", "Leer", "Screech", "Tail Whip", "Growl", "Light Screen", "Mist", "Reflect", "Roar", "Flash", "Kinesis", "Minimize", "Sand Attack", "Smokescreen"]:    
                    
                    ##innefective move
                    if Generation["moveset"][Player_move] not in ["Hypnosis", "Lovely Kiss", "Sing", "Sleep Powder", "Spore", "Agility", "Double Team", "Teleport", "Recover", "Soft-Boiled", "Haze", "Leech Seed", "Rest", "Substitute", "Acid Armor", "Amnesia", "Barrier", "Conversion", "Defense Curl", "Disable", "Harden", "Withdraw", "Focus Energy", "Growth", "Meditate", "Sharpen", "Swords Dance", "Metronome", "Transform", "Mimic", "Mirror Move", "Poison Gas", "Poison Powder", "Toxic", "Confuse Ray", "Glare", "Stun Spore", "Supersonic", "Thunder Wave", "Splash", "String Shot", "Whirlwind", "Leer", "Screech", "Tail Whip", "Growl", "Light Screen", "Mist", "Reflect", "Roar", "Flash", "Kinesis", "Minimize", "Sand Attack", "Smokescreen"]:    
                        
                        ##innefective move
                        if (Generation["typeMove"][Player_move] in "normal" and (Generation["type_1"][int(Ai_Pokemon[AiCurrentPokemon])] in "rock" or Generation["type_2"][int(Ai_Pokemon[AiCurrentPokemon])] in "rock")) or (Generation["typeMove"][Player_move] in "fire" and (Generation["type_1"][int(Ai_Pokemon[AiCurrentPokemon])] in "firewaterrockdragon" or Generation["type_2"][int(Ai_Pokemon[AiCurrentPokemon])] in "firewaterrockdragon")) or (Generation["typeMove"][Player_move] in "water" and (Generation["type_1"][int(Ai_Pokemon[AiCurrentPokemon])] in "watergrassdragon" or Generation["type_2"][int(Ai_Pokemon[AiCurrentPokemon])] in "watergrassdragon")) or (Generation["typeMove"][Player_move] in "electric" and (Generation["type_1"][int(Ai_Pokemon[AiCurrentPokemon])] in "electricgrassdragon" or Generation["type_2"][int(Ai_Pokemon[AiCurrentPokemon])] in "electricgrassdragon")) or (Generation["typeMove"][Player_move] in "grass" and (Generation["type_1"][int(Ai_Pokemon[AiCurrentPokemon])] in "firegrasspoisonflyingbugdragon" or Generation["type_2"][int(Ai_Pokemon[AiCurrentPokemon])] in "firegrasspoisonflyingbugdragon")) or (Generation["typeMove"][Player_move] in "ice" and (Generation["type_1"][int(Ai_Pokemon[AiCurrentPokemon])] in "fireice" or Generation["type_2"][int(Ai_Pokemon[AiCurrentPokemon])] in "fireice")) or (Generation["typeMove"][Player_move] in "fighting" and (Generation["type_1"][int(Ai_Pokemon[AiCurrentPokemon])] in "poisonflyingpsychicbug" or Generation["type_2"][int(Ai_Pokemon[AiCurrentPokemon])] in "poisonflyingpsychicbug")) or (Generation["typeMove"][Player_move] in "poison" and (Generation["type_1"][int(Ai_Pokemon[AiCurrentPokemon])] in "poisongroundrockghost" or Generation["type_2"][int(Ai_Pokemon[AiCurrentPokemon])] in "poisongroundrockghost")) or (Generation["typeMove"][Player_move] in "ground" and (Generation["type_1"][int(Ai_Pokemon[AiCurrentPokemon])] in "grassbug" or Generation["type_2"][int(Ai_Pokemon[AiCurrentPokemon])] in "grassbug")) or (Generation["typeMove"][Player_move] in "flying" and (Generation["type_1"][int(Ai_Pokemon[AiCurrentPokemon])] in "electricrock" or Generation["type_2"][int(Ai_Pokemon[AiCurrentPokemon])] in "electricrock")) or (Generation["typeMove"][Player_move] in "psychic" and (Generation["type_1"][int(Ai_Pokemon[AiCurrentPokemon])] in "psychic" or Generation["type_2"][int(Ai_Pokemon[AiCurrentPokemon])] in "psychic")) or (Generation["typeMove"][Player_move] in "bug" and (Generation["type_1"][int(Ai_Pokemon[AiCurrentPokemon])] in "firefightingflyingghost" or Generation["type_2"][int(Ai_Pokemon[AiCurrentPokemon])] in "firefightingflyingghost")) or (Generation["typeMove"][Player_move] in "rock" and (Generation["type_1"][int(Ai_Pokemon[AiCurrentPokemon])] in "fightingground" or Generation["type_2"][int(Ai_Pokemon[AiCurrentPokemon])] in "fightingground")):
                            A_modifier=0.5

                        ##Effective move
                        elif (Generation["typeMove"][Player_move] in "fire" and (Generation["type_1"][int(Ai_Pokemon[AiCurrentPokemon])] in "grassicebug" or Generation["type_2"][int(Ai_Pokemon[AiCurrentPokemon])] in "grassicebug")) or (Generation["typeMove"][Player_move] in "water" and (Generation["type_1"][int(Ai_Pokemon[AiCurrentPokemon])] in "firegroundrock" or Generation["type_2"][int(Ai_Pokemon[AiCurrentPokemon])] in "firegroundrock")) or (Generation["typeMove"][Player_move] in "electric" and (Generation["type_1"][int(Ai_Pokemon[AiCurrentPokemon])] in "waterflying" or Generation["type_2"][int(Ai_Pokemon[AiCurrentPokemon])] in "waterflying")) or (Generation["typeMove"][Player_move] in "grass" and (Generation["type_1"][int(Ai_Pokemon[AiCurrentPokemon])] in "watergroundrock" or Generation["type_2"][int(Ai_Pokemon[AiCurrentPokemon])] in "watergroundrock")) or (Generation["typeMove"][Player_move] in "ice" and (Generation["type_1"][int(Ai_Pokemon[AiCurrentPokemon])] in "grassgroundflyingdragon" or Generation["type_2"][int(Ai_Pokemon[AiCurrentPokemon])] in "grassgroundflyingdragon")) or (Generation["typeMove"][Player_move] in "fighting" and (Generation["type_1"][int(Ai_Pokemon[AiCurrentPokemon])] in "normalicerock" or Generation["type_2"][int(Ai_Pokemon[AiCurrentPokemon])] in "normalicerock")) or (Generation["typeMove"][Player_move] in "poison" and (Generation["type_1"][int(Ai_Pokemon[AiCurrentPokemon])] in "grassbug" or Generation["type_2"][int(Ai_Pokemon[AiCurrentPokemon])] in "grassbug")) or (Generation["typeMove"][Player_move] in "ground" and (Generation["type_1"][int(Ai_Pokemon[AiCurrentPokemon])] in "fireelectricpoisonrock" or Generation["type_2"][int(Ai_Pokemon[AiCurrentPokemon])] in "fireelectricpoisonrock")) or (Generation["typeMove"][Player_move] in "flying" and (Generation["type_1"][int(Ai_Pokemon[AiCurrentPokemon])] in "grassfightingbug" or Generation["type_2"][int(Ai_Pokemon[AiCurrentPokemon])] in "grassfightingbug")) or (Generation["typeMove"][Player_move] in "psychic" and (Generation["type_1"][int(Ai_Pokemon[AiCurrentPokemon])] in "fightingpoison" or Generation["type_2"][int(Ai_Pokemon[AiCurrentPokemon])] in "fightingpoison")) or (Generation["typeMove"][Player_move] in "bug" and (Generation["type_1"][int(Ai_Pokemon[AiCurrentPokemon])] in "grasspoisonpsychic" or Generation["type_2"][int(Ai_Pokemon[AiCurrentPokemon])] in "grasspoisonpsychic")) or (Generation["typeMove"][Player_move] in "rock" and (Generation["type_1"][int(Ai_Pokemon[AiCurrentPokemon])] in "fireiceflyingbug" or Generation["type_2"][int(Ai_Pokemon[AiCurrentPokemon])] in "fireiceflyingbug")) or (Generation["typeMove"][Player_move] in "ghost" and (Generation["type_1"][int(Ai_Pokemon[AiCurrentPokemon])] in "ghost" or Generation["type_2"][int(Ai_Pokemon[AiCurrentPokemon])] in "ghost")) or (Generation["typeMove"][Player_move] in "dragon" and (Generation["type_1"][int(Ai_Pokemon[AiCurrentPokemon])] in "dragon" or Generation["type_2"][int(Ai_Pokemon[AiCurrentPokemon])] in "dragon")):
                            A_modifier = 2

                        ## No Effect move
                        elif (Generation["typeMove"][Player_move] in "normal" and (Generation["type_1"][int(Ai_Pokemon[AiCurrentPokemon])] in "ghost" or Generation["type_2"][int(Ai_Pokemon[AiCurrentPokemon])] in "ghost")) or (Generation["typeMove"][Player_move] in "electric" and (Generation["type_1"][int(Ai_Pokemon[AiCurrentPokemon])] in "ground" or Generation["type_2"][int(Ai_Pokemon[AiCurrentPokemon])] in "ground")) or (Generation["typeMove"][Player_move] in "fighting" and (Generation["type_1"][int(Ai_Pokemon[AiCurrentPokemon])] in "ghost" or Generation["type_2"][int(Ai_Pokemon[AiCurrentPokemon])] in "ghost")) or (Generation["typeMove"][Player_move] in "ground" and (Generation["type_1"][int(Ai_Pokemon[AiCurrentPokemon])] in "flying" or Generation["type_2"][int(Ai_Pokemon[AiCurrentPokemon])] in "flying")) or (Generation["typeMove"][Player_move] in "ghost" and (Generation["type_1"][int(Ai_Pokemon[AiCurrentPokemon])] in "normalpsychic" or Generation["type_2"][int(Ai_Pokemon[AiCurrentPokemon])] in "normalpsychic")):
                            A_modifier = 0

                        ##Normal effect move
                        else:
                            A_modifier = 1

                        Ai_damage_dealt = math.ceil(((2*int(Ai_level[AiCurrentPokemon])/5+2) * Generation["damage"][Ai_turn] * (int(Ai_attack[AiCurrentPokemon])/Player_defence[currentPokemon])/50+2) *A_modifier)


                    ##Status effects
        
                ## Special Moves
                else:
                    A_modifier = 1
                    if Generation["moveset"][Ai_turn] in "Hypnosis Lovely Kiss Sing Sleep Powder Spore":
                        ##sleep
                        Player_status = "Sleep"
                        Player_status_length = 0
                        print("You are now  asleep")

                    elif Generation["moveset"][Ai_turn] in "Agility Double Team Teleport":
                        ##self-Generation["speed"]
                        Ai_speed[AiCurrentPokemon] = round(float(Ai_speed)* 1.05)
                        print("The Ai's speed rose")

                    elif Generation["moveset"][Ai_turn] in "Recover Soft-Boiled":
                        ##Self-heal half
                        if Generation["Ai_health"][AiCurrentPokemon] <= round(1/2*(Generation["HP"][Ai_Pokemon[AiCurrentPokemon]]*2 + int(Ai_level[AiCurrentPokemon])/100+int(Ai_level[AiCurrentPokemon])+10)):
                            Generation["Ai_health"][AiCurrentPokemon]= Generation["Ai_health"][AiCurrentPokemon] + round(1/2*(Generation["HP"][Ai_Pokemon[AiCurrentPokemon]]*2 + int(Ai_level[AiCurrentPokemon])/100+int(Ai_level[AiCurrentPokemon])+10))
                        else: 
                            Generation["Ai_health"][AiCurrentPokemon] = round(Generation["HP"][Ai_Pokemon[AiCurrentPokemon]]*2 + int(Ai_level[AiCurrentPokemon])/100+int(Ai_level[AiCurrentPokemon])+10)

                        print("Ai Heals itself")

                    elif Generation["moveset"][Ai_turn] in "Haze Leech Seed Rest Substitute":
                        ##self-heal
                        Ai_status="healing"
                        Ai_status_length = 0
                        print("The Ai is healing itself")

                    elif Generation["moveset"][Ai_turn] in "Acid Armor Amnesia Barrier Conversion Defense Curl Disable Harden Withdraw":
                        ##self-defense
                        Ai_defence[AiCurrentPokemon]  = round(float(Ai_defence[AiCurrentPokemon])* 1.05)

                        print("The Ai's defence rose")

                    elif Generation["moveset"][Ai_turn] in "Focus Energy Growth Meditate Sharpen Swords Dance":
                        ##self-Generation["attack"]
                        Ai_attack[AiCurrentPokemon]  = round(float(Ai_attack[AiCurrentPokemon])* 1.05)
                        print("The Ai's attack rose")

                    elif Generation["moveset"][Ai_turn] in "Metronome Transform Mimic Mirror Move":
                        ##random move
                        Ai_turn = randint(0,len(Generation["moveset"][AiCurrentPokemon])-1)
                        if Generation["moveset"][Ai_turn] not in "Acid Armor Agility Amnesia Barrier Confuse Ray Conversion Defense Curl Disable Double Team Flash Focus Energy Glare Growl Growth Harden Haze Hypnosis Kinesis Leech Seed Leer Light Screen Lovely Kiss Meditate Metronome Mimic Minimize Mirror Move Mist Poison Gas Poison Powder Recover Reflect Rest Roar Sand Attack Screech Sharpen Sing Sleep Powder Smokescreen Soft-Boiled Splash Spore String Shot Stun Spore Substitute Supersonic Swords Dance Tail Whip Teleport Thunder Wave Toxic Transform Whirlwind Withdraw":    
                            
                            
                            ##innefective move
                            if (Generation["typeMove"][Ai_turn] in "normal" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "rock" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "rock")) or (Generation["typeMove"][Ai_turn] in "fire" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "firewaterrockdragon" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "firewaterrockdragon")) or (Generation["typeMove"][Ai_turn] in "water" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "watergrassdragon" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "watergrassdragon")) or (Generation["typeMove"][Ai_turn] in "electric" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "electricgrassdragon" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "electricgrassdragon")) or (Generation["typeMove"][Ai_turn] in "grass" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "firegrasspoisonflyingbugdragon" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "firegrasspoisonflyingbugdragon")) or (Generation["typeMove"][Ai_turn] in "ice" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "fireice" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "fireice")) or (Generation["typeMove"][Ai_turn] in "fighting" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "poisonflyingpsychicbug" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "poisonflyingpsychicbug")) or (Generation["typeMove"][Ai_turn] in "poison" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "poisongroundrockghost" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "poisongroundrockghost")) or (Generation["typeMove"][Ai_turn] in "ground" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "grassbug" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "grassbug")) or (Generation["typeMove"][Ai_turn] in "flying" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "electricrock" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "electricrock")) or (Generation["typeMove"][Ai_turn] in "psychic" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "psychic" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "psychic")) or (Generation["typeMove"][Ai_turn] in "bug" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "firefightingflyingghost" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "firefightingflyingghost")) or (Generation["typeMove"][Ai_turn] in "rock" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "fightingground" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "fightingground")):                        
                                A_modifier=0.5

                            ##Effective move
                            elif (Generation["typeMove"][Ai_turn] in "fire" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "grassicebug" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "grassicebug")) or (Generation["typeMove"][Ai_turn] in "water" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "firegroundrock" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "firegroundrock")) or (Generation["typeMove"][Ai_turn] in "electric" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "waterflying" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "waterflying")) or (Generation["typeMove"][Ai_turn] in "grass" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "watergroundrock" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "watergroundrock")) or (Generation["typeMove"][Ai_turn] in "ice" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "grassgroundflyingdragon" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "grassgroundflyingdragon")) or (Generation["typeMove"][Ai_turn] in "fighting" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "normalicerock" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "normalicerock")) or (Generation["typeMove"][Ai_turn] in "poison" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "grassbug" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "grassbug")) or (Generation["typeMove"][Ai_turn] in "ground" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "fireelectricpoisonrock" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "fireelectricpoisonrock")) or (Generation["typeMove"][Ai_turn] in "flying" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "grassfightingbug" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "grassfightingbug")) or (Generation["typeMove"][Ai_turn] in "psychic" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "fightingpoison" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "fightingpoison")) or (Generation["typeMove"][Ai_turn] in "bug" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "grasspoisonpsychic" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "grasspoisonpsychic")) or (Generation["typeMove"][Ai_turn] in "rock" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "fireiceflyingbug" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "fireiceflyingbug")) or (Generation["typeMove"][Ai_turn] in "ghost" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "ghost" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "ghost")) or (Generation["typeMove"][Ai_turn] in "dragon" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "dragon" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "dragon")):                        
                                A_modifier = 2

                            ## No Effect move
                            elif (Generation["typeMove"][Ai_turn] in "normal" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "ghost" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "ghost")) or (Generation["typeMove"][Ai_turn] in "electric" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "ground" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "ground")) or (Generation["typeMove"][Ai_turn] in "fighting" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "ghost" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "ghost")) or (Generation["typeMove"][Ai_turn] in "ground" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "flying" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "flying")) or (Generation["typeMove"][Ai_turn] in "ghost" and (Generation["type_1"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "normalpsychic" or Generation["type_2"][gamedata["Pc"][gamedata["party"][currentPokemon]]] in "normalpsychic")):
                                A_modifier = 0

                            ##Normal effect move
                            else:
                                A_modifier = 1

                            Ai_damage_dealt = round(((2*Ai_level[AiCurrentPokemon]/5+2) * Generation["damage"][Ai_turn] * (Ai_attack[AiCurrentPokemon]/Player_defence[currentPokemon])/50+2) *A_modifier)

                        else:
                            A_modifier = 0 

                    elif Generation["moveset"][Ai_turn] in "Poison Gas Poison Powder Toxic":
                        ##poison
                        Player_status = "poison"
                        Player_status_length = 0
                        print("You are poisoned")

                    elif Generation["moveset"][Ai_turn] in "Confuse Ray Glare Stun Spore Supersonic Thunder Wave":
                        ##paralysis
                        Player_status = "paralysis"
                        Player_status_length = 0
                        print("You are now paralysed")

                    elif Generation["moveset"][Ai_turn] in "Splash":
                        ##none
                        print("Has no effect whatsoever.")

                    elif Generation["moveset"][Ai_turn] in "String Shot Whirlwind":
                        ##enemy-Generation["speed"]
                        Player_speed[currentPokemon] = round(float(Player_speed[currentPokemon])*0.95)
                        print("Your speed fell")

                    elif Generation["moveset"][Ai_turn] in "Leer Screech Tail Whip":
                        ##enemy-Generation["defence"]
                        Player_defence[currentPokemon]= round(float(Player_defence[currentPokemon])*0.95)
                        print("Your defence fell")

                    elif Generation["moveset"][Ai_turn] in "Growl Light Screen Mist Reflect Roar":
                        ##enemy-Generation["attack"]
                        Player_attack[currentPokemon]= round(float(Player_attack[currentPokemon])*0.95)
                        print("Your attack fell")

                    elif Generation["moveset"][Player_move] in "Flash Kinesis Minimize Sand Attack Smokescreen":
                        ##enemy-Generation["accuracy"]
                        Player_evasion[currentPokemon]= round(float(Player_evasion[currentPokemon])*0.95)
                        print("Your accuracy fell")

            else:
                print(Generation["pokemon"][int(Ai_Pokemon[AiCurrentPokemon])] + " misses.")
                print()

        else:
            A_modifier = 1
        ##Move order
        
        if Player_speed[currentPokemon]>Ai_speed[AiCurrentPokemon] and Player_move!=-1:
            print(Generation["pokemon"][gamedata["Pc"][gamedata["party"][currentPokemon]]] + " uses " + Generation["moveset"][Player_move])
            Generation["Ai_health"][AiCurrentPokemon]-=damage_dealt
        
            if modifier == 0.5:
                print("Not very effective")
            elif modifier == 2:
                print("Very Effective")
            elif modifier == 0:
                print("No effect")

            print("Damage dealt: " + str(damage_dealt) + " " + Generation["pokemon"][int(Ai_Pokemon[AiCurrentPokemon])] + " has " + str(Generation["Ai_health"][AiCurrentPokemon]) + " left")
            print()

            if int(Generation["Ai_health"][AiCurrentPokemon])>0:
                print(Generation["pokemon"][int(Ai_Pokemon[AiCurrentPokemon])] + " uses " + Generation["moveset"][Ai_turn])
                Generation["Player_health"][currentPokemon]-=Ai_damage_dealt
                
                if A_modifier == 0.5:
                    print("Not very effective")
                elif A_modifier == 2:
                    print("Very Effective")
                elif A_modifier == 0:
                    print("No effect")

                print("Damage dealt: " + str(Ai_damage_dealt) + " " + Generation["pokemon"][gamedata["Pc"][gamedata["party"][currentPokemon]]] + " has " + str(Generation["Player_health"][currentPokemon]) + " left")
                
                
                if Generation["Player_health"][currentPokemon] <= 0:    
                    ##Choose next pokemon
                    print(Generation["pokemon"][gamedata["Pc"][gamedata["party"][currentPokemon]]] + " Fainted")
                    i=0
                    for x in Generation["Player_health"]:
                        if x>0:
                            currentPokemon=i
                            print("Go " + Generation["pokemon"][gamedata["Pc"][gamedata["party"][currentPokemon]]] + "!")
                            break
                        i+=1
                    if Generation["Player_health"][currentPokemon] <= 0:
                        print("You black out")
                        break

            else:
                print("The " + Generation["pokemon"][int(Ai_Pokemon[AiCurrentPokemon])] + " Fainted!" )
                Ai_moves = []
                ### Calculate XP
                xp_recieved = round((1000*int(Ai_level[AiCurrentPokemon])/5)*(((2*int(Ai_level[AiCurrentPokemon])+10)**2.5)/(int(Ai_level[AiCurrentPokemon]) + gamedata["PcLevel"][gamedata["party"][currentPokemon]] + 10)**2.5+1))

                print("xp Earned: " + str(xp_recieved))
                gamedata["xp"][gamedata["party"][currentPokemon]]+=xp_recieved

                ##Required xp to level up
                xp_table = [8,19,37,61,91,127,169,217,271,331,397,469,547,631,721,817,919,1027,1141,1261,1387,1519,1657,1801,1951,2107,2269,2437,2611,2791,2977,3169,3367,3571,3781,3997,4219,4447,4681,4921,5167,5419,5677,5941,6211,6487,6769,7057,7351,7651,7957,8269,8587,8911,9241,9577,9919,10267,10621,10981,11347,11719,12097,12481,12871,13267,13669,14077,14491,14911,15337,15769,16207,16651,17101,17557,18019,18487,18961,19441,19927,20419,20917,21421,21931,22447,22969,23497,24031,24571,25117,25669,26227,26791,27361,27937,28519,29107,29701,9999999999999999999999]
                
                ##Level up
                if gamedata["xp"][gamedata["party"][currentPokemon]] >= xp_table[gamedata["PcLevel"][gamedata["party"][currentPokemon]]-1]:
                    
                    gamedata["xp"][gamedata["party"][currentPokemon]] -= xp_table[gamedata["PcLevel"][gamedata["party"][currentPokemon]]-1]
                    gamedata["PcLevel"][gamedata["party"][currentPokemon]]+=1
                    
                    print(Generation["pokemon"][gamedata["Pc"][gamedata["party"][currentPokemon]]] + " Levelled Up! They are now level " + str(gamedata["PcLevel"][gamedata["party"][currentPokemon]]))
                    
                    ##New move
                    if gamedata["PcLevel"][gamedata["party"][currentPokemon]]%2 ==0:
                        temp = Generation["learnsets"][gamedata["Pc"][gamedata["party"][currentPokemon]]].split("-")

                        while True:
                            new_move = randint(0,len(temp)-1)
                            
                            if temp[new_move] not in gamedata["PcMoves"][gamedata["party"][currentPokemon]]:
                                
                                print(Generation["pokemon"][gamedata["Pc"][gamedata["party"][currentPokemon]]] + " would like to learn the move:")
                                print(Generation["moveset"][int(temp[new_move])] + " Damage: " + str(Generation["damage"][int(temp[new_move])]) + " Accuracy: " + str(Generation["accuracy"][int(temp[new_move])]) + " Type: " + Generation["typeMove"][int(temp[new_move])])

                                game = 0
                                ##Learn move
                                while game != "yes" and game != "no":
                                    game = input("would you like to learn it? ")
                                    if game == 'no':
                                        print(Generation["pokemon"][gamedata["Pc"][gamedata["party"][currentPokemon]]] + " does not learn the move")

                                    elif game == "yes":
                                        i=0

                                        gamedata["PcMoves"][gamedata["party"][currentPokemon]].split("-")
                                        for x in gamedata["PcMoves"][gamedata["party"][currentPokemon]].split("-"):
                                            print("#"+str(i)+ " " + Generation["moveset"][int(x)] + " Damage: " + str(Generation["damage"][int(x)]) + " Accuracy: " + str(Generation["accuracy"][int(x)]) + " Type: " + Generation["typeMove"][int(x)])
                                            i+=1

                                        remove_move = int(input("Which move would you like to forget? "))
                                        
                                        if remove_move>len(gamedata["PcMoves"][gamedata["party"][currentPokemon]].split("-"))-1:
                                            gamedata["PcMoves"][gamedata["party"][currentPokemon]] += "-" + temp[new_move]
                                        
                                        else:
                                            banned_move = gamedata["PcMoves"][gamedata["party"][currentPokemon]].split("-")[remove_move]
                                            new_list = []

                                            for x in gamedata["PcMoves"][gamedata["party"][currentPokemon]].split("-"):
                                                if banned_move != x:
                                                    new_list.append(x)
                                                else:
                                                    new_list.append(temp[new_move])
                                            
                                            x = "-".join(new_list)

                                            gamedata["PcMoves"][gamedata["party"][currentPokemon]] = x
                                    break
                                break

                    ##Evolve
                    if ((gamedata["PcLevel"][gamedata["party"][currentPokemon]] == 25 or gamedata["PcLevel"][gamedata["party"][currentPokemon]] == 50 or gamedata["PcLevel"][gamedata["party"][currentPokemon]] >= 75) and Generation["next_evolve"][gamedata["Pc"][gamedata["party"][currentPokemon]]] != 0 ):

                        gamedata["pc"][gamedata["party"][currentPokemon]]=Generation["next_evolve"][gamedata["Pc"][gamedata["party"][currentPokemon]]]
                        print( Generation["pokemon"][gamedata["Pc"][gamedata["party"][currentPokemon]]-1] + " Evolves! They are now " + Generation["pokemon"][gamedata["Pc"][gamedata["party"][currentPokemon]]])

                ##next Generation["pokemon"]
                i=0
                for x in Generation["Ai_health"]:
                    if int(x)>0 and int(Ai_Pokemon[AiCurrentPokemon])<1000:
                        print(Generation["pokemon"][int(Ai_Pokemon[AiCurrentPokemon])] + " faints.")
                        AiCurrentPokemon=i
                        print("Go " + Generation["pokemon"][int(Ai_Pokemon[AiCurrentPokemon])] + "!")
                        break
                    i+=1

                if Generation["Ai_health"][AiCurrentPokemon]<=0:
                    gamedata["BattleWon"] +=1
                    print("Trainer is out of pokemon. You win!")
                    gamedata["money"] += 1000
                    print("You earned $1000! You now have $" + str(gamedata["money"]))
                    save()
                    break

        ##Ai Moves first
        else:
            print(Generation["pokemon"][int(Ai_Pokemon[AiCurrentPokemon])] + " uses " + Generation["moveset"][Ai_turn])
            Generation["Player_health"][currentPokemon]-=Ai_damage_dealt
                
            if A_modifier == 0.5:
                print("Not very effective")
            elif A_modifier == 2:
                print("Very Effective")
            elif A_modifier == 0:
                print("No effect")

            print("Damage dealt: " + str(Ai_damage_dealt) + " " + Generation["pokemon"][gamedata["Pc"][gamedata["party"][currentPokemon]]] + " has " + str(Generation["Player_health"][currentPokemon]) + " left")
            print()

            if Generation["Player_health"][currentPokemon]>0 and Player_move!=-1:
                print(Generation["pokemon"][gamedata["Pc"][gamedata["party"][currentPokemon]]] + " uses " + Generation["moveset"][Player_move])
                Generation["Ai_health"][AiCurrentPokemon]-=damage_dealt
                
                if modifier == 0.5:
                    print("Not very effective")
                elif modifier == 2:
                    print("Very Effective")
                elif modifier == 0:
                    print("No effect")

                print("Damage dealt: " + str(damage_dealt) + " " + Generation["pokemon"][int(Ai_Pokemon[AiCurrentPokemon])] + " has " + str(Generation["Ai_health"][AiCurrentPokemon]) + " left")

                if int(Generation["Ai_health"][AiCurrentPokemon])<=0:
                    print("The " + Generation["pokemon"][int(Ai_Pokemon[AiCurrentPokemon])] + " Fainted!" )
                    Ai_moves = []
                    ### Calculate XP
                    xp_recieved = round((1000*int(Ai_level[AiCurrentPokemon])/5)*(((2*int(Ai_level[AiCurrentPokemon])+10)**2.5)/(int(Ai_level[AiCurrentPokemon]) + gamedata["PcLevel"][gamedata["party"][currentPokemon]] + 10)**2.5+1))

                    print("xp Earned: " + str(xp_recieved))
                    gamedata["xp"][gamedata["party"][currentPokemon]]+=xp_recieved

                    ##Required xp to level up
                    xp_table = [8,19,37,61,91,127,169,217,271,331,397,469,547,631,721,817,919,1027,1141,1261,1387,1519,1657,1801,1951,2107,2269,2437,2611,2791,2977,3169,3367,3571,3781,3997,4219,4447,4681,4921,5167,5419,5677,5941,6211,6487,6769,7057,7351,7651,7957,8269,8587,8911,9241,9577,9919,10267,10621,10981,11347,11719,12097,12481,12871,13267,13669,14077,14491,14911,15337,15769,16207,16651,17101,17557,18019,18487,18961,19441,19927,20419,20917,21421,21931,22447,22969,23497,24031,24571,25117,25669,26227,26791,27361,27937,28519,29107,29701,9999999999999999999999]
                    
                    ##Level up
                    if gamedata["xp"][gamedata["party"][currentPokemon]] >= xp_table[gamedata["PcLevel"][gamedata["party"][currentPokemon]]-1]:
                        
                        gamedata["xp"][gamedata["party"][currentPokemon]] -= xp_table[gamedata["PcLevel"][gamedata["party"][currentPokemon]]-1]
                        gamedata["PcLevel"][gamedata["party"][currentPokemon]]+=1
                        
                        print(Generation["pokemon"][gamedata["Pc"][gamedata["party"][currentPokemon]]] + " Levelled Up! They are now level " + str(gamedata["PcLevel"][gamedata["party"][currentPokemon]]))
                        
                        ##New move
                        if gamedata["PcLevel"][gamedata["party"][currentPokemon]]%2 ==0:
                            temp = Generation["learnsets"][gamedata["Pc"][gamedata["party"][currentPokemon]]].split("-")

                            while True:
                                new_move = randint(0,len(temp)-1)
                                
                                if temp[new_move] not in gamedata["PcMoves"][gamedata["party"][currentPokemon]]:
                                    
                                    print(Generation["pokemon"][gamedata["Pc"][gamedata["party"][currentPokemon]]] + " would like to learn the move:")
                                    print(Generation["moveset"][int(temp[new_move])] + " Damage: " + str(Generation["damage"][int(temp[new_move])]) + " Accuracy: " + str(Generation["accuracy"][int(temp[new_move])]) + " Type: " + Generation["typeMove"][int(temp[new_move])])

                                    game = 0
                                    ##Learn move
                                    while game != "yes" and game != "no":
                                        game = input("would you like to learn it? ")
                                        if game == 'no':
                                            print(Generation["pokemon"][gamedata["Pc"][gamedata["party"][currentPokemon]]] + " does not learn the move")

                                        elif game == "yes":
                                            i=0

                                            gamedata["PcMoves"][gamedata["party"][currentPokemon]].split("-")
                                            for x in gamedata["PcMoves"][gamedata["party"][currentPokemon]].split("-"):
                                                print("#"+str(i)+ " " + Generation["moveset"][int(x)] + " Damage: " + str(Generation["damage"][int(x)]) + " Accuracy: " + str(Generation["accuracy"][int(x)]) + " Type: " + Generation["typeMove"][int(x)])
                                                i+=1

                                            remove_move = int(input("Which move would you like to forget? "))
                                            if remove_move>len(gamedata["PcMoves"][gamedata["party"][currentPokemon]].split("-"))-1:
                                                gamedata["PcMoves"][gamedata["party"][currentPokemon]] += "-" + temp[new_move]
                                            
                                            else:
                                                banned_move = gamedata["PcMoves"][gamedata["party"][currentPokemon]].split("-")[remove_move]
                                                new_list = []

                                                for x in gamedata["PcMoves"][gamedata["party"][currentPokemon]].split("-"):
                                                    if banned_move != x:
                                                        new_list.append(x)
                                                    else:
                                                        new_list.append(temp[new_move])
                
                                                x = "-".join(new_list)

                                                gamedata["PcMoves"][gamedata["party"][currentPokemon]] = x
                                        break
                                    break


                        ##Evolve
                        if ((gamedata["PcLevel"][gamedata["party"][currentPokemon]] == 25 or gamedata["PcLevel"][gamedata["party"][currentPokemon]] == 50 or gamedata["PcLevel"][gamedata["party"][currentPokemon]] >= 75) and Generation["next_evolve"][gamedata["Pc"][gamedata["party"][currentPokemon]]] != 0 ):

                            gamedata["pc"][gamedata["party"][currentPokemon]]=Generation["next_evolve"][gamedata["Pc"][gamedata["party"][currentPokemon]]]
                            print( Generation["pokemon"][gamedata["Pc"][gamedata["party"][currentPokemon]]-1] + " Evolves! They are now " + Generation["pokemon"][gamedata["Pc"][gamedata["party"][currentPokemon]]])
                        

                    ##next Generation["pokemon"]
                    
                    i=0
                    for x in Generation["Ai_health"]:
                        if int(x)>0 and int(Ai_Pokemon[AiCurrentPokemon])<1000:
                            print(Generation["pokemon"][int(Ai_Pokemon[AiCurrentPokemon])] + " faints.")
                            AiCurrentPokemon=i
                            print("Go " + Generation["pokemon"][int(Ai_Pokemon[AiCurrentPokemon])] + "!")
                            break
                        i+=1

                    if Generation["Ai_health"][AiCurrentPokemon]<=0:
                        gamedata["BattleWon"]+=1
                        print("Trainer is out of pokemon. You win!")
                        gamedata["money"] += 1000
                        print("You earned $1000! You now have $" + str(gamedata["money"]))
                        save()
                        break


            elif Generation["Player_health"][currentPokemon] <= 0:
                ##Choose next Generation["pokemon"]
                print(Generation["pokemon"][gamedata["Pc"][gamedata["party"][currentPokemon]]] + " Fainted")
                i=0
                for x in Generation["Player_health"]:
                    if x>0:
                        currentPokemon=i
                        print("Go " + Generation["pokemon"][gamedata["Pc"][gamedata["party"][currentPokemon]]] + "!")
                        break
                    i+=1
                if Generation["Player_health"][currentPokemon] <= 0:
                    print("You black out")
                    break

    
        Player_status_length+=1
        Ai_status_length+=1


firstload()
###START GAME (finally)
print("")
print("Game has started")

while True:
    game = input("What would you like to do? (general) ")
    if game =="help":
        print("wild - spawns a random pokemon")
        print("trainer - starts a trainer fight (gym battle)")
        print("save - saves your progress (only one save can be stored at one time")
        print("load - loads your last save. (all unsaved progress will be lost)")
        print("quit - will quit your game (all unsaved progress will be lost)")
        print("buy - will buy a pokeball for $200")
        print("pc - will allow you to view and change the pokemon in your PC")
        print("party - will allow you to view your party pokemon and their stats")
        print("location - will show you your location, what pokemon can spawn there, and allow you to travel to other towns (as long as you have won enough battles to do so)")
        print("money - will show you your current money")
        print("order - allows you to rearrange your party")

    elif game == "wild":
        PokeBattle()

    elif game == "trainer":
        TrainerBattle()

    elif game == "save":
        save()

    elif game == "load":
        load()

    elif game == "quit":
        game=input("Would you like to save first? ")
        if game =="yes":
            save()
            break
        elif game == "no":
            break

    elif game == "buy":
        buy()

    elif game == "pc":
        pc()

    elif game =="party":
        Party()

    elif game =="location":
        LocationFind()

    elif game =="money":
        print("you have $" + str(gamedata["money"]))

    elif game =="debug":
        debug()

    elif game =="order":
        PartyOrder()

    else:
        print("invalid response (input 'help' for a list of commands. This is available on almost any screen)")
import json
from pprint import pprint
from random import randint
import math

## Variable set up
global pokemon
pokemon = ["Bulbasaur", "Ivysaur", "Venusaur", "Charmander", "Charmeleon", "Charizard", "Squirtle", "Wartortle", "Blastoise", "Caterpie", "Metapod", "Butterfree", "Weedle", "Kakuna", "Beedrill", "Pidgey", "Pidgeotto", "Pidgeot", "Rattata", "Raticate", "Spearow", "Fearow", "Ekans", "Arbok", "Pikachu", "Raichu", "Sandshrew", "Sandslash", "Nidoran♀", "Nidorina", "Nidoqueen", "Nidoran♂", "Nidorino", "Nidoking", "Clefairy", "Clefable", "Vulpix", "Ninetales", "Jigglypuff", "Wigglytuff", "Zubat", "Golbat", "Oddish", "Gloom", "Vileplume", "Paras", "Parasect", "Venonat", "Venomoth", "Diglett", "Dugtrio", "Meowth", "Persian", "Psyduck", "Golduck", "Mankey", "Primeape", "Growlithe", "Arcanine", "Poliwag", "Poliwhirl", "Poliwrath", "Abra", "Kadabra", "Alakazam", "Machop", "Machoke", "Machamp", "Bellsprout", "Weepinbell", "Victreebel", "Tentacool", "Tentacruel", "Geodude", "Graveler", "Golem", "Ponyta", "Rapidash", "Slowpoke", "Slowbro", "Magnemite", "Magneton", "Farfetch’d", "Doduo", "Dodrio", "Seel", "Dewgong", "Grimer", "Muk", "Shellder", "Cloyster", "Gastly", "Haunter", "Gengar", "Onix", "Drowzee", "Hypno", "Krabby", "Kingler", "Voltorb", "Electrode", "Exeggcute", "Exeggutor", "Cubone", "Marowak", "Hitmonlee", "Hitmonchan", "Lickitung", "Koffing", "Weezing", "Rhyhorn", "Rhydon", "Chansey", "Tangela", "Kangaskhan", "Horsea", "Seadra", "Goldeen", "Seaking", "Staryu", "Starmie", "Mr. Mime", "Scyther", "Jynx", "Electabuzz", "Magmar", "Pinsir", "Tauros", "Magikarp", "Gyarados", "Lapras", "Ditto", "Eevee", "Vaporeon", "Jolteon", "Flareon", "Porygon", "Omanyte", "Omastar", "Kabuto", "Kabutops", "Aerodactyl", "Snorlax", "Articuno", "Zapdos", "Moltres", "Dratini", "Dragonair", "Dragonite", "Mewtwo", "Mew"]
global type_1 
type_1 = ["grass","grass","grass","fire","fire","fire","water","water","water","bug","bug","bug","bug","bug","bug","normal","normal","normal","normal","normal","normal","normal","poison","poison","electric","electric","ground","ground","poison","poison","poison","poison","poison","poison","fairy","fairy","fire","fire","normal","normal","poison","poison","grass","grass","grass","bug","bug","bug","bug","ground","ground","normal","normal","water","water","fighting","fighting","fire","fire","water","water","water","psychic","psychic","psychic","fighting","fighting","fighting","grass","grass","grass","water","water","rock","rock","rock","fire","fire","water","water","electric","electric","normal","normal","normal","water","water","poison","poison","water","water","ghost","ghost","ghost","rock","psychic","psychic","water","water","electric","electric","grass","grass","ground","ground","fighting","fighting","normal","poison","poison","ground","ground","normal","grass","normal","water","water","water","water","water","water","psychic","bug","ice","electric","fire","bug","normal","water","water","water","normal","normal","water","electric","fire","normal","rock","rock","rock","rock","rock","normal","ice","electric","fire","dragon","dragon","dragon","psychic","psychic"]
global type_2
type_2 = ["poison","poison","poison","none","none","flying","none","none","none","none","none","flying","poison","poison","poison","flying","flying","flying","none","none","flying","flying","none","none","none","none","none","none","none","none","ground","none","none","ground","none","none","none","none","fairy","fairy","flying","flying","poison","poison","poison","grass","grass","poison","poison","none","none","none","none","none","none","none","none","none","none","none","none","fighting","none","none","none","none","none","none","poison","poison","poison","poison","poison","ground","ground","ground","none","none","psychic","psychic","steel","steel","flying","flying","flying","none","ice","none","none","none","ice","poison","poison","poison","ground","none","none","none","none","none","none","psychic","psychic","none","none","none","none","none","none","none","rock","rock","none","none","none","none","none","none","none","none","psychic","fairy","flying","psychic","none","none","none","none","none","flying","ice","none","none","none","none","none","none","water","water","water","water","flying","none","flying","flying","flying","none","none","flying","none","none"]
global evolve
evolve =[0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,0,1,0,1,0,1,0,1,0,1,2,0,1,2,0,1,0,1,0,1,0,1,0,1,2,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,2,0,1,2,0,1,2,0,1,2,0,1,0,1,2,0,1,0,1,0,1,0,0,1,0,1,0,1,0,1,0,1,2,0,0,1,0,1,0,1,0,1,0,1,0,1,0,0,1,0,1,0,0,0,0,1,0,1,0,1,0,0,0,0,0,0,0,0,1,0,0,0,1,1,1,1,0,0,1,0,1,0,0,0,0,0,1,0,0,0]

##stats
global HP
HP =[45,60,80,39,58,78,44,59,79,45,50,60,40,45,65,40,63,83,30,55,40,65,30,60,35,60,50,75,55,70,90,46,61,81,70,95,38,73,115,140,40,75,45,60,75,35,60,60,70,10,35,40,65,50,80,40,65,55,90,40,65,90,25,40,55,70,80,90,50,65,80,40,80,40,55,80,50,65,90,95,25,50,52,35,60,65,90,80,105,30,50,30,45,60,35,60,85,30,55,40,60,60,95,50,60,50,50,90,40,65,80,105,250,65,105,30,55,45,80,30,60,40,70,65,65,65,65,75,20,95,130,48,55,130,65,65,65,35,70,30,60,80,160,90,90,90,41,61,91,106,100]
global attack
attack = [49,62,82,52,64,84,48,63,83,30,20,45,35,25,80,45,60,80,56,81,60,90,60,85,55,90,75,100,47,62,82,57,72,92,45,70,41,76,45,70,45,80,50,65,80,70,95,55,65,55,80,45,70,52,82,80,105,70,110,50,65,85,20,35,50,80,100,130,75,90,105,40,70,80,95,110,85,100,65,75,35,60,65,85,110,45,70,80,105,65,90,35,50,65,45,48,73,105,130,30,50,40,95,50,80,120,105,55,65,90,85,130,5,55,95,40,65,67,92,45,75,45,110,50,83,95,125,100,10,125,85,48,55,65,65,130,60,40,60,80,115,105,110,85,90,100,64,84,134,110,100]
global defence
defence = [49,63,83,43,58,78,65,80,100,35,55,50,30,50,40,40,55,75,35,60,30,65,44,69,30,55,85,110,52,67,87,40,57,77,48,73,40,75,20,45,35,70,55,70,85,55,80,50,60,25,50,35,60,48,78,35,60,45,80,40,65,95,15,30,45,50,70,80,35,50,65,35,65,100,115,130,55,70,65,110,70,95,55,45,70,55,80,50,75,100,180,30,45,60,160,45,70,90,115,50,70,80,85,95,110,53,79,75,95,120,95,120,5,115,80,70,95,60,65,55,85,65,80,35,57,57,100,95,55,79,80,48,50,60,60,60,70,100,125,90,105,65,65,100,85,90,45,65,95,90,100]
global speed
speed = [45,60,80,65,80,100,43,58,78,45,30,70,50,35,75,56,71,91,72,97,70,100,55,80,90,100,40,65,41,56,76,50,65,85,35,60,65,100,20,45,55,90,30,40,50,25,30,45,90,95,120,90,115,55,85,70,95,60,95,90,90,70,90,105,120,35,45,55,40,55,70,70,100,20,35,45,90,105,15,30,45,70,60,75,100,45,70,25,50,40,70,80,95,110,70,42,67,50,75,100,140,40,55,35,45,87,76,30,35,60,25,40,50,60,90,60,85,63,68,85,115,90,105,95,105,93,85,110,80,81,60,48,55,65,130,65,40,35,55,55,80,130,30,85,100,90,50,70,80,130,100]
global Player_health
Player_health =[0,0,0,0,0,0]
global Ai_health
Ai_health = 0


##moves
global moveset
moveset = ["Absorb", "Acid", "Acid Armor", "Agility", "Amnesia", "Aurora Beam", "Barrage", "Barrier", "Bide", "Bind", "Bite", "Blizzard", "Body Slam", "Bone Club", "Bonemerang", "Bubble", "Bubble Beam", "Clamp", "Comet Punch", "Confuse Ray", "Confusion", "Constrict", "Conversion", "Counter", "Crabhammer", "Cut", "Defense Curl", "Dig", "Disable", "Dizzy Punch", "Double Kick", "Double Slap", "Double Team", "Double-Edge", "Dragon Rage", "Dream Eater", "Drill Peck", "Earthquake", "Egg Bomb", "Ember", "Explosion", "Fire Blast", "Fire Punch", "Fire Spin", "Fissure", "Flamethrower", "Flash", "Fly", "Focus Energy", "Fury Attack", "Fury Swipes", "Glare", "Growl", "Growth", "Guillotine", "Gust", "Harden", "Haze", "Headbutt", "High Jump Kick", "Horn Attack", "Horn Drill", "Hydro Pump", "Hyper Beam", "Hyper Fang", "Hypnosis", "Ice Beam", "Ice Punch", "Jump Kick", "Karate Chop", "Kinesis", "Leech Life", "Leech Seed", "Leer", "Lick", "Light Screen", "Lovely Kiss", "Low Kick", "Meditate", "Mega Drain", "Mega Kick", "Mega Punch", "Metronome", "Mimic", "Minimize", "Mirror Move", "Mist", "Night Shade", "Pay Day", "Peck", "Petal Dance", "Pin Missile", "Poison Gas", "Poison Powder", "Poison Sting", "Pound", "Psybeam", "Psychic", "Psywave", "Quick Attack", "Rage", "Razor Leaf", "Razor Wind", "Recover", "Reflect", "Rest", "Roar", "Rock Slide", "Rock Throw", "Rolling Kick", "Sand Attack", "Scratch", "Screech", "Seismic Toss", "Self-Destruct", "Sharpen", "Sing", "Skull Bash", "Sky Attack", "Slam", "Slash", "Sleep Powder", "Sludge", "Smog", "Smokescreen", "Soft-Boiled", "Solar Beam", "Sonic Boom", "Spike Cannon", "Splash", "Spore", "Stomp", "Strength", "String Shot", "Struggle", "Stun Spore", "Submission", "Substitute", "Super Fang", "Supersonic", "Surf", "Swift", "Swords Dance", "Tackle", "Tail Whip", "Take Down", "Teleport", "Thrash", "Thunder", "Thunder Punch", "Thunder Shock", "Thunder Wave", "Thunderbolt", "Toxic", "Transform", "Tri Attack", "Twineedle", "Vice Grip", "Vine Whip", "Water Gun", "Waterfall", "Whirlwind", "Wing Attack", "Withdraw", "Wrap",]
global typeMove
typeMove =["grass","poison","poison","psychic","psychic","ice","normal","psychic","normal","normal","dark","ice","normal","ground","ground","water","water","water","normal","ghost","psychic","normal","normal","fighting","water","normal","normal","ground","normal","normal","fighting","normal","normal","normal","dragon","psychic","flying","ground","normal","fire","normal","fire","fire","fire","ground","fire","normal","flying","normal","normal","normal","normal","normal","normal","normal","flying","normal","ice","normal","fighting","normal","normal","water","normal","normal","psychic","ice","ice","fighting","fighting","psychic","bug","grass","normal","ghost","psychic","normal","fighting","psychic","grass","normal","normal","normal","normal","normal","flying","ice","ghost","normal","flying","grass","bug","poison","poison","poison","normal","psychic","psychic","psychic","normal","normal","grass","normal","normal","psychic","psychic","normal","rock","rock","fighting","ground","normal","normal","fighting","normal","normal","normal","normal","flying","normal","normal","grass","poison","poison","normal","normal","grass","normal","normal","normal","grass","normal","normal","bug","normal","grass","fighting","normal","normal","normal","water","normal","normal","normal","normal","normal","psychic","normal","electric","electric","electric","electric","electric","poison","normal","normal","bug","normal","grass","water","water","normal","flying","water","normal",]
global damage
damage = [20,40,0,0,0,65,15,0,0,15,60,110,85,65,50,40,65,35,18,0,50,10,0,0,100,50,0,80,0,70,30,15,0,120,0,100,80,100,100,40,250,110,75,35,0,90,0,90,0,15,18,0,0,0,0,40,0,0,70,130,65,0,110,150,80,0,90,75,100,50,0,80,0,0,30,0,0,0,0,40,120,80,0,0,0,0,0,0,40,35,120,25,0,0,15,40,65,90,0,40,20,55,80,0,0,0,0,75,50,60,0,40,0,0,200,0,0,130,140,80,70,0,65,30,0,0,120,0,20,0,0,65,80,0,50,0,80,0,0,0,90,60,0,40,0,90,0,120,110,75,40,0,90,0,0,80,25,55,45,40,80,0,60,0,15]
global accuracy
accuracy = [100,100,150,0,150,100,85,150,0,85,100,70,100,85,90,100,100,85,85,100,100,100,150,100,90,95,150,100,100,100,100,85,150,100,100,100,100,100,75,100,100,85,100,85,150,100,100,95,150,85,80,100,100,150,0,100,150,0,100,90,100,150,80,90,90,60,100,100,95,100,80,100,90,100,100,150,75,100,150,100,75,85,150,0,150,0,150,100,100,100,100,95,90,75,100,100,100,100,80,100,100,95,100,150,0,150,0,90,90,85,100,100,85,100,100,150,55,100,90,75,100,75,100,70,100,150,100,90,100,150,100,100,100,95,100,75,80,150,90,55,100,100,150,100,100,85,150,100,70,100,100,90,100,90,150,100,100,100,100,100,100,150,100,150,90]
global learnsets
learnsets =["52-143-72-158-93-101-53-121-126","52-72-143-72-158-93-101-53-121-126","52-72-143-158-72-158-93-101-53-121-126","52-111-39-73-100-120-45-43","39-52-111-39-73-100-120-45-43","39-52-73-111-39-73-100-120-45-43","143-144-15-163-159-10-16-95-58-62-117","15-143-144-163-144-15-163-159-10-16-95-58-62-117","4-15-40-46-143-144-163-144-15-163-159-10-16-95-58-62-117","133-143","133-143","56","20-20-93-135-121-139-161-96","94-133","56-94-133","49-49-48-156-100-91-3","55-110-99-161-162-3-85","55-99-110-143-110-55-99-85-162-109-161-3-3-102","55-99-110-110-99-161-162-3-85","143-144-99-64-48-138","99-143-144-99-64-48-138","52-89-73-49-85-36-3","52-73-89-73-49-85-36-3","73-164-94-10-51-112-1","73-94-164-94-10-51-112-1","52-150-151-99-141-3-148","52-150-151-3-99-141-148","111-110-120-94-141-50","110-111-110-120-94-141-50","52-143-111-94-144-10-50-30","52-111-143-111-94-144-10-50-30","12-111-143-144-111-94-12","73-143-60-94-48-49-61-30","60-73-143-60-94-48-49-61-30","60-94-143-147-60-94-147-30-48-49-61-73","52-95-116-31-84-82-26-75","31-82-84-116-26-52-75-95","39-144-99-106-19-45-43","39-99-106-144-19-43-45","116-95-28-26-31-105-12-33","26-28-31-116-12-33-95-105","71-139-10-19-162-57","10-71-112-139-10-19-162-57","0-93-135-121-1-90-126","0-93-135-93-135-121-1-90-126","1-90-121-135-93-135-121-0-126","111-135-71-130-120-53","71-111-135-135-71-130-120-53","28-143-93-71-135-96-121-97","111-52-27-110-120-37","27-52-111-52-27-110-120-37","52-111-10-88-112-50-120","10-52-111-112-10-88-112-50-120","111-144-28-20-50-62","28-111-144-144-28-20-50-62","73-111-69-50-48-113-147","50-69-73-111-69-50-48-113-147","10-106-39-73-145-3-45","39-73-106-145-3-10-45","15-65-159-31-12-4-62","15-65-159-65-159-31-12-4-62","12-31-65-159-65-159-4-15-62","146","20-28-146-20-28-96-103-97-104","20-28-146-20-28-96-103-97-104","69-77-73-48-113-136","69-73-77-77-73-48-113-136","69-73-77-77-73-48-113-136","53-158-164-93-121-135-1-101-119","53-158-164-164-93-121-135-1-101-119","1-101-121-135-164-93-121-53-119-158","1-139-164-94-159-21-7-112-62","1-139-164-139-164-94-159-21-7-112-62","143-26-108-114-56-37-40","26-143-26-108-114-56-37-40","26-143-26-108-114-56-37-40","39-144-131-52-43-145-3","39-52-131-144-144-131-52-43-145-3","39-52-131-144-144-131-52-43-145-3","20-28-58-52-159-4-97","20-28-58-28-58-52-159-163-4-97","143-127-150-139-151-141-112","127-143-150-127-150-139-151-141-112","89-110-73-49-142-3-120","89-52-49-36-100-155-3","49-52-89-52-49-36-100-155-3","58-52-5-105-145-66","5-52-58-52-5-105-145-66","28-95-92-84-122-56-112-2","28-92-95-92-84-122-56-112-2","143-163-139-17-5-73-66","5-17-139-163-128-66-73-143","19-74-87-65-35","19-74-87-65-35","19-74-87-65-35","112-143-9-108-100-119-56","65-95-28-20-58-92-97-78","20-28-65-95-28-20-58-92-97-78","15-73-157-54-131-24-56","15-73-157-157-54-131-24-56","112-143-127-114-75-141-40","112-127-143-127-114-75-141-40","6-65-104-72-135-93-126-121","72-93-104-121-126-135-6-65-131","13-52-73-48-147-14-100","13-48-52-73-73-48-147-14-100","30-78-109-68-48-59-80","3-18-42-67-149-81-23","139-164-131-28-26-119-112","123-143-122-124-114-57-40","122-123-143-122-124-114-57-40","60-131-144-49-61-73-145","49-60-131-144-131-144-49-61-73-145","31-95-116-52-84-26-75-33","9-21-0-93-135-121-119-53","18-100-10-144-81-73-29","15-124-73-159-3-62","15-124-124-73-159-3-62","89-144-139-60-49-160-61-3","89-139-144-139-60-49-160-61-3","143-159-56-103-141-84-75-62","56-143-159-62-75-84-103-141","7-20-20-75-31-78-137","99-73-48-32-120-142-3","76-95-74-31-67-12-147-11","73-99-150-112-149-75-148","39-73-19-42-124-123-45","157-113-54-48-56-120-142","143-131-144-73-100-145","129-143","10-34-62-73-10-34-73-62-63-129-143","52-159-116-86-12-19-66-62","154","110-143-99-144-10-145","99-110-143-159-99-159-144-10-2-57-86-62-145","99-110-143-150-99-150-144-151-30-3-91-148-10-145","39-99-110-143-99-39-144-10-73-43-100-45-145","22-115-143-96-103-3-155","159-163-60-73-128-62","60-159-163-60-73-128-62","56-111-0-120-73-62","0-56-111-0-120-73-62","3-162-139-10-145-63","4-58-105-12-56-33-63","66-89-11-3-86","36-150-148-3-75","43-89-73-3-118","73-164-151-3-119-34-63","73-151-164-151-3-119-34-63","3-73-151-164-151-3-119-34-63","20-28-97-141-7-97-103-86-4","95-154-81-82-97"]


##location
global location
location = ["Pallet Town", "Viridian City", "Pewter City", "Cerulean City", "Vermilion City", "Lavender Town", "Celadon City", "Fuchsia City", "Saffron City", "Cinnabar Island"]
##(which pokemon can spawn)
global LocationPokemon
LocationPokemon=["59-71-119-15-18","15-18-20-55-28-31-12-9-10-13-16","15-20-38-18-26-55-40-73-45-34-22","53-97-117-68-9-10-62-12-13-15-42-51-89","89-97-20-22-49-50-18-99-60-78-40-73-65-94","15-22-55-57-36-42-68-51","60-78-91-92-103-18-19-20-83-21-89-128-97-117-71","97-117-118-128-129-53-78-146-28-29-31-32-101-45-46-83-47-48-110-112-122-126-114-127-68-69-43-131-19-16-119-115","128","108-109-87-88-36-57-76-125-80-81-24-25-99-124-144-40-41-53-54-78-79-85-86-98-116-119-143-23-26-27-131-73-74-65-66-94-104-145-63-100-111-39-112-96-63-149-150"]


##Trainer battles
##(152 represents no pokemon)
global TrainerPokemon
TrainerPokemon=["73-94-152-152-152-152","119-120-152-152-152-152","99-24-25-152-152-152","70-113-44-152-152-152","108-88-108-109-152-152","63-121-48-64-152-152","57-76-77-58","110-50-30-33-111-152","86-90-79-123-130-152","94-106-105-94-67-152","93-41-92-23-93-152","129-147-147-141-148-152","17-64-11-129-102-5"]
##(What moves a pokemon can do. The number represents the position of the pokemon)
global TrainerMove1
TrainerMove1=["143-26","143-159","143-112-127","164-93-121-101","143-123-122-124","28-96-103-97","39-73-145-3","131-144-49-60","52-5-105-145","108-100-119-56","19-87-65-35","62-34-73-63","162-85-118-161"]
global TrainerMove2
TrainerMove2=["143-112-8-9","143-159-56-16","150-151-52-99","9-21","28-92-84-122","20-7-75-31","144-131-52-43","52-27-110-120","139-17-5-128","67-42-149-23","139-19-162-57","3-119-34-63","96-97-104-103"]
global TrainerMove3
TrainerMove3=["","","152-150-151-52","93-79-121-90","143-123-122-124","93-71-135-96","144-131-52-43","111-144-94-12","159-52-163-4","68-48-68-80","19-87-65-35","3-119-34-63","73-144-49-61"]
global TrainerMove4
TrainerMove4=["","","","","123-122-153-114","96-103-98-104","106-39-145-41","143-60-94-147","31-67-12-147","108-100-119-56","10-51-112-1","139-145-10-63","34-62-63-73"]
global TrainerMove5
TrainerMove5=["","","","","","","","131-144-44-61","12-19-62-11","73-48-44-136","19-87-153-35","3-119-7-63","65-6-131"]
global TrainerMove6		
TrainerMove6=["","","","","","","","","","","","","41-100-120-43"]
global TrainerLevel
TrainerLevel = ["12-14-0-0-0-0", "18-21-0-0-0-0","21-18-24-0-0-0","29-24-29-0-0-0","37-39-37-43","38-37-38-43","42-40-42-47-0-0","45-42-44-45-50-0","54-53-54-56-56-0","53-55-55-56-58-0","56-56-55-58-60-0","58-56-56-60-62-0","61-59-61-63-61-65"]


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
	while True:
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
	global gamedata
	with open('gamedata.txt') as json_file:
		gamedata = json.load(json_file)

	print("Loaded successfully")

## Save Gamesave
def save():
	with open('gamedata.txt', 'w') as outfile:  
		json.dump(gamedata, outfile, indent=1)

	print("Saved successfully")

def starter():
	global PcLevel
	print("")
	print("Welcome to the world of Pokemon. Today you will be given a choice of your first pokemon. Here are your choices")
	print("#1 " + pokemon[0] + " Type: " + type_1[0] +" " + type_2[0])
	print("#2 " + pokemon[3] + " Type: " + type_1[3] + " " + type_2[3])
	print("#3 " + pokemon[6] + " Type: " + type_1[6] + " " + type_2[6])
	while True:
		starter = input("which number pokemon would you like ")
		if starter == "1":
			gamedata["Pc"].append(0)
			gamedata["party"][0]=0
			gamedata["PcLevel"].append(1)
			print(pokemon[gamedata["Pc"][0]]+ " a great choice!")
			temp1=learnsets[0].split("-")
			gamedata["PcMoves"].append(temp1[0]+"-"+temp1[1])
			gamedata["xp"].append(0)
			break

		elif starter == "2":
			gamedata["Pc"].append(3)
			gamedata["party"][0]=0
			gamedata["PcLevel"].append(1)
			print(pokemon[gamedata["Pc"][0]]+ " a great choice!")
			temp1=learnsets[3].split("-")
			gamedata["PcMoves"].append(temp1[0]+"-"+temp1[1])	
			gamedata["xp"].append(0)		
			break

		elif starter == "3":
			gamedata["Pc"].append(6)
			gamedata["party"][0]=0
			gamedata["PcLevel"].append(1)
			print(pokemon[gamedata["Pc"][0]]+ " a great choice!")
			temp1=learnsets[6].split("-")
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
				for x in pokemon:
					if selected_pokemon.lower() == x.lower():
						Pokemon= pokemon[i]
						
						print()
						
						level_pokemon = int(input("What level would you like? ")) 

						print()

						global attack
						attack1 = round(attack[i]*2 + level_pokemon/100+5+10)
						global HP
						health1 = round(HP[i]*2+level_pokemon/100+level_pokemon+10)
						global speed
						speed1 = round(speed[i]*2 + level_pokemon/100+5+10)
						global defence
						defence1 = round(defence[i]*2 + level_pokemon/100+5+10)

						print()

						print(Pokemon + " Attack: " + str(attack1) + " HP: " + str(health1) + " Speed: " + str(speed1) + " Defence " + str(defence1))

						cost = 10* level_pokemon *(evolve[i]+1.5)
						buy = input(Pokemon + " Costs $" + str(cost) + ". Would you still like to buy it? ")

						while buy != "yes" and buy != 'no':
							if buy =="yes":
								if gamedata["money"]>=cost:
									gamedata["Pc"].append("-" + str(i))
								else:
									print("insufficient funds")

							elif buy != "yes" and buy != 'no':
								buy = (Pokemon + " Costs $" + str(cost) + ". Would you still like to buy it? ")

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
	temp1=LocationPokemon[gamedata["CurrentLocation"]].split("-")
	for x in temp1:
		temp2.append(pokemon[int(x)])
	print("Current Location: " + location[gamedata["CurrentLocation"]])
	print("")
	print("Here you can find:")
	for x in temp2:
		print(x)
	print("")

	game = input("Would you like to travel? ")
	if game == "yes":
		i=0
		for x in location:
			print("#" + str(i)+":" + x)
			i+=1
		game = int(input("Where would you like to travel? (int only)" ))
		if gamedata["BattleWon"] >= game:
			gamedata["CurrentLocation"] = game
			print("You travelled to " + location[gamedata["CurrentLocation"]])
			print("")
		else: 
			print("You have not yet won enough gym battles to get there yet. ")
			print("")

	else:
		print("")

def debug():
	pprint(gamedata)

def Party():
	print("")
	i=0
	for x in gamedata["party"]:
		if x != "":
			temp = gamedata["Pc"][x]
			print("#" +str(i))
			print ("Pokemon: " + pokemon[temp]) 
			print("Level: " + str(gamedata["PcLevel"][x]))
			print("Type: " + type_1[temp] + " " + type_2[temp])
			
			temp2 = gamedata["PcMoves"][x].split("-")
			for z in temp2:
				print("Move learnt: " + moveset[int(z)])

			print("")
			i+=1

def pc():
	print("")
	i=0
	print("Party:")
	Party()
	
	print("PC:")
	print("")
	
	for x in gamedata["Pc"]:
		print("#"+str(i))
		print('pokemon: ' + pokemon[x])
		print('Level: ' + str(gamedata["PcLevel"][i]))
		print("Type: " + type_1[x] + " " + type_2[x])
		temp = gamedata["PcMoves"][i].split("-")
		for z in temp:
			print("Move learnt: " + moveset[int(z)])
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
				print(pokemon[gamedata["Pc"][game2]] + " replaces " + pokemon[gamedata["Pc"][temp]])
			gamedata["party"][game] = game2


		print("")
		game = input("would you like to leave?" )
		if game =="yes":
				break
	print("")

def PokeBattle():
	print("")
	temp1 = LocationPokemon[gamedata["CurrentLocation"]].split("-")
	x = randint(0,len(temp1)-1)
	
	##establish Ai stats
	Ai_Pokemon= int(temp1[x])
	Ai_level = randint(math.ceil(0.9*gamedata["PcLevel"][gamedata["party"][0]]), round(1.1*gamedata["PcLevel"][gamedata["party"][0]]))
	Ai_attack = round(attack[Ai_Pokemon]*2 + Ai_level/100+5+10)
	Ai_health = round(HP[Ai_Pokemon]*2+Ai_level/100+Ai_level+10)
	Ai_speed = round(speed[Ai_Pokemon]*2 + Ai_level/100+5+10)
	Ai_defence = round(defence[Ai_Pokemon]*2 + Ai_level/100+5+10)
	Ai_evasion = 100
	Ai_moves = []
	Ai_status = ""
	Ai_status_length = 0

	i=0
	temp = learnsets[Ai_Pokemon+1].split("-")
	while i<4:
		temp2 =temp[randint(0,len(temp)-1)]
		if temp2 not in Ai_moves:
				Ai_moves.append(temp2)
				i+=1

	##establish player stats
	currentPokemon = 0
	Player_health = []
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
			Player_health.append(round(HP[gamedata["Pc"][x]]*2 + gamedata["PcLevel"][x]/100+gamedata["PcLevel"][x]+10))
			Player_speed.append(round(speed[gamedata["Pc"][x]]*2 + gamedata["PcLevel"][x]/100+5+10))
			Player_defence.append(round(defence[gamedata["Pc"][x]]*2 + gamedata["PcLevel"][x]/100+5+10))
			Player_attack.append(round(attack[gamedata["Pc"][x]]*2 + gamedata["PcLevel"][x]/100+5+10))


	print("A wild level " + str(Ai_level)+ " " + pokemon[Ai_Pokemon] + " appears!")
	print("Go " + pokemon[gamedata["Pc"][gamedata["party"][currentPokemon]]] + "!")

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
					print ("#" + str(i) +" " + moveset[int(x)] + " Damage: " + str(damage[int(x)]) + " Accuracy: " + str(accuracy[int(x)]) + " Type: " + typeMove[int(x)])
					i+=1
				game = input("Which attack would you like to do?" )
				if game == "quit":
					print("")
				elif game.isnumeric:
					if int(game)<=len(moves)-1:
						Player_move = int(moves[int(game)])
						print("You choose " + moveset[Player_move])
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
						print("#" +str(i) + " " + pokemon[gamedata["Pc"][x]] + " Health: " + str(Player_health[i]) + " Type: " + type_1[gamedata["Pc"][x]] + " " + type_2[gamedata["Pc"][x]])
						i+=1
			
				game = input("Which pokemon would you like to put in?" )
				if game == "quit":
					print("")
				elif game.isnumeric:
					currentPokemon = int(game)
					print("You choose " + pokemon[gamedata["Pc"][gamedata["party"][currentPokemon]]])
					switch = True
					break

				else:
					print("invalid response")

			##Catch
			elif game == "item":
				if gamedata["pokeballs"]>0:
					 gamedata["pokeballs"]-=1
					 f = round((HP[Ai_Pokemon]*2+Ai_level/100+Ai_level+10 * 255 * 4) / (Ai_health * 10))*10
					 M = randint(0,255)
					 if f>=M:
					 	print("The wild " + pokemon[Ai_Pokemon] + " was caught")
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

			##Show current pokemon
			elif game =="current":
				print(pokemon[gamedata["Pc"][gamedata["party"][currentPokemon]]])

			elif game =="stats":
				print(Ai_health)

			elif game =="die":
				Player_health[currentPokemon] = 0
				attacked = True

			elif game =="kill":
				Ai_health = 0
				attacked = True

		##Calculate effects
		if Player_status in "healing Sleep poison paralysis":
			if Player_status == "healing":
				Player_health[currentPokemon] += round(1/5*HP[gamedata["Pc"][currentPokemon]]*2 + gamedata["PcLevel"][currentPokemon]/100+gamedata["PcLevel"][currentPokemon]+10)
				print("Player is healed: " + str(round(1/5*(round(HP[gamedata["Pc"][currentPokemon]]*2 + gamedata["PcLevel"][currentPokemon]/100+gamedata["PcLevel"][currentPokemon]+10)))) + "HP")

			elif Player_status == "poison":
				Player_health[currentPokemon] -= round(1/16*HP[gamedata["Pc"][currentPokemon]]*2 + gamedata["PcLevel"][currentPokemon]/100+gamedata["PcLevel"][currentPokemon]+10)
				print("Player is poisoned: " + str(round(1/16*(round(HP[gamedata["Pc"][currentPokemon]]*2 + gamedata["PcLevel"][currentPokemon]/100+gamedata["PcLevel"][currentPokemon]+10)))) + "HP")

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
				Ai_health += round(1/5*HP[Ai_Pokemon]*2 + Ai_level/100+Ai_level+10)
				print("Ai is healed: " + str(round(1/5*HP[Ai_Pokemon]*2 + Ai_level/100+Ai_level+10) + "HP"))

			elif Ai_status == "poison":
				Ai_health -= round(1/16*HP[Ai_Pokemon]*2 + Ai_level/100+Ai_level+10)
				print("Player is poisoned: " + str(round(1/5*HP[Ai_Pokemon]*2 + Ai_level/100+Ai_level+10)) + "HP")

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
			P =accuracy[Player_move] * (Player_evasion/Ai_evasion)
			hit_chance = randint(0,100)
			if P>=hit_chance:

				## Regular Moves
				if moveset[Player_move] not in ["Hypnosis", "Lovely Kiss", "Sing", "Sleep Powder", "Spore", "Agility", "Double Team", "Teleport", "Recover", "Soft-Boiled", "Haze", "Leech Seed", "Rest", "Substitute", "Acid Armor", "Amnesia", "Barrier", "Conversion", "Defense Curl", "Disable", "Harden", "Withdraw", "Focus Energy", "Growth", "Meditate", "Sharpen", "Swords Dance", "Metronome", "Transform", "Mimic", "Mirror Move", "Poison Gas", "Poison Powder", "Toxic", "Confuse Ray", "Glare", "Stun Spore", "Supersonic", "Thunder Wave", "Splash", "String Shot", "Whirlwind", "Leer", "Screech", "Tail Whip", "Growl", "Light Screen", "Mist", "Reflect", "Roar", "Flash", "Kinesis", "Minimize", "Sand Attack", "Smokescreen"]:	
					
					##innefective move
					if (typeMove[Player_move] in "normal" and (type_1[Ai_Pokemon] in "rock" or type_2[Ai_Pokemon] in "rock")) or (typeMove[Player_move] in "fire" and (type_1[Ai_Pokemon] in "firewaterrockdragon" or type_2[Ai_Pokemon] in "firewaterrockdragon")) or (typeMove[Player_move] in "water" and (type_1[Ai_Pokemon] in "watergrassdragon" or type_2[Ai_Pokemon] in "watergrassdragon")) or (typeMove[Player_move] in "electric" and (type_1[Ai_Pokemon] in "electricgrassdragon" or type_2[Ai_Pokemon] in "electricgrassdragon")) or (typeMove[Player_move] in "grass" and (type_1[Ai_Pokemon] in "firegrasspoisonflyingbugdragon" or type_2[Ai_Pokemon] in "firegrasspoisonflyingbugdragon")) or (typeMove[Player_move] in "ice" and (type_1[Ai_Pokemon] in "fireice" or type_2[Ai_Pokemon] in "fireice")) or (typeMove[Player_move] in "fighting" and (type_1[Ai_Pokemon] in "poisonflyingpsychicbug" or type_2[Ai_Pokemon] in "poisonflyingpsychicbug")) or (typeMove[Player_move] in "poison" and (type_1[Ai_Pokemon] in "poisongroundrockghost" or type_2[Ai_Pokemon] in "poisongroundrockghost")) or (typeMove[Player_move] in "ground" and (type_1[Ai_Pokemon] in "grassbug" or type_2[Ai_Pokemon] in "grassbug")) or (typeMove[Player_move] in "flying" and (type_1[Ai_Pokemon] in "electricrock" or type_2[Ai_Pokemon] in "electricrock")) or (typeMove[Player_move] in "psychic" and (type_1[Ai_Pokemon] in "psychic" or type_2[Ai_Pokemon] in "psychic")) or (typeMove[Player_move] in "bug" and (type_1[Ai_Pokemon] in "firefightingflyingghost" or type_2[Ai_Pokemon] in "firefightingflyingghost")) or (typeMove[Player_move] in "rock" and (type_1[Ai_Pokemon] in "fightingground" or type_2[Ai_Pokemon] in "fightingground")):
						modifier=0.5

					##Effective move
					elif (typeMove[Player_move] in "fire" and (type_1[Ai_Pokemon] in "grassicebug" or type_2[Ai_Pokemon] in "grassicebug")) or (typeMove[Player_move] in "water" and (type_1[Ai_Pokemon] in "firegroundrock" or type_2[Ai_Pokemon] in "firegroundrock")) or (typeMove[Player_move] in "electric" and (type_1[Ai_Pokemon] in "waterflying" or type_2[Ai_Pokemon] in "waterflying")) or (typeMove[Player_move] in "grass" and (type_1[Ai_Pokemon] in "watergroundrock" or type_2[Ai_Pokemon] in "watergroundrock")) or (typeMove[Player_move] in "ice" and (type_1[Ai_Pokemon] in "grassgroundflyingdragon" or type_2[Ai_Pokemon] in "grassgroundflyingdragon")) or (typeMove[Player_move] in "fighting" and (type_1[Ai_Pokemon] in "normalicerock" or type_2[Ai_Pokemon] in "normalicerock")) or (typeMove[Player_move] in "poison" and (type_1[Ai_Pokemon] in "grassbug" or type_2[Ai_Pokemon] in "grassbug")) or (typeMove[Player_move] in "ground" and (type_1[Ai_Pokemon] in "fireelectricpoisonrock" or type_2[Ai_Pokemon] in "fireelectricpoisonrock")) or (typeMove[Player_move] in "flying" and (type_1[Ai_Pokemon] in "grassfightingbug" or type_2[Ai_Pokemon] in "grassfightingbug")) or (typeMove[Player_move] in "psychic" and (type_1[Ai_Pokemon] in "fightingpoison" or type_2[Ai_Pokemon] in "fightingpoison")) or (typeMove[Player_move] in "bug" and (type_1[Ai_Pokemon] in "grasspoisonpsychic" or type_2[Ai_Pokemon] in "grasspoisonpsychic")) or (typeMove[Player_move] in "rock" and (type_1[Ai_Pokemon] in "fireiceflyingbug" or type_2[Ai_Pokemon] in "fireiceflyingbug")) or (typeMove[Player_move] in "ghost" and (type_1[Ai_Pokemon] in "ghost" or type_2[Ai_Pokemon] in "ghost")) or (typeMove[Player_move] in "dragon" and (type_1[Ai_Pokemon] in "dragon" or type_2[Ai_Pokemon] in "dragon")):
						modifier = 2

					## No Effect move
					elif (typeMove[Player_move] in "normal" and (type_1[Ai_Pokemon] in "ghost" or type_2[Ai_Pokemon] in "ghost")) or (typeMove[Player_move] in "electric" and (type_1[Ai_Pokemon] in "ground" or type_2[Ai_Pokemon] in "ground")) or (typeMove[Player_move] in "fighting" and (type_1[Ai_Pokemon] in "ghost" or type_2[Ai_Pokemon] in "ghost")) or (typeMove[Player_move] in "ground" and (type_1[Ai_Pokemon] in "flying" or type_2[Ai_Pokemon] in "flying")) or (typeMove[Player_move] in "ghost" and (type_1[Ai_Pokemon] in "normalpsychic" or type_2[Ai_Pokemon] in "normalpsychic")):
						modifier = 0

					##Normal effect move
					else:
						modifier = 1

					damage_dealt = math.ceil(((2*gamedata["PcLevel"][gamedata["party"][currentPokemon]]/5+2) * damage[Player_move] * (Player_attack[currentPokemon]/Ai_defence)/50+2) *modifier)


					##Status effects
		
				else:
					if moveset[Player_move] in "Hypnosis Lovely Kiss Sing Sleep Powder Spore":
						##sleep
						Ai_status = "Sleep"
						Ai_status_length = 0
						print(pokemon[Ai_Pokemon] + " is now asleep")
						print()
					

					elif moveset[Player_move] in "Agility Double Team Teleport":
						##self-speed
						Player_speed[currentPokemon] = round(float(Player_speed[currentPokemon])* 1.05)
						print(pokemon[gamedata["Pc"][gamedata["party"][currentPokemon]]] + "'s speed rose")
						print()
					
					
					elif moveset[Player_move] in "Recover Soft-Boiled":
						##Self-heal half
						if Player_health[currentPokemon] <= 1/2*(round(HP[gamedata["Pc"][currentPokemon]]*2 + gamedata["PcLevel"][currentPokemon]/100+gamedata["PcLevel"][currentPokemon]+10)):
							Player_health[currentPokemon] += 1/2*(round(HP[gamedata["Pc"][currentPokemon]]*2 + gamedata["PcLevel"][currentPokemon]/100+gamedata["PcLevel"][currentPokemon]+10))
						else: 
							Player_health[currentPokemon] = round(HP[gamedata["Pc"][currentPokemon]]*2 + gamedata["PcLevel"][currentPokemon]/100+gamedata["PcLevel"][currentPokemon]+10)
						
						print(pokemon[gamedata["Pc"][gamedata["party"][currentPokemon]]] + "'s healed")
						print()

					
					elif moveset[Player_move] in "Haze Leech Seed Rest Substitute":
						##self-heal
						player_status="healing"
						player_status_length = 0
						
						print(pokemon[gamedata["Pc"][gamedata["party"][currentPokemon]]] + " is healing itself")
						print()

					
					elif moveset[Player_move] in "Acid Armor Amnesia Barrier Conversion Defense Curl Disable Harden Withdraw":
						##self-defense
						Player_defence[currentPokemon] = round(float(Player_defence[currentPokemon])* 1.05)
						
						print(pokemon[gamedata["Pc"][gamedata["party"][currentPokemon]]] + "'s defense rose")
						print()

					
					elif moveset[Player_move] in "Focus Energy Growth Meditate Sharpen Swords Dance":
						##self-attack
						Player_attack[currentPokemon] = round(float(Player_attack[currentPokemon])* 1.05)
						
						print(pokemon[gamedata["Pc"][gamedata["party"][currentPokemon]]] + "'s attack rose")
						print()

					
					elif moveset[Player_move] in "Metronome Transform Mimic Mirror Move":
						##random move
						Player_move = randint[0,len(moveset)-1]
						if moveset[Player_move] not in "Acid Armor Agility Amnesia Barrier Confuse Ray Conversion Defense Curl Disable Double Team Flash Focus Energy Glare Growl Growth Harden Haze Hypnosis Kinesis Leech Seed Leer Light Screen Lovely Kiss Meditate Metronome Mimic Minimize Mirror Move Mist Poison Gas Poison Powder Recover Reflect Rest Roar Sand Attack Screech Sharpen Sing Sleep Powder Smokescreen Soft-Boiled Splash Spore String Shot Stun Spore Substitute Supersonic Swords Dance Tail Whip Teleport Thunder Wave Toxic Transform Whirlwind Withdraw":	
							print(pokemon[gamedata["Pc"][gamedata["party"][currentPokemon]]] + " uses " + moveset[Player_move])
							##innefective move
							if (typeMove[Player_move] == "normal" and (type_1[Ai_Pokemon] == "rock" or type_2[Ai_Pokemon] == "rock")) or (typeMove[Player_move] == "fire" and (type_1[Ai_Pokemon] in "firewaterrockdragon" or type_2[Ai_Pokemon] in "firewaterrockdragon")) or (typeMove[Player_move] == "water" and (type_1[Ai_Pokemon] in "watergrassdragon" or type_2[Ai_Pokemon] in "watergrassdragon")) or (typeMove[Player_move] == "electric" and (type_1[Ai_Pokemon] in "electricgrassdragon" or type_2[Ai_Pokemon] in "electricgrassdragon")) or (typeMove[Player_move] == "grass" and (type_1[Ai_Pokemon] in "firegrasspoisonflyingbugdragon" or type_2[Ai_Pokemon] in "firegrasspoisonflyingbugdragon")) or (typeMove[Player_move] == "ice" and (type_1[Ai_Pokemon] in "fireice" or type_2[Ai_Pokemon] in "fireice")) or (typeMove[Player_move] == "fighting" and (type_1[Ai_Pokemon] in "poisonflyingpsychicbug" or type_2[Ai_Pokemon] in "poisonflyingpsychicbug")) or (typeMove[Player_move] == "poison" and (type_1[Ai_Pokemon] in "poisongroundrockghost" or type_2[Ai_Pokemon] in "poisongroundrockghost")) or (typeMove[Player_move] == "ground" and (type_1[Ai_Pokemon] in "grassbug" or type_2[Ai_Pokemon] in "grassbug")) or (typeMove[Player_move] == "flying" and (type_1[Ai_Pokemon] in "electricrock" or type_2[Ai_Pokemon] in "electricrock")) or (typeMove[Player_move] == "psychic" and (type_1[Ai_Pokemon] in "psychic" or type_2[Ai_Pokemon] in "psychic")) or (typeMove[Player_move] == "bug" and (type_1[Ai_Pokemon] in "firefightingflyingghost" or type_2[Ai_Pokemon] in "firefightingflyingghost")) or (typeMove[Player_move] == "rock" and (type_1[Ai_Pokemon] in "fightingground" or type_2[Ai_Pokemon] in "fightingground")):
								print("not very effective")
								modifier=0.5

							elif (typeMove[Player_move] == "fire" and (type_1[Ai_Pokemon] == "grassicebug" or type_2[Ai_Pokemon] == "grassicebug")) or (typeMove[Player_move] == "water" and (type_1[Ai_Pokemon] == "firegroundrock" or type_2[Ai_Pokemon] == "firegroundrock")) or (typeMove[Player_move] == "electric" and (type_1[Ai_Pokemon] == "waterflying" or type_2[Ai_Pokemon] == "waterflying")) or (typeMove[Player_move] == "grass" and (type_1[Ai_Pokemon] == "watergroundrock" or type_2[Ai_Pokemon] == "watergroundrock")) or (typeMove[Player_move] == "ice" and (type_1[Ai_Pokemon] == "grassgroundflyingdragon" or type_2[Ai_Pokemon] == "grassgroundflyingdragon")) or (typeMove[Player_move] == "fighting" and (type_1[Ai_Pokemon] == "normalicerock" or type_2[Ai_Pokemon] == "normalicerock")) or (typeMove[Player_move] == "poison" and (type_1[Ai_Pokemon] == "grassbug" or type_2[Ai_Pokemon] == "grassbug")) or (typeMove[Player_move] == "ground" and (type_1[Ai_Pokemon] == "fireelectricpoisonrock" or type_2[Ai_Pokemon] == "fireelectricpoisonrock")) or (typeMove[Player_move] == "flying" and (type_1[Ai_Pokemon] == "grassfightingbug" or type_2[Ai_Pokemon] == "grassfightingbug")) or (typeMove[Player_move] == "psychic" and (type_1[Ai_Pokemon] == "fightingpoison" or type_2[Ai_Pokemon] == "fightingpoison")) or (typeMove[Player_move] == "bug" and (type_1[Ai_Pokemon] == "grasspoisonpsychic" or type_2[Ai_Pokemon] == "grasspoisonpsychic")) or (typeMove[Player_move] == "rock" and (type_1[Ai_Pokemon] == "fireiceflyingbug" or type_2[Ai_Pokemon] == "fireiceflyingbug")) or (typeMove[Player_move] == "ghost" and (type_1[Ai_Pokemon] == "ghost" or type_2[Ai_Pokemon] == "ghost")) or (typeMove[Player_move] == "dragon" and (type_1[Ai_Pokemon] == "dragon" or type_2[Ai_Pokemon] == "dragon")):
								print("Very effective")
								modifier = 2

							elif (typeMove[Player_move] == "normal" and (type_1[Ai_Pokemon] == "ghost" or type_2[Ai_Pokemon] == "ghost")) or (typeMove[Player_move] == "electric" and (type_1[Ai_Pokemon] == "ground" or type_2[Ai_Pokemon] == "ground")) or (typeMove[Player_move] == "fighting" and (type_1[Ai_Pokemon] == "ghost" or type_2[Ai_Pokemon] == "ghost")) or (typeMove[Player_move] == "ground" and (type_1[Ai_Pokemon] == "flying" or type_2[Ai_Pokemon] == "flying")) or (typeMove[Player_move] == "ghost" and (type_1[Ai_Pokemon] == "normalpsychic" or type_2[Ai_Pokemon] == "normalpsychic")):
								print("No effect")
								modifier = 0

							else:
								print("yes")
								modifier = 1
							
							damage_dealt = round(((2*gamedata["PcLevel"][gamedata["party"][currentPokemon]]/5+2) * damage[Player_move] * (Player_attack[currentPokemon]/Ai_defence)/50+2) *modifier)
							Ai_health-=damage_dealt
							print("Damage dealt: " + str(damage_dealt) + " " + pokemon[Ai_Pokemon] + " has " + str(Ai_health) + " left")

						else:
							print("No effect")

					
					elif moveset[Player_move] in "Poison Gas Poison Powder Toxic":
						##poison
						Ai_status = "poison"
						Ai_status_length = 0
						
						print(pokemon[Ai_Pokemon] + " is now poisoned")
						print()
					

					elif moveset[Player_move] in "Confuse Ray Glare Stun Spore Supersonic Thunder Wave":
						##paralysis
						Ai_status = "paralysis"
						Ai_status_length = 0
						print(pokemon[Ai_Pokemon] + " is now paralysed")
						print()


					elif moveset[Player_move] in "Splash":
						##none
						print("Has no effect whatsoever.")
						print()
					

					elif moveset[Player_move] in "String Shot Whirlwind":
						##enemy-speed
						Ai_speed= round(float(Ai_speed)* 0.95)
						print(pokemon[Ai_Pokemon] + " is now slower")
						print()

					
					elif moveset[Player_move] in "Leer Screech Tail Whip":
						##enemy-defence
						Ai_defence= round(float(Ai_defence)* 0.95)
						print(pokemon[Ai_Pokemon] + "'s defence fell")
						print()

					
					elif moveset[Player_move] in "Growl Light Screen Mist Reflect Roar":
						##enemy-attack
						Ai_attack= round(float(Ai_attack)* 0.95)
						print(pokemon[Ai_Pokemon] + "'s attack fell")
						print()
				
					elif moveset[Player_move] in "Flash Kinesis Minimize Sand Attack Smokescreen":
						##enemy-accuracy
						Ai_evasion= round(float(Ai_evasion)* 0.95)
						print(pokemon[Ai_Pokemon] + "'s accuracy fell")
						print()

			else:
				print(pokemon[gamedata["Pc"][gamedata["party"][currentPokemon]]] + " misses.")
				print()

		
		## Ai Move calculation
		if Ai_paralysed == False:
			P =accuracy[Ai_turn] * (Ai_evasion/Player_evasion)
			hit_chance = randint(0,100)

			if P>=hit_chance or moveset[Ai_turn] in ["Hypnosis", "Lovely Kiss", "Sing", "Sleep Powder", "Spore", "Agility", "Double Team", "Teleport", "Recover", "Soft-Boiled", "Haze", "Leech Seed", "Rest", "Substitute", "Acid Armor", "Amnesia", "Barrier", "Conversion", "Defense Curl", "Disable", "Harden", "Withdraw", "Focus Energy", "Growth", "Meditate", "Sharpen", "Swords Dance", "Metronome", "Transform", "Mimic", "Mirror Move", "Poison Gas", "Poison Powder", "Toxic", "Confuse Ray", "Glare", "Stun Spore", "Supersonic", "Thunder Wave", "Splash", "String Shot", "Whirlwind", "Leer", "Screech", "Tail Whip", "Growl", "Light Screen", "Mist", "Reflect", "Roar", "Flash", "Kinesis", "Minimize", "Sand Attack", "Smokescreen"]:

				## Regular Moves
				if moveset[Ai_turn] not in ["Hypnosis", "Lovely Kiss", "Sing", "Sleep Powder", "Spore", "Agility", "Double Team", "Teleport", "Recover", "Soft-Boiled", "Haze", "Leech Seed", "Rest", "Substitute", "Acid Armor", "Amnesia", "Barrier", "Conversion", "Defense Curl", "Disable", "Harden", "Withdraw", "Focus Energy", "Growth", "Meditate", "Sharpen", "Swords Dance", "Metronome", "Transform", "Mimic", "Mirror Move", "Poison Gas", "Poison Powder", "Toxic", "Confuse Ray", "Glare", "Stun Spore", "Supersonic", "Thunder Wave", "Splash", "String Shot", "Whirlwind", "Leer", "Screech", "Tail Whip", "Growl", "Light Screen", "Mist", "Reflect", "Roar", "Flash", "Kinesis", "Minimize", "Sand Attack", "Smokescreen"]:	
					
					##innefective move
					if (typeMove[Ai_turn] in "normal" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "rock" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "rock")) or (typeMove[Ai_turn] in "fire" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "firewaterrockdragon" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "firewaterrockdragon")) or (typeMove[Ai_turn] in "water" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "watergrassdragon" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "watergrassdragon")) or (typeMove[Ai_turn] in "electric" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "electricgrassdragon" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "electricgrassdragon")) or (typeMove[Ai_turn] in "grass" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "firegrasspoisonflyingbugdragon" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "firegrasspoisonflyingbugdragon")) or (typeMove[Ai_turn] in "ice" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "fireice" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "fireice")) or (typeMove[Ai_turn] in "fighting" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "poisonflyingpsychicbug" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "poisonflyingpsychicbug")) or (typeMove[Ai_turn] in "poison" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "poisongroundrockghost" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "poisongroundrockghost")) or (typeMove[Ai_turn] in "ground" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "grassbug" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "grassbug")) or (typeMove[Ai_turn] in "flying" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "electricrock" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "electricrock")) or (typeMove[Ai_turn] in "psychic" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "psychic" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "psychic")) or (typeMove[Ai_turn] in "bug" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "firefightingflyingghost" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "firefightingflyingghost")) or (typeMove[Ai_turn] in "rock" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "fightingground" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "fightingground")):						
						A_modifier=0.5

					##Effective move
					elif (typeMove[Ai_turn] in "fire" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "grassicebug" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "grassicebug")) or (typeMove[Ai_turn] in "water" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "firegroundrock" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "firegroundrock")) or (typeMove[Ai_turn] in "electric" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "waterflying" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "waterflying")) or (typeMove[Ai_turn] in "grass" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "watergroundrock" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "watergroundrock")) or (typeMove[Ai_turn] in "ice" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "grassgroundflyingdragon" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "grassgroundflyingdragon")) or (typeMove[Ai_turn] in "fighting" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "normalicerock" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "normalicerock")) or (typeMove[Ai_turn] in "poison" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "grassbug" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "grassbug")) or (typeMove[Ai_turn] in "ground" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "fireelectricpoisonrock" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "fireelectricpoisonrock")) or (typeMove[Ai_turn] in "flying" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "grassfightingbug" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "grassfightingbug")) or (typeMove[Ai_turn] in "psychic" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "fightingpoison" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "fightingpoison")) or (typeMove[Ai_turn] in "bug" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "grasspoisonpsychic" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "grasspoisonpsychic")) or (typeMove[Ai_turn] in "rock" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "fireiceflyingbug" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "fireiceflyingbug")) or (typeMove[Ai_turn] in "ghost" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "ghost" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "ghost")) or (typeMove[Ai_turn] in "dragon" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "dragon" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "dragon")):						
						A_modifier = 2

					## No Effect move
					elif (typeMove[Ai_turn] in "normal" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "ghost" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "ghost")) or (typeMove[Ai_turn] in "electric" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "ground" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "ground")) or (typeMove[Ai_turn] in "fighting" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "ghost" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "ghost")) or (typeMove[Ai_turn] in "ground" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "flying" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "flying")) or (typeMove[Ai_turn] in "ghost" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "normalpsychic" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "normalpsychic")):
						A_modifier = 0

					##Normal effect move
					else:
						A_modifier = 1

					Ai_damage_dealt = math.ceil(((2*Ai_level/5+2) * damage[Ai_turn] * (Ai_attack/Player_defence[currentPokemon])/50+2) *A_modifier)


					##Status effects
		
				## Special Moves
				else:
					if moveset[Ai_turn] in "Hypnosis Lovely Kiss Sing Sleep Powder Spore":
						##sleep
						Player_status = "Sleep"
						Player_status_length = 0
						print("you are now asleep")

					elif moveset[Ai_turn] in "Agility Double Team Teleport":
						##self-speed
						Ai_speed = round(float(Ai_speed)* 1.05)
					elif moveset[Ai_turn] in "Recover Soft-Boiled":
						##Self-heal half
						if Ai_health <= round(1/2*(HP[Ai_Pokemon]*2 + Ai_level/100+Ai_level+10)):
							Ai_health= Ai_health + round(1/2*(HP[Ai_Pokemon]*2 + Ai_level/100+Ai_level+10))
						else: 
							Ai_health = (round(HP[Ai_Pokemon]*2 + Ai_level/100+Ai_level+10))

						print("Ai Heals itself")

					elif moveset[Ai_turn] in "Haze Leech Seed Rest Substitute":
						##self-heal
						Ai_status="healing"
						Ai_status_length = 0
						print("The Ai is healing itself")

					elif moveset[Ai_turn] in "Acid Armor Amnesia Barrier Conversion Defense Curl Disable Harden Withdraw":
						##self-defense
						Ai_defence  = round(float(Ai_defence)* 1.05)
						print("The Ai's defence rose")

					elif moveset[Ai_turn] in "Focus Energy Growth Meditate Sharpen Swords Dance":
						##self-attack
						Ai_attack  = round(float(Ai_attack)* 1.05)
						print("The Ai's attack rose")

					elif moveset[Ai_turn] in "Metronome Transform Mimic Mirror Move":
						##random move
						Ai_turn = randint(0,len(moveset)-1)
						if moveset[Ai_turn] not in "Acid Armor Agility Amnesia Barrier Confuse Ray Conversion Defense Curl Disable Double Team Flash Focus Energy Glare Growl Growth Harden Haze Hypnosis Kinesis Leech Seed Leer Light Screen Lovely Kiss Meditate Metronome Mimic Minimize Mirror Move Mist Poison Gas Poison Powder Recover Reflect Rest Roar Sand Attack Screech Sharpen Sing Sleep Powder Smokescreen Soft-Boiled Splash Spore String Shot Stun Spore Substitute Supersonic Swords Dance Tail Whip Teleport Thunder Wave Toxic Transform Whirlwind Withdraw":	
							
							
							##innefective move
							if (typeMove[Ai_turn] in "normal" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "rock" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "rock")) or (typeMove[Ai_turn] in "fire" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "firewaterrockdragon" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "firewaterrockdragon")) or (typeMove[Ai_turn] in "water" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "watergrassdragon" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "watergrassdragon")) or (typeMove[Ai_turn] in "electric" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "electricgrassdragon" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "electricgrassdragon")) or (typeMove[Ai_turn] in "grass" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "firegrasspoisonflyingbugdragon" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "firegrasspoisonflyingbugdragon")) or (typeMove[Ai_turn] in "ice" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "fireice" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "fireice")) or (typeMove[Ai_turn] in "fighting" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "poisonflyingpsychicbug" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "poisonflyingpsychicbug")) or (typeMove[Ai_turn] in "poison" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "poisongroundrockghost" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "poisongroundrockghost")) or (typeMove[Ai_turn] in "ground" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "grassbug" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "grassbug")) or (typeMove[Ai_turn] in "flying" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "electricrock" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "electricrock")) or (typeMove[Ai_turn] in "psychic" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "psychic" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "psychic")) or (typeMove[Ai_turn] in "bug" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "firefightingflyingghost" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "firefightingflyingghost")) or (typeMove[Ai_turn] in "rock" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "fightingground" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "fightingground")):						
								A_modifier=0.5

							##Effective move
							elif (typeMove[Ai_turn] in "fire" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "grassicebug" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "grassicebug")) or (typeMove[Ai_turn] in "water" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "firegroundrock" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "firegroundrock")) or (typeMove[Ai_turn] in "electric" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "waterflying" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "waterflying")) or (typeMove[Ai_turn] in "grass" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "watergroundrock" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "watergroundrock")) or (typeMove[Ai_turn] in "ice" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "grassgroundflyingdragon" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "grassgroundflyingdragon")) or (typeMove[Ai_turn] in "fighting" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "normalicerock" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "normalicerock")) or (typeMove[Ai_turn] in "poison" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "grassbug" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "grassbug")) or (typeMove[Ai_turn] in "ground" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "fireelectricpoisonrock" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "fireelectricpoisonrock")) or (typeMove[Ai_turn] in "flying" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "grassfightingbug" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "grassfightingbug")) or (typeMove[Ai_turn] in "psychic" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "fightingpoison" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "fightingpoison")) or (typeMove[Ai_turn] in "bug" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "grasspoisonpsychic" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "grasspoisonpsychic")) or (typeMove[Ai_turn] in "rock" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "fireiceflyingbug" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "fireiceflyingbug")) or (typeMove[Ai_turn] in "ghost" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "ghost" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "ghost")) or (typeMove[Ai_turn] in "dragon" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "dragon" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "dragon")):						
								A_modifier = 2

							## No Effect move
							elif (typeMove[Ai_turn] in "normal" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "ghost" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "ghost")) or (typeMove[Ai_turn] in "electric" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "ground" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "ground")) or (typeMove[Ai_turn] in "fighting" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "ghost" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "ghost")) or (typeMove[Ai_turn] in "ground" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "flying" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "flying")) or (typeMove[Ai_turn] in "ghost" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "normalpsychic" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "normalpsychic")):
								A_modifier = 0

							##Normal effect move
							else:
								A_modifier = 1

							Ai_damage_dealt = round(((2*Ai_level/5+2) * damage[Ai_turn] * (Ai_attack/Player_defence[currentPokemon])/50+2) *A_modifier)

						else:
							A_modifier = 0 

					elif moveset[Ai_turn] in "Poison Gas Poison Powder Toxic":
						##poison
						Player_status = "poison"
						Player_status_length = 0
						print("You are now poisoned")

					elif moveset[Ai_turn] in "Confuse Ray Glare Stun Spore Supersonic Thunder Wave":
						##paralysis
						Player_status = "paralysis"
						Player_status_length = 0
						print("You are now asleep")

					elif moveset[Ai_turn] in "Splash":
						##none
						print("Has no effect whatsoever.")

					elif moveset[Ai_turn] in "String Shot Whirlwind":
						##enemy-speed
						Player_speed[currentPokemon] = round(float(Player_speed[currentPokemon])*0.95)
						print("Your speed fell")

					elif moveset[Ai_turn] in "Leer Screech Tail Whip":
						##enemy-defence
						Player_defence[currentPokemon]= round(float(Player_defence[currentPokemon])*0.95)
						print("Your defence fell")

					elif moveset[Ai_turn] in "Growl Light Screen Mist Reflect Roar":
						##enemy-attack
						Player_attack[currentPokemon]= round(float(Player_attack[currentPokemon])*0.95)
						print("Your attack fell")

					elif moveset[Player_move] in "Flash Kinesis Minimize Sand Attack Smokescreen":
						##enemy-accuracy
						print("Your accuracy fell")
						Player_evasion[currentPokemon]= round(float(Player_evasion[currentPokemon])*0.95)

			else:
				print(pokemon[Ai_Pokemon] + " misses.")
				print()

		##Move order
		
		if Player_speed[currentPokemon]>Ai_speed and Player_move!=-1:
			print(pokemon[gamedata["Pc"][gamedata["party"][currentPokemon]]] + " uses " + moveset[Player_move])
			Ai_health-=damage_dealt
		
			if modifier == 0.5:
				print("Not very effective")
			elif modifier == 2:
				print("Very Effective")
			elif modifier == 0:
				print("No effect")

			print("Damage dealt: " + str(damage_dealt) + " " + pokemon[Ai_Pokemon] + " has " + str(Ai_health) + " left")
			print()

			if Ai_health>0:
				print(pokemon[Ai_Pokemon] + " uses " + moveset[Ai_turn])
				Player_health[currentPokemon]-=Ai_damage_dealt
				
				if A_modifier == 0.5:
					print("Not very effective")
				elif A_modifier == 2:
					print("Very Effective")
				elif A_modifier == 0:
					print("No effect")

				print("Damage dealt: " + str(Ai_damage_dealt) + " " + pokemon[gamedata["Pc"][gamedata["party"][currentPokemon]]] + " has " + str(Player_health[currentPokemon]) + " left")
				
				
				if Player_health[currentPokemon] <= 0:	
					##Choose next pokemon
					print(pokemon[gamedata["Pc"][gamedata["party"][currentPokemon]]] + " Fainted")
					i=0
					for x in Player_health:
						if x>0:
							currentPokemon=i
							print("Go " + pokemon[gamedata["Pc"][gamedata["party"][currentPokemon]]] + "!")
							break
						i+=1
					if Player_health[currentPokemon] <= 0:
						print("You black out")
						break

			else:
				### Calculate XP
				print("XP")
				xp_recieved = round((152*Ai_level/5)*(((2*Ai_level+10)**2.5)/(Ai_level + gamedata["PcLevel"][gamedata["party"][currentPokemon]] + 10)**2.5+1))

				print("xp Earned: " + str(xp_recieved))
				gamedata["xp"][gamedata["party"][currentPokemon]]+=xp_recieved

				##Required xp to level up
				xp_table = [8,19,37,61,91,127,169,217,271,331,397,469,547,631,721,817,919,1027,1141,1261,1387,1519,1657,1801,1951,2107,2269,2437,2611,2791,2977,3169,3367,3571,3781,3997,4219,4447,4681,4921,5167,5419,5677,5941,6211,6487,6769,7057,7351,7651,7957,8269,8587,8911,9241,9577,9919,10267,10621,10981,11347,11719,12097,12481,12871,13267,13669,14077,14491,14911,15337,15769,16207,16651,17101,17557,18019,18487,18961,19441,19927,20419,20917,21421,21931,22447,22969,23497,24031,24571,25117,25669,26227,26791,27361,27937,28519,29107,29701,9999999999999999999999]
				
				##Level up
				if gamedata["xp"][gamedata["party"][currentPokemon]] >= xp_table[gamedata["PcLevel"][gamedata["party"][currentPokemon]]-1]:
					
					gamedata["xp"][gamedata["party"][currentPokemon]] -= xp_table[gamedata["PcLevel"][gamedata["party"][currentPokemon]]-1]
					gamedata["PcLevel"][gamedata["party"][currentPokemon]]+=1
					
					print(pokemon[gamedata["Pc"][gamedata["party"][currentPokemon]]] + " Levelled Up! They are now level " + str(gamedata["PcLevel"][gamedata["party"][currentPokemon]]))
					
					##New move
					if gamedata["PcLevel"][gamedata["party"][currentPokemon]]%2 ==0:
						temp = learnsets[gamedata["Pc"][gamedata["party"][currentPokemon]]].split("-")

						while True:
							new_move = randint(0,len(temp)-1)
							
							if temp[new_move] not in gamedata["PcMoves"][gamedata["party"][currentPokemon]]:
								
								print(pokemon[gamedata["Pc"][gamedata["party"][currentPokemon]]] + " would like to learn the move:")
								print(moveset[int(temp[new_move])] + " Damage: " + str(damage[int(temp[new_move])]) + " Accuracy: " + str(accuracy[int(temp[new_move])]) + " Type: " + typeMove[int(temp[new_move])])

								game = 0
								##Learn move
								while game != "yes" and game != "no":
									game = input("would you like to learn it? ")
									if game == 'no':
										print(pokemon[gamedata["Pc"][gamedata["party"][currentPokemon]]] + " does not learn the move")

									elif game == "yes":
										i=0

										gamedata["PcMoves"][gamedata["party"][currentPokemon]].split("-")
										for x in gamedata["PcMoves"][gamedata["party"][currentPokemon]].split("-"):
											print("#"+str(i)+ " " + moveset[int(x)] + " Damage: " + str(damage[int(x)]) + " Accuracy: " + str(accuracy[int(x)]) + " Type: " + typeMove[int(x)])
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
					if (gamedata["PcLevel"][gamedata["party"][currentPokemon]] > 25 and evolve[gamedata["Pc"][gamedata["party"][currentPokemon]]] <=0 and evolve[gamedata["Pc"][gamedata["party"][currentPokemon]]] < evolve[gamedata["Pc"][gamedata["party"][currentPokemon]]+1]) or (gamedata["PcLevel"][gamedata["party"][currentPokemon]] > 50 and evolve[gamedata["Pc"][gamedata["party"][currentPokemon]]] <=2 and evolve[gamedata["Pc"][gamedata["party"][currentPokemon]]] < evolve[gamedata["Pc"][gamedata["party"][currentPokemon]]+1]):

						gamedata["Pc"][gamedata["party"][currentPokemon]]+=1
						print( pokemon[gamedata["Pc"][gamedata["party"][currentPokemon]]-1] + " Evolves! They are now " + pokemon[gamedata["Pc"][gamedata["party"][currentPokemon]]])
				
				gamedata["money"] += 100
				print("You earned $100! You now have $" + str(gamedata["money"]))
				save()
				break
		

		##Ai Moves first
		else:
			print(pokemon[Ai_Pokemon] + " uses " + moveset[Ai_turn])
			Player_health[currentPokemon]-=Ai_damage_dealt
				
			if A_modifier == 0.5:
				print("Not very effective")
			elif A_modifier == 2:
				print("Very Effective")
			elif A_modifier == 0:
				print("No effect")

			print("Damage dealt: " + str(Ai_damage_dealt) + " " + pokemon[gamedata["Pc"][gamedata["party"][currentPokemon]]] + " has " + str(Player_health[currentPokemon]) + " left")
			print()

			if Player_health[currentPokemon]>0 and Player_move!=-1:
				print(pokemon[gamedata["Pc"][gamedata["party"][currentPokemon]]] + " uses " + moveset[Player_move])
				Ai_health-=damage_dealt
				
				if modifier == 0.5:
					print("Not very effective")
				elif modifier == 2:
					print("Very Effective")
				elif modifier == 0:
					print("No effect")

				print("Damage dealt: " + str(damage_dealt) + " " + pokemon[Ai_Pokemon] + " has " + str(Ai_health) + " left")

				if Ai_health<=0:
					### Calculate XP
					print("XP")
					xp_recieved = round((152*Ai_level/5)*(((2*Ai_level+10)**2.5)/(Ai_level + gamedata["PcLevel"][gamedata["party"][currentPokemon]] + 10)**2.5+1))

					print("xp Earned: " + str(xp_recieved))
					gamedata["xp"][gamedata["party"][currentPokemon]]+=xp_recieved

					##Required xp to level up
					xp_table = [8,19,37,61,91,127,169,217,271,331,397,469,547,631,721,817,919,1027,1141,1261,1387,1519,1657,1801,1951,2107,2269,2437,2611,2791,2977,3169,3367,3571,3781,3997,4219,4447,4681,4921,5167,5419,5677,5941,6211,6487,6769,7057,7351,7651,7957,8269,8587,8911,9241,9577,9919,10267,10621,10981,11347,11719,12097,12481,12871,13267,13669,14077,14491,14911,15337,15769,16207,16651,17101,17557,18019,18487,18961,19441,19927,20419,20917,21421,21931,22447,22969,23497,24031,24571,25117,25669,26227,26791,27361,27937,28519,29107,29701,9999999999999999999999]
					
					##Level up
					if gamedata["xp"][gamedata["party"][currentPokemon]] >= xp_table[gamedata["PcLevel"][gamedata["party"][currentPokemon]]-1]:
						
						gamedata["xp"][gamedata["party"][currentPokemon]] -= xp_table[gamedata["PcLevel"][gamedata["party"][currentPokemon]]-1]
						gamedata["PcLevel"][gamedata["party"][currentPokemon]]+=1
						
						print(pokemon[gamedata["Pc"][gamedata["party"][currentPokemon]]] + " Levelled Up! They are now level " + str(gamedata["PcLevel"][gamedata["party"][currentPokemon]]))
						
						##New move
						if gamedata["PcLevel"][gamedata["party"][currentPokemon]]%2 ==0:
							temp = learnsets[gamedata["Pc"][gamedata["party"][currentPokemon]]].split("-")

							while True:
								new_move = randint(0,len(temp)-1)
								
								if temp[new_move] not in gamedata["PcMoves"][gamedata["party"][currentPokemon]]:
									
									print(pokemon[gamedata["Pc"][gamedata["party"][currentPokemon]]] + " would like to learn the move:")
									print(moveset[int(temp[new_move])] + " Damage: " + str(damage[int(temp[new_move])]) + " Accuracy: " + str(accuracy[int(temp[new_move])]) + " Type: " + typeMove[int(temp[new_move])])

									game = 0
									##Learn move
									while game != "yes" and game != "no":
										game = input("would you like to learn it? ")
										if game == 'no':
											print(pokemon[gamedata["Pc"][gamedata["party"][currentPokemon]]] + " does not learn the move")

										elif game == "yes":
											i=0

											gamedata["PcMoves"][gamedata["party"][currentPokemon]].split("-")
											for x in gamedata["PcMoves"][gamedata["party"][currentPokemon]].split("-"):
												print("#"+str(i)+ " " + moveset[int(x)] + " Damage: " + str(damage[int(x)]) + " Accuracy: " + str(accuracy[int(x)]) + " Type: " + typeMove[int(x)])
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
						if (gamedata["PcLevel"][gamedata["party"][currentPokemon]] > 25 and evolve[gamedata["Pc"][gamedata["party"][currentPokemon]]] <=0 and evolve[gamedata["Pc"][gamedata["party"][currentPokemon]]] < evolve[gamedata["Pc"][gamedata["party"][currentPokemon]]+1]) or (gamedata["PcLevel"][gamedata["party"][currentPokemon]] > 50 and evolve[gamedata["Pc"][gamedata["party"][currentPokemon]]] <=2 and evolve[gamedata["Pc"][gamedata["party"][currentPokemon]]] < evolve[gamedata["Pc"][gamedata["party"][currentPokemon]]+1]):

							gamedata["Pc"][gamedata["party"][currentPokemon]]+=1
							print( pokemon[gamedata["Pc"][gamedata["party"][currentPokemon]]-1] + " Evolves! They are now " + pokemon[gamedata["Pc"][gamedata["party"][currentPokemon]]])
					
					gamedata["money"] += 100
					print("You earned $100! You now have $" + str(gamedata["money"]))
					save()
					break

			elif Player_health[currentPokemon] <= 0:
				##Choose next pokemon
				print(pokemon[gamedata["Pc"][gamedata["party"][currentPokemon]]] + " Fainted")
				i=0
				for x in Player_health:
					if x>0:
						currentPokemon=i
						print("Go " + pokemon[gamedata["Pc"][gamedata["party"][currentPokemon]]] + "!")
						break
					i+=1
				if Player_health[currentPokemon] <= 0:
					print("You black out")
					break

	
		Player_status_length+=1
		Ai_status_length+=1

def TrainerBattle():
	print()
	Ai_Pokemon= TrainerPokemon[gamedata["BattleWon"]].split("-")
	Ai_level = TrainerLevel[gamedata["BattleWon"]].split("-")
	AiCurrentPokemon = 0

	Ai_attack = []
	Ai_health = []
	Ai_speed = []
	Ai_defence = []

	i=0
	for x in Ai_Pokemon:
		x = int(x)
		if x != 152:
			y = int(Ai_level[i])
			Ai_attack.append(round(attack[x]*2 + y/100+5+10))
			Ai_health.append(round(HP[x]*2+y/100+y+10))
			Ai_speed.append(round(speed[x]*2 + y/100+5+10))
			Ai_defence.append(round(defence[x]*2 + y/100+5+10))
		i+=1
	
	Ai_evasion = 100
	Ai_status = ""
	Ai_status_length = 0


	##establish player stats
	currentPokemon = 0
	Player_health = []
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
			Player_health.append(round(HP[gamedata["Pc"][x]]*2 + gamedata["PcLevel"][x]/100+gamedata["PcLevel"][x]+10))
			Player_speed.append(round(speed[gamedata["Pc"][x]]*2 + gamedata["PcLevel"][x]/100+5+10))
			Player_defence.append(round(defence[gamedata["Pc"][x]]*2 + gamedata["PcLevel"][x]/100+5+10))
			Player_attack.append(round(attack[gamedata["Pc"][x]]*2 + gamedata["PcLevel"][x]/100+5+10))


	print("The Trainer sends out " + pokemon[int(Ai_Pokemon[AiCurrentPokemon])])
	print("Go " + pokemon[gamedata["Pc"][gamedata["party"][currentPokemon]]] + "!")

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

		Ai_moves = []
		##Calculate Ai Moves
		if AiCurrentPokemon ==0:
			temp = TrainerMove1[gamedata["BattleWon"]].split("-")
			for x in temp:
				Ai_moves.append(int(x))

		if AiCurrentPokemon ==1:
			temp = TrainerMove2[gamedata["BattleWon"]].split("-")
			for x in temp:
				Ai_moves.append(int(x))

		if AiCurrentPokemon ==2:
			temp = TrainerMove3[gamedata["BattleWon"]].split("-")
			for x in temp:
				Ai_moves.append(int(x))

		if AiCurrentPokemon ==3:
			temp = TrainerMove4[gamedata["BattleWon"]].split("-")
			for x in temp:
				Ai_moves.append(int(x))

		if AiCurrentPokemon ==4:
			temp = TrainerMove5[gamedata["BattleWon"]].split("-")
			for x in temp:
				Ai_moves.append(int(x))

		if AiCurrentPokemon ==5:
			temp = TrainerMove6[gamedata["BattleWon"]].split("-")
			for x in temp:
				Ai_moves.append(int(x))

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
					print ("#" + str(i) +" " + moveset[int(x)] + " Damage: " + str(damage[int(x)]) + " Accuracy: " + str(accuracy[int(x)]) + " Type: " + typeMove[int(x)])
					i+=1
				game = input("Which attack would you like to do?" )
				if game == "quit":
					print("")
				elif game.isnumeric:
					if int(game)<=len(moves)-1:
						Player_move = int(moves[int(game)])
						print("You choose " + moveset[Player_move])
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
						print("#" +str(i) + " " + pokemon[gamedata["Pc"][x]] + " Health: " + str(Player_health[i]) + " Type: " + type_1[gamedata["Pc"][x]] + " " + type_2[gamedata["Pc"][x]])
						i+=1
			
				game = input("Which pokemon would you like to put in?" )
				if game == "quit":
					print("")
				elif game.isnumeric:
					currentPokemon = int(game)
					print("You choose " + pokemon[gamedata["Pc"][gamedata["party"][currentPokemon]]])
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

			##Show current pokemon
			elif game =="current":
				print(pokemon[gamedata["Pc"][gamedata["party"][currentPokemon]]])

			elif game =="stats":
				print(Ai_health)

			elif game =="die":
				Player_health[currentPokemon] = 0
				attacked = True

			elif game =="kill":
				Ai_health = 0
				attacked = True

		##Calculate effects
		if Player_status in "healing Sleep poison paralysis":
			if Player_status == "healing":
				Player_health[currentPokemon] += round(1/5*HP[gamedata["Pc"][currentPokemon]]*2 + gamedata["PcLevel"][currentPokemon]/100+gamedata["PcLevel"][currentPokemon]+10)
				print("Player is healed: " + str(round(1/5*(round(HP[gamedata["Pc"][currentPokemon]]*2 + gamedata["PcLevel"][currentPokemon]/100+gamedata["PcLevel"][currentPokemon]+10)))) + "HP")

			elif Player_status == "poison":
				Player_health[currentPokemon] -= round(1/16*HP[gamedata["Pc"][currentPokemon]]*2 + gamedata["PcLevel"][currentPokemon]/100+gamedata["PcLevel"][currentPokemon]+10)
				print("Player is poisoned: " + str(round(1/16*(round(HP[gamedata["Pc"][currentPokemon]]*2 + gamedata["PcLevel"][currentPokemon]/100+gamedata["PcLevel"][currentPokemon]+10)))) + "HP")

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
				Ai_health[AiCurrentPokemon] += round(1/5*HP[Ai_Pokemon[AiCurrentPokemon]]*2 + Ai_level[AiCurrentPokemon]/100+Ai_level[AiCurrentPokemon]+10)
				print("Ai is healed: " + str(round(1/5*HP[Ai_Pokemon[AiCurrentPokemon]]*2 + Ai_level[AiCurrentPokemon]/100+Ai_level[AiCurrentPokemon]+10) + "HP"))

			elif Ai_status == "poison":
				Ai_health -= round(1/16*HP[Ai_Pokemon[AiCurrentPokemon]]*2 + Ai_level[AiCurrentPokemon]/100+Ai_level[AiCurrentPokemon]+10)
				print("Player is poisoned: " + str(round(1/16*HP[Ai_Pokemon[AiCurrentPokemon]]*2 + Ai_level[AiCurrentPokemon]/100+Ai_level[AiCurrentPokemon]+10)) + "HP")

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
			P =accuracy[Player_move] * (Player_evasion/Ai_evasion)
			hit_chance = randint(0,100)
			if P>=hit_chance:

				## Regular Moves
				if moveset[Player_move] not in ["Hypnosis", "Lovely Kiss", "Sing", "Sleep Powder", "Spore", "Agility", "Double Team", "Teleport", "Recover", "Soft-Boiled", "Haze", "Leech Seed", "Rest", "Substitute", "Acid Armor", "Amnesia", "Barrier", "Conversion", "Defense Curl", "Disable", "Harden", "Withdraw", "Focus Energy", "Growth", "Meditate", "Sharpen", "Swords Dance", "Metronome", "Transform", "Mimic", "Mirror Move", "Poison Gas", "Poison Powder", "Toxic", "Confuse Ray", "Glare", "Stun Spore", "Supersonic", "Thunder Wave", "Splash", "String Shot", "Whirlwind", "Leer", "Screech", "Tail Whip", "Growl", "Light Screen", "Mist", "Reflect", "Roar", "Flash", "Kinesis", "Minimize", "Sand Attack", "Smokescreen"]:	
					
					##innefective move
					if (typeMove[Player_move] in "normal" and (type_1[int(Ai_Pokemon[AiCurrentPokemon])] in "rock" or type_2[int(Ai_Pokemon[AiCurrentPokemon])] in "rock")) or (typeMove[Player_move] in "fire" and (type_1[int(Ai_Pokemon[AiCurrentPokemon])] in "firewaterrockdragon" or type_2[int(Ai_Pokemon[AiCurrentPokemon])] in "firewaterrockdragon")) or (typeMove[Player_move] in "water" and (type_1[int(Ai_Pokemon[AiCurrentPokemon])] in "watergrassdragon" or type_2[int(Ai_Pokemon[AiCurrentPokemon])] in "watergrassdragon")) or (typeMove[Player_move] in "electric" and (type_1[int(Ai_Pokemon[AiCurrentPokemon])] in "electricgrassdragon" or type_2[int(Ai_Pokemon[AiCurrentPokemon])] in "electricgrassdragon")) or (typeMove[Player_move] in "grass" and (type_1[int(Ai_Pokemon[AiCurrentPokemon])] in "firegrasspoisonflyingbugdragon" or type_2[int(Ai_Pokemon[AiCurrentPokemon])] in "firegrasspoisonflyingbugdragon")) or (typeMove[Player_move] in "ice" and (type_1[int(Ai_Pokemon[AiCurrentPokemon])] in "fireice" or type_2[int(Ai_Pokemon[AiCurrentPokemon])] in "fireice")) or (typeMove[Player_move] in "fighting" and (type_1[int(Ai_Pokemon[AiCurrentPokemon])] in "poisonflyingpsychicbug" or type_2[int(Ai_Pokemon[AiCurrentPokemon])] in "poisonflyingpsychicbug")) or (typeMove[Player_move] in "poison" and (type_1[int(Ai_Pokemon[AiCurrentPokemon])] in "poisongroundrockghost" or type_2[int(Ai_Pokemon[AiCurrentPokemon])] in "poisongroundrockghost")) or (typeMove[Player_move] in "ground" and (type_1[int(Ai_Pokemon[AiCurrentPokemon])] in "grassbug" or type_2[int(Ai_Pokemon[AiCurrentPokemon])] in "grassbug")) or (typeMove[Player_move] in "flying" and (type_1[int(Ai_Pokemon[AiCurrentPokemon])] in "electricrock" or type_2[int(Ai_Pokemon[AiCurrentPokemon])] in "electricrock")) or (typeMove[Player_move] in "psychic" and (type_1[int(Ai_Pokemon[AiCurrentPokemon])] in "psychic" or type_2[int(Ai_Pokemon[AiCurrentPokemon])] in "psychic")) or (typeMove[Player_move] in "bug" and (type_1[int(Ai_Pokemon[AiCurrentPokemon])] in "firefightingflyingghost" or type_2[int(Ai_Pokemon[AiCurrentPokemon])] in "firefightingflyingghost")) or (typeMove[Player_move] in "rock" and (type_1[int(Ai_Pokemon[AiCurrentPokemon])] in "fightingground" or type_2[int(Ai_Pokemon[AiCurrentPokemon])] in "fightingground")):
						modifier=0.5

					##Effective move
					elif (typeMove[Player_move] in "fire" and (type_1[int(Ai_Pokemon[AiCurrentPokemon])] in "grassicebug" or type_2[int(Ai_Pokemon[AiCurrentPokemon])] in "grassicebug")) or (typeMove[Player_move] in "water" and (type_1[int(Ai_Pokemon[AiCurrentPokemon])] in "firegroundrock" or type_2[int(Ai_Pokemon[AiCurrentPokemon])] in "firegroundrock")) or (typeMove[Player_move] in "electric" and (type_1[int(Ai_Pokemon[AiCurrentPokemon])] in "waterflying" or type_2[int(Ai_Pokemon[AiCurrentPokemon])] in "waterflying")) or (typeMove[Player_move] in "grass" and (type_1[int(Ai_Pokemon[AiCurrentPokemon])] in "watergroundrock" or type_2[int(Ai_Pokemon[AiCurrentPokemon])] in "watergroundrock")) or (typeMove[Player_move] in "ice" and (type_1[int(Ai_Pokemon[AiCurrentPokemon])] in "grassgroundflyingdragon" or type_2[int(Ai_Pokemon[AiCurrentPokemon])] in "grassgroundflyingdragon")) or (typeMove[Player_move] in "fighting" and (type_1[int(Ai_Pokemon[AiCurrentPokemon])] in "normalicerock" or type_2[int(Ai_Pokemon[AiCurrentPokemon])] in "normalicerock")) or (typeMove[Player_move] in "poison" and (type_1[int(Ai_Pokemon[AiCurrentPokemon])] in "grassbug" or type_2[int(Ai_Pokemon[AiCurrentPokemon])] in "grassbug")) or (typeMove[Player_move] in "ground" and (type_1[int(Ai_Pokemon[AiCurrentPokemon])] in "fireelectricpoisonrock" or type_2[int(Ai_Pokemon[AiCurrentPokemon])] in "fireelectricpoisonrock")) or (typeMove[Player_move] in "flying" and (type_1[int(Ai_Pokemon[AiCurrentPokemon])] in "grassfightingbug" or type_2[int(Ai_Pokemon[AiCurrentPokemon])] in "grassfightingbug")) or (typeMove[Player_move] in "psychic" and (type_1[int(Ai_Pokemon[AiCurrentPokemon])] in "fightingpoison" or type_2[int(Ai_Pokemon[AiCurrentPokemon])] in "fightingpoison")) or (typeMove[Player_move] in "bug" and (type_1[int(Ai_Pokemon[AiCurrentPokemon])] in "grasspoisonpsychic" or type_2[int(Ai_Pokemon[AiCurrentPokemon])] in "grasspoisonpsychic")) or (typeMove[Player_move] in "rock" and (type_1[int(Ai_Pokemon[AiCurrentPokemon])] in "fireiceflyingbug" or type_2[int(Ai_Pokemon[AiCurrentPokemon])] in "fireiceflyingbug")) or (typeMove[Player_move] in "ghost" and (type_1[int(Ai_Pokemon[AiCurrentPokemon])] in "ghost" or type_2[int(Ai_Pokemon[AiCurrentPokemon])] in "ghost")) or (typeMove[Player_move] in "dragon" and (type_1[int(Ai_Pokemon[AiCurrentPokemon])] in "dragon" or type_2[int(Ai_Pokemon[AiCurrentPokemon])] in "dragon")):
						modifier = 2

					## No Effect move
					elif (typeMove[Player_move] in "normal" and (type_1[int(Ai_Pokemon[AiCurrentPokemon])] in "ghost" or type_2[int(Ai_Pokemon[AiCurrentPokemon])] in "ghost")) or (typeMove[Player_move] in "electric" and (type_1[int(Ai_Pokemon[AiCurrentPokemon])] in "ground" or type_2[int(Ai_Pokemon[AiCurrentPokemon])] in "ground")) or (typeMove[Player_move] in "fighting" and (type_1[int(Ai_Pokemon[AiCurrentPokemon])] in "ghost" or type_2[int(Ai_Pokemon[AiCurrentPokemon])] in "ghost")) or (typeMove[Player_move] in "ground" and (type_1[int(Ai_Pokemon[AiCurrentPokemon])] in "flying" or type_2[int(Ai_Pokemon[AiCurrentPokemon])] in "flying")) or (typeMove[Player_move] in "ghost" and (type_1[int(Ai_Pokemon[AiCurrentPokemon])] in "normalpsychic" or type_2[int(Ai_Pokemon[AiCurrentPokemon])] in "normalpsychic")):
						modifier = 0
					##Normal effect move
					else:
						modifier = 1

					damage_dealt = round(((2*gamedata["PcLevel"][gamedata["party"][currentPokemon]]/5+2) * damage[Player_move] * (Player_attack[currentPokemon]/Ai_defence[AiCurrentPokemon])/50+2) *modifier)


					##Status effects
		
				else:
					if moveset[Player_move] in "Hypnosis Lovely Kiss Sing Sleep Powder Spore":
						##sleep
						Ai_status = "Sleep"
						Ai_status_length = 0
						print(pokemon[Ai_Pokemon] + " is now asleep")
						print()
					

					elif moveset[Player_move] in "Agility Double Team Teleport":
						##self-speed
						Player_speed[currentPokemon] = round(float(Player_speed[currentPokemon])* 1.05)
						print(pokemon[gamedata["Pc"][gamedata["party"][currentPokemon]]] + "'s speed rose")
						print()
					
					
					elif moveset[Player_move] in "Recover Soft-Boiled":
						##Self-heal half
						if Player_health[currentPokemon] <= 1/2*(round(HP[gamedata["Pc"][currentPokemon]]*2 + gamedata["PcLevel"][currentPokemon]/100+gamedata["PcLevel"][currentPokemon]+10)):
							Player_health[currentPokemon] += 1/2*(round(HP[gamedata["Pc"][currentPokemon]]*2 + gamedata["PcLevel"][currentPokemon]/100+gamedata["PcLevel"][currentPokemon]+10))
						else: 
							Player_health[currentPokemon] = round(HP[gamedata["Pc"][currentPokemon]]*2 + gamedata["PcLevel"][currentPokemon]/100+gamedata["PcLevel"][currentPokemon]+10)
						
						print(pokemon[gamedata["Pc"][gamedata["party"][currentPokemon]]] + "'s healed")
						print()

					
					elif moveset[Player_move] in "Haze Leech Seed Rest Substitute":
						##self-heal
						player_status="healing"
						player_status_length = 0
						
						print(pokemon[gamedata["Pc"][gamedata["party"][currentPokemon]]] + " is healing itself")
						print()

					
					elif moveset[Player_move] in "Acid Armor Amnesia Barrier Conversion Defense Curl Disable Harden Withdraw":
						##self-defense
						Player_defence[currentPokemon] = round(float(Player_defence[currentPokemon])* 1.05)
						
						print(pokemon[gamedata["Pc"][gamedata["party"][currentPokemon]]] + "'s defense rose")
						print()

					
					elif moveset[Player_move] in "Focus Energy Growth Meditate Sharpen Swords Dance":
						##self-attack
						Player_attack[currentPokemon] = round(float(Player_attack[currentPokemon])* 1.05)
						
						print(pokemon[gamedata["Pc"][gamedata["party"][currentPokemon]]] + "'s attack rose")
						print()

					
					elif moveset[Player_move] in "Metronome Transform Mimic Mirror Move":
						##random move
						Player_move = randint[0,len(moveset)-1]
						if moveset[Player_move] not in "Acid Armor Agility Amnesia Barrier Confuse Ray Conversion Defense Curl Disable Double Team Flash Focus Energy Glare Growl Growth Harden Haze Hypnosis Kinesis Leech Seed Leer Light Screen Lovely Kiss Meditate Metronome Mimic Minimize Mirror Move Mist Poison Gas Poison Powder Recover Reflect Rest Roar Sand Attack Screech Sharpen Sing Sleep Powder Smokescreen Soft-Boiled Splash Spore String Shot Stun Spore Substitute Supersonic Swords Dance Tail Whip Teleport Thunder Wave Toxic Transform Whirlwind Withdraw":	
							print(pokemon[gamedata["Pc"][gamedata["party"][currentPokemon]]] + " uses " + moveset[Player_move])
							##innefective move
							if (typeMove[Player_move] == "normal" and (type_1[Ai_Pokemon] == "rock" or type_2[Ai_Pokemon] == "rock")) or (typeMove[Player_move] == "fire" and (type_1[Ai_Pokemon] in "firewaterrockdragon" or type_2[Ai_Pokemon] in "firewaterrockdragon")) or (typeMove[Player_move] == "water" and (type_1[Ai_Pokemon] in "watergrassdragon" or type_2[Ai_Pokemon] in "watergrassdragon")) or (typeMove[Player_move] == "electric" and (type_1[Ai_Pokemon] in "electricgrassdragon" or type_2[Ai_Pokemon] in "electricgrassdragon")) or (typeMove[Player_move] == "grass" and (type_1[Ai_Pokemon] in "firegrasspoisonflyingbugdragon" or type_2[Ai_Pokemon] in "firegrasspoisonflyingbugdragon")) or (typeMove[Player_move] == "ice" and (type_1[Ai_Pokemon] in "fireice" or type_2[Ai_Pokemon] in "fireice")) or (typeMove[Player_move] == "fighting" and (type_1[Ai_Pokemon] in "poisonflyingpsychicbug" or type_2[Ai_Pokemon] in "poisonflyingpsychicbug")) or (typeMove[Player_move] == "poison" and (type_1[Ai_Pokemon] in "poisongroundrockghost" or type_2[Ai_Pokemon] in "poisongroundrockghost")) or (typeMove[Player_move] == "ground" and (type_1[Ai_Pokemon] in "grassbug" or type_2[Ai_Pokemon] in "grassbug")) or (typeMove[Player_move] == "flying" and (type_1[Ai_Pokemon] in "electricrock" or type_2[Ai_Pokemon] in "electricrock")) or (typeMove[Player_move] == "psychic" and (type_1[Ai_Pokemon] in "psychic" or type_2[Ai_Pokemon] in "psychic")) or (typeMove[Player_move] == "bug" and (type_1[Ai_Pokemon] in "firefightingflyingghost" or type_2[Ai_Pokemon] in "firefightingflyingghost")) or (typeMove[Player_move] == "rock" and (type_1[Ai_Pokemon] in "fightingground" or type_2[Ai_Pokemon] in "fightingground")):
								print("not very effective")
								modifier=0.5

							elif (typeMove[Player_move] == "fire" and (type_1[Ai_Pokemon] == "grassicebug" or type_2[Ai_Pokemon] == "grassicebug")) or (typeMove[Player_move] == "water" and (type_1[Ai_Pokemon] == "firegroundrock" or type_2[Ai_Pokemon] == "firegroundrock")) or (typeMove[Player_move] == "electric" and (type_1[Ai_Pokemon] == "waterflying" or type_2[Ai_Pokemon] == "waterflying")) or (typeMove[Player_move] == "grass" and (type_1[Ai_Pokemon] == "watergroundrock" or type_2[Ai_Pokemon] == "watergroundrock")) or (typeMove[Player_move] == "ice" and (type_1[Ai_Pokemon] == "grassgroundflyingdragon" or type_2[Ai_Pokemon] == "grassgroundflyingdragon")) or (typeMove[Player_move] == "fighting" and (type_1[Ai_Pokemon] == "normalicerock" or type_2[Ai_Pokemon] == "normalicerock")) or (typeMove[Player_move] == "poison" and (type_1[Ai_Pokemon] == "grassbug" or type_2[Ai_Pokemon] == "grassbug")) or (typeMove[Player_move] == "ground" and (type_1[Ai_Pokemon] == "fireelectricpoisonrock" or type_2[Ai_Pokemon] == "fireelectricpoisonrock")) or (typeMove[Player_move] == "flying" and (type_1[Ai_Pokemon] == "grassfightingbug" or type_2[Ai_Pokemon] == "grassfightingbug")) or (typeMove[Player_move] == "psychic" and (type_1[Ai_Pokemon] == "fightingpoison" or type_2[Ai_Pokemon] == "fightingpoison")) or (typeMove[Player_move] == "bug" and (type_1[Ai_Pokemon] == "grasspoisonpsychic" or type_2[Ai_Pokemon] == "grasspoisonpsychic")) or (typeMove[Player_move] == "rock" and (type_1[Ai_Pokemon] == "fireiceflyingbug" or type_2[Ai_Pokemon] == "fireiceflyingbug")) or (typeMove[Player_move] == "ghost" and (type_1[Ai_Pokemon] == "ghost" or type_2[Ai_Pokemon] == "ghost")) or (typeMove[Player_move] == "dragon" and (type_1[Ai_Pokemon] == "dragon" or type_2[Ai_Pokemon] == "dragon")):
								print("Very effective")
								modifier = 2

							elif (typeMove[Player_move] == "normal" and (type_1[Ai_Pokemon] == "ghost" or type_2[Ai_Pokemon] == "ghost")) or (typeMove[Player_move] == "electric" and (type_1[Ai_Pokemon] == "ground" or type_2[Ai_Pokemon] == "ground")) or (typeMove[Player_move] == "fighting" and (type_1[Ai_Pokemon] == "ghost" or type_2[Ai_Pokemon] == "ghost")) or (typeMove[Player_move] == "ground" and (type_1[Ai_Pokemon] == "flying" or type_2[Ai_Pokemon] == "flying")) or (typeMove[Player_move] == "ghost" and (type_1[Ai_Pokemon] == "normalpsychic" or type_2[Ai_Pokemon] == "normalpsychic")):
								print("No effect")
								modifier = 0

							else:
								print("yes")
								modifier = 1
							
							damage_dealt = round(((2*gamedata["PcLevel"][gamedata["party"][currentPokemon]]/5+2) * damage[Player_move] * (Player_attack[currentPokemon]/Ai_defence)/50+2) *modifier)
							Ai_health-=damage_dealt
							print("Damage dealt: " + str(damage_dealt) + " " + pokemon[Ai_Pokemon[AiCurrentPokemon]] + " has " + str(Ai_health[AiCurrentPokemon]) + " left")

						else:
							print("No effect")

					
					elif moveset[Player_move] in "Poison Gas Poison Powder Toxic":
						##poison
						Ai_status = "poison"
						Ai_status_length = 0
						
						print(pokemon[int(Ai_Pokemon[AiCurrentPokemon])] + " is now poisoned")
						print()
					

					elif moveset[Player_move] in "Confuse Ray Glare Stun Spore Supersonic Thunder Wave":
						##paralysis
						Ai_status = "paralysis"
						Ai_status_length = 0
						print(pokemon[int(Ai_Pokemon[AiCurrentPokemon])] + " is now paralysed")
						print()


					elif moveset[Player_move] in "Splash":
						##none
						print("Has no effect whatsoever.")
						print()
					

					elif moveset[Player_move] in "String Shot Whirlwind":
						##enemy-speed
						Ai_speed= round(float(Ai_speed[AiCurrentPokemon])* 0.95)
						print(pokemon[int(Ai_Pokemon[AiCurrentPokemon])] + " is now slower")
						print()

					
					elif moveset[Player_move] in "Leer Screech Tail Whip":
						##enemy-defence
						Ai_defence= round(float(Ai_defence[AiCurrentPokemon])* 0.95)
						print(pokemon[int(Ai_Pokemon[AiCurrentPokemon])] + "'s defence fell")
						print()

					
					elif moveset[Player_move] in "Growl Light Screen Mist Reflect Roar":
						##enemy-attack
						Ai_attack= round(float(Ai_attack[AiCurrentPokemon])* 0.95)
						print(pokemon[int(Ai_Pokemon[AiCurrentPokemon])] + "'s attack fell")
						print()
				
					elif moveset[Player_move] in "Flash Kinesis Minimize Sand Attack Smokescreen":
						##enemy-accuracy
						Ai_evasion= round(float(Ai_evasion[AiCurrentPokemon])* 0.95)
						print(pokemon[int(Ai_Pokemon[AiCurrentPokemon])] + "'s accuracy fell")
						print()

			else:
				print(pokemon[gamedata["Pc"][gamedata["party"][currentPokemon]]] + " misses.")
				print()

		
		## Ai Move calculation
		if Ai_paralysed == False:
			A_modifier = 1
			P =accuracy[Ai_turn] * (Ai_evasion/Player_evasion)
			hit_chance = randint(0,100)

			if P>=hit_chance or moveset[Ai_turn] in ["Hypnosis", "Lovely Kiss", "Sing", "Sleep Powder", "Spore", "Agility", "Double Team", "Teleport", "Recover", "Soft-Boiled", "Haze", "Leech Seed", "Rest", "Substitute", "Acid Armor", "Amnesia", "Barrier", "Conversion", "Defense Curl", "Disable", "Harden", "Withdraw", "Focus Energy", "Growth", "Meditate", "Sharpen", "Swords Dance", "Metronome", "Transform", "Mimic", "Mirror Move", "Poison Gas", "Poison Powder", "Toxic", "Confuse Ray", "Glare", "Stun Spore", "Supersonic", "Thunder Wave", "Splash", "String Shot", "Whirlwind", "Leer", "Screech", "Tail Whip", "Growl", "Light Screen", "Mist", "Reflect", "Roar", "Flash", "Kinesis", "Minimize", "Sand Attack", "Smokescreen"]:

				## Regular Moves
				if moveset[Ai_turn] not in ["Hypnosis", "Lovely Kiss", "Sing", "Sleep Powder", "Spore", "Agility", "Double Team", "Teleport", "Recover", "Soft-Boiled", "Haze", "Leech Seed", "Rest", "Substitute", "Acid Armor", "Amnesia", "Barrier", "Conversion", "Defense Curl", "Disable", "Harden", "Withdraw", "Focus Energy", "Growth", "Meditate", "Sharpen", "Swords Dance", "Metronome", "Transform", "Mimic", "Mirror Move", "Poison Gas", "Poison Powder", "Toxic", "Confuse Ray", "Glare", "Stun Spore", "Supersonic", "Thunder Wave", "Splash", "String Shot", "Whirlwind", "Leer", "Screech", "Tail Whip", "Growl", "Light Screen", "Mist", "Reflect", "Roar", "Flash", "Kinesis", "Minimize", "Sand Attack", "Smokescreen"]:	
					
					##innefective move
					if moveset[Player_move] not in ["Hypnosis", "Lovely Kiss", "Sing", "Sleep Powder", "Spore", "Agility", "Double Team", "Teleport", "Recover", "Soft-Boiled", "Haze", "Leech Seed", "Rest", "Substitute", "Acid Armor", "Amnesia", "Barrier", "Conversion", "Defense Curl", "Disable", "Harden", "Withdraw", "Focus Energy", "Growth", "Meditate", "Sharpen", "Swords Dance", "Metronome", "Transform", "Mimic", "Mirror Move", "Poison Gas", "Poison Powder", "Toxic", "Confuse Ray", "Glare", "Stun Spore", "Supersonic", "Thunder Wave", "Splash", "String Shot", "Whirlwind", "Leer", "Screech", "Tail Whip", "Growl", "Light Screen", "Mist", "Reflect", "Roar", "Flash", "Kinesis", "Minimize", "Sand Attack", "Smokescreen"]:	
						
						##innefective move
						if (typeMove[Player_move] in "normal" and (type_1[int(Ai_Pokemon[AiCurrentPokemon])] in "rock" or type_2[int(Ai_Pokemon[AiCurrentPokemon])] in "rock")) or (typeMove[Player_move] in "fire" and (type_1[int(Ai_Pokemon[AiCurrentPokemon])] in "firewaterrockdragon" or type_2[int(Ai_Pokemon[AiCurrentPokemon])] in "firewaterrockdragon")) or (typeMove[Player_move] in "water" and (type_1[int(Ai_Pokemon[AiCurrentPokemon])] in "watergrassdragon" or type_2[int(Ai_Pokemon[AiCurrentPokemon])] in "watergrassdragon")) or (typeMove[Player_move] in "electric" and (type_1[int(Ai_Pokemon[AiCurrentPokemon])] in "electricgrassdragon" or type_2[int(Ai_Pokemon[AiCurrentPokemon])] in "electricgrassdragon")) or (typeMove[Player_move] in "grass" and (type_1[int(Ai_Pokemon[AiCurrentPokemon])] in "firegrasspoisonflyingbugdragon" or type_2[int(Ai_Pokemon[AiCurrentPokemon])] in "firegrasspoisonflyingbugdragon")) or (typeMove[Player_move] in "ice" and (type_1[int(Ai_Pokemon[AiCurrentPokemon])] in "fireice" or type_2[int(Ai_Pokemon[AiCurrentPokemon])] in "fireice")) or (typeMove[Player_move] in "fighting" and (type_1[int(Ai_Pokemon[AiCurrentPokemon])] in "poisonflyingpsychicbug" or type_2[int(Ai_Pokemon[AiCurrentPokemon])] in "poisonflyingpsychicbug")) or (typeMove[Player_move] in "poison" and (type_1[int(Ai_Pokemon[AiCurrentPokemon])] in "poisongroundrockghost" or type_2[int(Ai_Pokemon[AiCurrentPokemon])] in "poisongroundrockghost")) or (typeMove[Player_move] in "ground" and (type_1[int(Ai_Pokemon[AiCurrentPokemon])] in "grassbug" or type_2[int(Ai_Pokemon[AiCurrentPokemon])] in "grassbug")) or (typeMove[Player_move] in "flying" and (type_1[int(Ai_Pokemon[AiCurrentPokemon])] in "electricrock" or type_2[int(Ai_Pokemon[AiCurrentPokemon])] in "electricrock")) or (typeMove[Player_move] in "psychic" and (type_1[int(Ai_Pokemon[AiCurrentPokemon])] in "psychic" or type_2[int(Ai_Pokemon[AiCurrentPokemon])] in "psychic")) or (typeMove[Player_move] in "bug" and (type_1[int(Ai_Pokemon[AiCurrentPokemon])] in "firefightingflyingghost" or type_2[int(Ai_Pokemon[AiCurrentPokemon])] in "firefightingflyingghost")) or (typeMove[Player_move] in "rock" and (type_1[int(Ai_Pokemon[AiCurrentPokemon])] in "fightingground" or type_2[int(Ai_Pokemon[AiCurrentPokemon])] in "fightingground")):
							A_modifier=0.5

						##Effective move
						elif (typeMove[Player_move] in "fire" and (type_1[int(Ai_Pokemon[AiCurrentPokemon])] in "grassicebug" or type_2[int(Ai_Pokemon[AiCurrentPokemon])] in "grassicebug")) or (typeMove[Player_move] in "water" and (type_1[int(Ai_Pokemon[AiCurrentPokemon])] in "firegroundrock" or type_2[int(Ai_Pokemon[AiCurrentPokemon])] in "firegroundrock")) or (typeMove[Player_move] in "electric" and (type_1[int(Ai_Pokemon[AiCurrentPokemon])] in "waterflying" or type_2[int(Ai_Pokemon[AiCurrentPokemon])] in "waterflying")) or (typeMove[Player_move] in "grass" and (type_1[int(Ai_Pokemon[AiCurrentPokemon])] in "watergroundrock" or type_2[int(Ai_Pokemon[AiCurrentPokemon])] in "watergroundrock")) or (typeMove[Player_move] in "ice" and (type_1[int(Ai_Pokemon[AiCurrentPokemon])] in "grassgroundflyingdragon" or type_2[int(Ai_Pokemon[AiCurrentPokemon])] in "grassgroundflyingdragon")) or (typeMove[Player_move] in "fighting" and (type_1[int(Ai_Pokemon[AiCurrentPokemon])] in "normalicerock" or type_2[int(Ai_Pokemon[AiCurrentPokemon])] in "normalicerock")) or (typeMove[Player_move] in "poison" and (type_1[int(Ai_Pokemon[AiCurrentPokemon])] in "grassbug" or type_2[int(Ai_Pokemon[AiCurrentPokemon])] in "grassbug")) or (typeMove[Player_move] in "ground" and (type_1[int(Ai_Pokemon[AiCurrentPokemon])] in "fireelectricpoisonrock" or type_2[int(Ai_Pokemon[AiCurrentPokemon])] in "fireelectricpoisonrock")) or (typeMove[Player_move] in "flying" and (type_1[int(Ai_Pokemon[AiCurrentPokemon])] in "grassfightingbug" or type_2[int(Ai_Pokemon[AiCurrentPokemon])] in "grassfightingbug")) or (typeMove[Player_move] in "psychic" and (type_1[int(Ai_Pokemon[AiCurrentPokemon])] in "fightingpoison" or type_2[int(Ai_Pokemon[AiCurrentPokemon])] in "fightingpoison")) or (typeMove[Player_move] in "bug" and (type_1[int(Ai_Pokemon[AiCurrentPokemon])] in "grasspoisonpsychic" or type_2[int(Ai_Pokemon[AiCurrentPokemon])] in "grasspoisonpsychic")) or (typeMove[Player_move] in "rock" and (type_1[int(Ai_Pokemon[AiCurrentPokemon])] in "fireiceflyingbug" or type_2[int(Ai_Pokemon[AiCurrentPokemon])] in "fireiceflyingbug")) or (typeMove[Player_move] in "ghost" and (type_1[int(Ai_Pokemon[AiCurrentPokemon])] in "ghost" or type_2[int(Ai_Pokemon[AiCurrentPokemon])] in "ghost")) or (typeMove[Player_move] in "dragon" and (type_1[int(Ai_Pokemon[AiCurrentPokemon])] in "dragon" or type_2[int(Ai_Pokemon[AiCurrentPokemon])] in "dragon")):
							A_modifier = 2

						## No Effect move
						elif (typeMove[Player_move] in "normal" and (type_1[int(Ai_Pokemon[AiCurrentPokemon])] in "ghost" or type_2[int(Ai_Pokemon[AiCurrentPokemon])] in "ghost")) or (typeMove[Player_move] in "electric" and (type_1[int(Ai_Pokemon[AiCurrentPokemon])] in "ground" or type_2[int(Ai_Pokemon[AiCurrentPokemon])] in "ground")) or (typeMove[Player_move] in "fighting" and (type_1[int(Ai_Pokemon[AiCurrentPokemon])] in "ghost" or type_2[int(Ai_Pokemon[AiCurrentPokemon])] in "ghost")) or (typeMove[Player_move] in "ground" and (type_1[int(Ai_Pokemon[AiCurrentPokemon])] in "flying" or type_2[int(Ai_Pokemon[AiCurrentPokemon])] in "flying")) or (typeMove[Player_move] in "ghost" and (type_1[int(Ai_Pokemon[AiCurrentPokemon])] in "normalpsychic" or type_2[int(Ai_Pokemon[AiCurrentPokemon])] in "normalpsychic")):
							A_modifier = 0

						##Normal effect move
						else:
							A_modifier = 1

						Ai_damage_dealt = math.ceil(((2*int(Ai_level[AiCurrentPokemon])/5+2) * damage[Ai_turn] * (int(Ai_attack[AiCurrentPokemon])/Player_defence[currentPokemon])/50+2) *A_modifier)


					##Status effects
		
				## Special Moves
				else:
					A_modifier = 1
					if moveset[Ai_turn] in "Hypnosis Lovely Kiss Sing Sleep Powder Spore":
						##sleep
						Player_status = "Sleep"
						Player_status_length = 0
						print("You are now  asleep")

					elif moveset[Ai_turn] in "Agility Double Team Teleport":
						##self-speed
						Ai_speed = round(float(Ai_speed)* 1.05)
						print("The Ai's speed rose")

					elif moveset[Ai_turn] in "Recover Soft-Boiled":
						##Self-heal half
						if Ai_health <= round(1/2*(HP[Ai_Pokemon[AiCurrentPokemon]]*2 + int(Ai_level[AiCurrentPokemon])/100+int(Ai_level[AiCurrentPokemon])+10)):
							Ai_health= Ai_health[AiCurrentPokemon] + round(1/2*(HP[Ai_Pokemon[AiCurrentPokemon]]*2 + int(Ai_level[AiCurrentPokemon])/100+int(Ai_level[AiCurrentPokemon])+10))
						else: 
							Ai_health = round(HP[Ai_Pokemon[AiCurrentPokemon]]*2 + int(Ai_level[AiCurrentPokemon])/100+int(Ai_level[AiCurrentPokemon])+10)

						print("Ai Heals itself")

					elif moveset[Ai_turn] in "Haze Leech Seed Rest Substitute":
						##self-heal
						Ai_status="healing"
						Ai_status_length = 0
						print("The Ai is healing itself")

					elif moveset[Ai_turn] in "Acid Armor Amnesia Barrier Conversion Defense Curl Disable Harden Withdraw":
						##self-defense
						Ai_defence  = round(float(Ai_defence[AiCurrentPokemon])* 1.05)

						print("The Ai's defence rose")

					elif moveset[Ai_turn] in "Focus Energy Growth Meditate Sharpen Swords Dance":
						##self-attack
						Ai_attack  = round(float(Ai_attack[AiCurrentPokemon])* 1.05)
						print("The Ai's attack rose")

					elif moveset[Ai_turn] in "Metronome Transform Mimic Mirror Move":
						##random move
						Ai_turn = randint(0,len(moveset[AiCurrentPokemon])-1)
						if moveset[Ai_turn] not in "Acid Armor Agility Amnesia Barrier Confuse Ray Conversion Defense Curl Disable Double Team Flash Focus Energy Glare Growl Growth Harden Haze Hypnosis Kinesis Leech Seed Leer Light Screen Lovely Kiss Meditate Metronome Mimic Minimize Mirror Move Mist Poison Gas Poison Powder Recover Reflect Rest Roar Sand Attack Screech Sharpen Sing Sleep Powder Smokescreen Soft-Boiled Splash Spore String Shot Stun Spore Substitute Supersonic Swords Dance Tail Whip Teleport Thunder Wave Toxic Transform Whirlwind Withdraw":	
							
							
							##innefective move
							if (typeMove[Ai_turn] in "normal" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "rock" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "rock")) or (typeMove[Ai_turn] in "fire" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "firewaterrockdragon" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "firewaterrockdragon")) or (typeMove[Ai_turn] in "water" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "watergrassdragon" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "watergrassdragon")) or (typeMove[Ai_turn] in "electric" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "electricgrassdragon" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "electricgrassdragon")) or (typeMove[Ai_turn] in "grass" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "firegrasspoisonflyingbugdragon" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "firegrasspoisonflyingbugdragon")) or (typeMove[Ai_turn] in "ice" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "fireice" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "fireice")) or (typeMove[Ai_turn] in "fighting" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "poisonflyingpsychicbug" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "poisonflyingpsychicbug")) or (typeMove[Ai_turn] in "poison" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "poisongroundrockghost" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "poisongroundrockghost")) or (typeMove[Ai_turn] in "ground" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "grassbug" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "grassbug")) or (typeMove[Ai_turn] in "flying" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "electricrock" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "electricrock")) or (typeMove[Ai_turn] in "psychic" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "psychic" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "psychic")) or (typeMove[Ai_turn] in "bug" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "firefightingflyingghost" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "firefightingflyingghost")) or (typeMove[Ai_turn] in "rock" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "fightingground" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "fightingground")):						
								A_modifier=0.5

							##Effective move
							elif (typeMove[Ai_turn] in "fire" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "grassicebug" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "grassicebug")) or (typeMove[Ai_turn] in "water" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "firegroundrock" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "firegroundrock")) or (typeMove[Ai_turn] in "electric" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "waterflying" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "waterflying")) or (typeMove[Ai_turn] in "grass" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "watergroundrock" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "watergroundrock")) or (typeMove[Ai_turn] in "ice" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "grassgroundflyingdragon" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "grassgroundflyingdragon")) or (typeMove[Ai_turn] in "fighting" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "normalicerock" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "normalicerock")) or (typeMove[Ai_turn] in "poison" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "grassbug" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "grassbug")) or (typeMove[Ai_turn] in "ground" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "fireelectricpoisonrock" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "fireelectricpoisonrock")) or (typeMove[Ai_turn] in "flying" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "grassfightingbug" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "grassfightingbug")) or (typeMove[Ai_turn] in "psychic" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "fightingpoison" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "fightingpoison")) or (typeMove[Ai_turn] in "bug" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "grasspoisonpsychic" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "grasspoisonpsychic")) or (typeMove[Ai_turn] in "rock" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "fireiceflyingbug" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "fireiceflyingbug")) or (typeMove[Ai_turn] in "ghost" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "ghost" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "ghost")) or (typeMove[Ai_turn] in "dragon" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "dragon" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "dragon")):						
								A_modifier = 2

							## No Effect move
							elif (typeMove[Ai_turn] in "normal" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "ghost" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "ghost")) or (typeMove[Ai_turn] in "electric" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "ground" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "ground")) or (typeMove[Ai_turn] in "fighting" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "ghost" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "ghost")) or (typeMove[Ai_turn] in "ground" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "flying" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "flying")) or (typeMove[Ai_turn] in "ghost" and (type_1[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "normalpsychic" or type_2[gamedata["Pc"][gamedata["party"][currentPokemon]]] in "normalpsychic")):
								A_modifier = 0

							##Normal effect move
							else:
								A_modifier = 1

							Ai_damage_dealt = round(((2*Ai_level/5+2) * damage[Ai_turn] * (Ai_attack/Player_defence[currentPokemon])/50+2) *A_modifier)

						else:
							A_modifier = 0 

					elif moveset[Ai_turn] in "Poison Gas Poison Powder Toxic":
						##poison
						Player_status = "poison"
						Player_status_length = 0
						print("You are poisoned")

					elif moveset[Ai_turn] in "Confuse Ray Glare Stun Spore Supersonic Thunder Wave":
						##paralysis
						Player_status = "paralysis"
						Player_status_length = 0
						print("You are now paralysed")

					elif moveset[Ai_turn] in "Splash":
						##none
						print("Has no effect whatsoever.")

					elif moveset[Ai_turn] in "String Shot Whirlwind":
						##enemy-speed
						Player_speed[currentPokemon] = round(float(Player_speed[currentPokemon])*0.95)
						print("Your speed fell")

					elif moveset[Ai_turn] in "Leer Screech Tail Whip":
						##enemy-defence
						Player_defence[currentPokemon]= round(float(Player_defence[currentPokemon])*0.95)
						print("Your defence fell")

					elif moveset[Ai_turn] in "Growl Light Screen Mist Reflect Roar":
						##enemy-attack
						Player_attack[currentPokemon]= round(float(Player_attack[currentPokemon])*0.95)
						print("Your attack fell")

					elif moveset[Player_move] in "Flash Kinesis Minimize Sand Attack Smokescreen":
						##enemy-accuracy
						Player_evasion[currentPokemon]= round(float(Player_evasion[currentPokemon])*0.95)
						print("Your accuracy fell")

			else:
				print(pokemon[int(Ai_Pokemon[AiCurrentPokemon])] + " misses.")
				print()

		else:
			A_modifier = 1
		##Move order
		
		if Player_speed[currentPokemon]>Ai_speed[AiCurrentPokemon] and Player_move!=-1:
			print(pokemon[gamedata["Pc"][gamedata["party"][currentPokemon]]] + " uses " + moveset[Player_move])
			Ai_health[AiCurrentPokemon]-=damage_dealt
		
			if modifier == 0.5:
				print("Not very effective")
			elif modifier == 2:
				print("Very Effective")
			elif modifier == 0:
				print("No effect")

			print("Damage dealt: " + str(damage_dealt) + " " + pokemon[int(Ai_Pokemon[AiCurrentPokemon])] + " has " + str(Ai_health[AiCurrentPokemon]) + " left")
			print()

			if int(Ai_health[AiCurrentPokemon])>0:
				print(pokemon[int(Ai_Pokemon[AiCurrentPokemon])] + " uses " + moveset[Ai_turn])
				Player_health[currentPokemon]-=Ai_damage_dealt
				
				if A_modifier == 0.5:
					print("Not very effective")
				elif A_modifier == 2:
					print("Very Effective")
				elif A_modifier == 0:
					print("No effect")

				print("Damage dealt: " + str(Ai_damage_dealt) + " " + pokemon[gamedata["Pc"][gamedata["party"][currentPokemon]]] + " has " + str(Player_health[currentPokemon]) + " left")
				
				
				if Player_health[currentPokemon] <= 0:	
					##Choose next pokemon
					print(pokemon[gamedata["Pc"][gamedata["party"][currentPokemon]]] + " Fainted")
					i=0
					for x in Player_health:
						if x>0:
							currentPokemon=i
							print("Go " + pokemon[gamedata["Pc"][gamedata["party"][currentPokemon]]] + "!")
							break
						i+=1
					if Player_health[currentPokemon] <= 0:
						print("You black out")
						break

			else:
				### Calculate XP
				xp_recieved = round((152*int(Ai_level[AiCurrentPokemon])/5)*(((2*int(Ai_level[AiCurrentPokemon])+10)**2.5)/(int(Ai_level[AiCurrentPokemon]) + gamedata["PcLevel"][gamedata["party"][currentPokemon]] + 10)**2.5+1))

				print("xp Earned: " + str(xp_recieved))
				gamedata["xp"][gamedata["party"][currentPokemon]]+=xp_recieved

				##Required xp to level up
				xp_table = [8,19,37,61,91,127,169,217,271,331,397,469,547,631,721,817,919,1027,1141,1261,1387,1519,1657,1801,1951,2107,2269,2437,2611,2791,2977,3169,3367,3571,3781,3997,4219,4447,4681,4921,5167,5419,5677,5941,6211,6487,6769,7057,7351,7651,7957,8269,8587,8911,9241,9577,9919,10267,10621,10981,11347,11719,12097,12481,12871,13267,13669,14077,14491,14911,15337,15769,16207,16651,17101,17557,18019,18487,18961,19441,19927,20419,20917,21421,21931,22447,22969,23497,24031,24571,25117,25669,26227,26791,27361,27937,28519,29107,29701,9999999999999999999999]
				
				##Level up
				if gamedata["xp"][gamedata["party"][currentPokemon]] >= xp_table[gamedata["PcLevel"][gamedata["party"][currentPokemon]]-1]:
					
					gamedata["xp"][gamedata["party"][currentPokemon]] -= xp_table[gamedata["PcLevel"][gamedata["party"][currentPokemon]]-1]
					gamedata["PcLevel"][gamedata["party"][currentPokemon]]+=1
					
					print(pokemon[gamedata["Pc"][gamedata["party"][currentPokemon]]] + " Levelled Up! They are now level " + str(gamedata["PcLevel"][gamedata["party"][currentPokemon]]))
					
					##New move
					if gamedata["PcLevel"][gamedata["party"][currentPokemon]]%2 ==0:
						temp = learnsets[gamedata["Pc"][gamedata["party"][currentPokemon]]].split("-")

						while True:
							new_move = randint(0,len(temp)-1)
							
							if temp[new_move] not in gamedata["PcMoves"][gamedata["party"][currentPokemon]]:
								
								print(pokemon[gamedata["Pc"][gamedata["party"][currentPokemon]]] + " would like to learn the move:")
								print(moveset[int(temp[new_move])] + " Damage: " + str(damage[int(temp[new_move])]) + " Accuracy: " + str(accuracy[int(temp[new_move])]) + " Type: " + typeMove[int(temp[new_move])])

								game = 0
								##Learn move
								while game != "yes" and game != "no":
									game = input("would you like to learn it? ")
									if game == 'no':
										print(pokemon[gamedata["Pc"][gamedata["party"][currentPokemon]]] + " does not learn the move")

									elif game == "yes":
										i=0

										gamedata["PcMoves"][gamedata["party"][currentPokemon]].split("-")
										for x in gamedata["PcMoves"][gamedata["party"][currentPokemon]].split("-"):
											print("#"+str(i)+ " " + moveset[int(x)] + " Damage: " + str(damage[int(x)]) + " Accuracy: " + str(accuracy[int(x)]) + " Type: " + typeMove[int(x)])
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
					if (gamedata["PcLevel"][gamedata["party"][currentPokemon]] > 25 and evolve[gamedata["Pc"][gamedata["party"][currentPokemon]]] <=0 and evolve[gamedata["Pc"][gamedata["party"][currentPokemon]]] < evolve[gamedata["Pc"][gamedata["party"][currentPokemon]]+1]) or (gamedata["PcLevel"][gamedata["party"][currentPokemon]] > 50 and evolve[gamedata["Pc"][gamedata["party"][currentPokemon]]] <=2 and evolve[gamedata["Pc"][gamedata["party"][currentPokemon]]] < evolve[gamedata["Pc"][gamedata["party"][currentPokemon]]+1]):

						gamedata["Pc"][gamedata["party"][currentPokemon]]+=1
						print( pokemon[gamedata["Pc"][gamedata["party"][currentPokemon]]-1] + " Evolves! They are now " + pokemon[gamedata["Pc"][gamedata["party"][currentPokemon]]])

				##next pokemon
				i=0
				for x in Ai_health:
					if int(x)>0 and int(Ai_Pokemon[AiCurrentPokemon])<152:
						print(pokemon[int(Ai_Pokemon[AiCurrentPokemon])] + " faints.")
						AiCurrentPokemon=i
						print("Go " + pokemon[int(Ai_Pokemon[AiCurrentPokemon])] + "!")
						break
					i+=1

				if Ai_health[AiCurrentPokemon]<=0:
					gamedata["BattleWon"] +=1
					print("Trainer is out of pokemon. You win!")
					gamedata["money"] += 1000
					print("You earned $1000! You now have $" + str(gamedata["money"]))
					save()
					break

		##Ai Moves first
		else:
			print(pokemon[int(Ai_Pokemon[AiCurrentPokemon])] + " uses " + moveset[Ai_turn])
			Player_health[currentPokemon]-=Ai_damage_dealt
				
			if A_modifier == 0.5:
				print("Not very effective")
			elif A_modifier == 2:
				print("Very Effective")
			elif A_modifier == 0:
				print("No effect")

			print("Damage dealt: " + str(Ai_damage_dealt) + " " + pokemon[gamedata["Pc"][gamedata["party"][currentPokemon]]] + " has " + str(Player_health[currentPokemon]) + " left")
			print()

			if Player_health[currentPokemon]>0 and Player_move!=-1:
				print(pokemon[gamedata["Pc"][gamedata["party"][currentPokemon]]] + " uses " + moveset[Player_move])
				Ai_health[AiCurrentPokemon]-=damage_dealt
				
				if modifier == 0.5:
					print("Not very effective")
				elif modifier == 2:
					print("Very Effective")
				elif modifier == 0:
					print("No effect")

				print("Damage dealt: " + str(damage_dealt) + " " + pokemon[int(Ai_Pokemon[AiCurrentPokemon])] + " has " + str(Ai_health[AiCurrentPokemon]) + " left")

				if int(Ai_health[AiCurrentPokemon])<=0:
					### Calculate XP
					xp_recieved = round((152*int(Ai_level[AiCurrentPokemon])/5)*(((2*int(Ai_level[AiCurrentPokemon])+10)**2.5)/(int(Ai_level[AiCurrentPokemon]) + gamedata["PcLevel"][gamedata["party"][currentPokemon]] + 10)**2.5+1))

					print("xp Earned: " + str(xp_recieved))
					gamedata["xp"][gamedata["party"][currentPokemon]]+=xp_recieved

					##Required xp to level up
					xp_table = [8,19,37,61,91,127,169,217,271,331,397,469,547,631,721,817,919,1027,1141,1261,1387,1519,1657,1801,1951,2107,2269,2437,2611,2791,2977,3169,3367,3571,3781,3997,4219,4447,4681,4921,5167,5419,5677,5941,6211,6487,6769,7057,7351,7651,7957,8269,8587,8911,9241,9577,9919,10267,10621,10981,11347,11719,12097,12481,12871,13267,13669,14077,14491,14911,15337,15769,16207,16651,17101,17557,18019,18487,18961,19441,19927,20419,20917,21421,21931,22447,22969,23497,24031,24571,25117,25669,26227,26791,27361,27937,28519,29107,29701,9999999999999999999999]
					
					##Level up
					if gamedata["xp"][gamedata["party"][currentPokemon]] >= xp_table[gamedata["PcLevel"][gamedata["party"][currentPokemon]]-1]:
						
						gamedata["xp"][gamedata["party"][currentPokemon]] -= xp_table[gamedata["PcLevel"][gamedata["party"][currentPokemon]]-1]
						gamedata["PcLevel"][gamedata["party"][currentPokemon]]+=1
						
						print(pokemon[gamedata["Pc"][gamedata["party"][currentPokemon]]] + " Levelled Up! They are now level " + str(gamedata["PcLevel"][gamedata["party"][currentPokemon]]))
						
						##New move
						if gamedata["PcLevel"][gamedata["party"][currentPokemon]]%2 ==0:
							temp = learnsets[gamedata["Pc"][gamedata["party"][currentPokemon]]].split("-")

							while True:
								new_move = randint(0,len(temp)-1)
								
								if temp[new_move] not in gamedata["PcMoves"][gamedata["party"][currentPokemon]]:
									
									print(pokemon[gamedata["Pc"][gamedata["party"][currentPokemon]]] + " would like to learn the move:")
									print(moveset[int(temp[new_move])] + " Damage: " + str(damage[int(temp[new_move])]) + " Accuracy: " + str(accuracy[int(temp[new_move])]) + " Type: " + typeMove[int(temp[new_move])])

									game = 0
									##Learn move
									while game != "yes" and game != "no":
										game = input("would you like to learn it? ")
										if game == 'no':
											print(pokemon[gamedata["Pc"][gamedata["party"][currentPokemon]]] + " does not learn the move")

										elif game == "yes":
											i=0

											gamedata["PcMoves"][gamedata["party"][currentPokemon]].split("-")
											for x in gamedata["PcMoves"][gamedata["party"][currentPokemon]].split("-"):
												print("#"+str(i)+ " " + moveset[int(x)] + " Damage: " + str(damage[int(x)]) + " Accuracy: " + str(accuracy[int(x)]) + " Type: " + typeMove[int(x)])
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
						if (gamedata["PcLevel"][gamedata["party"][currentPokemon]] > 25 and evolve[gamedata["Pc"][gamedata["party"][currentPokemon]]] <=0 and evolve[gamedata["Pc"][gamedata["party"][currentPokemon]]] < evolve[gamedata["Pc"][gamedata["party"][currentPokemon]]+1]) or (gamedata["PcLevel"][gamedata["party"][currentPokemon]] > 50 and evolve[gamedata["Pc"][gamedata["party"][currentPokemon]]] <=2 and evolve[gamedata["Pc"][gamedata["party"][currentPokemon]]] < evolve[gamedata["Pc"][gamedata["party"][currentPokemon]]+1]):

							gamedata["Pc"][gamedata["party"][currentPokemon]]+=1
							print( pokemon[gamedata["Pc"][gamedata["party"][currentPokemon]]-1] + " Evolves! They are now " + pokemon[gamedata["Pc"][gamedata["party"][currentPokemon]]])
						

					##next pokemon
					
					i=0
					for x in Ai_health:
						if int(x)>0 and int(Ai_Pokemon[AiCurrentPokemon])<152:
							print(pokemon[int(Ai_Pokemon[AiCurrentPokemon])] + " faints.")
							AiCurrentPokemon=i
							print("Go " + pokemon[int(Ai_Pokemon[AiCurrentPokemon])] + "!")
							break
						i+=1

					if Ai_health[AiCurrentPokemon]<=0:
						gamedata["BattleWon"]+=1
						print("Trainer is out of pokemon. You win!")
						gamedata["money"] += 1000
						print("You earned $1000! You now have $" + str(gamedata["money"]))
						save()
						break


			elif Player_health[currentPokemon] <= 0:
				##Choose next pokemon
				print(pokemon[gamedata["Pc"][gamedata["party"][currentPokemon]]] + " Fainted")
				i=0
				for x in Player_health:
					if x>0:
						currentPokemon=i
						print("Go " + pokemon[gamedata["Pc"][gamedata["party"][currentPokemon]]] + "!")
						break
					i+=1
				if Player_health[currentPokemon] <= 0:
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

	else:
		print("invalid response (input 'help' for a list of commands. This is available on almost any screen)")
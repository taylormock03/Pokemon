# This is where the user will first go to the store and be sent to sub areas
from Lib.Init.ItemInit import CatchItem, HealItem


def storeInit(player):
    print("Welcome Trainer! You have $" + str(player.getMoney()))
    
    selection = ""
    while selection != "leave":
        selection = input("What are you looking for \n#1 Pokeballs\n#2 Healing Items\n#3 Status Healers\nOr just type 'leave' to go on your way\n>")

        if selection == "1":
            catchItems(player)
        if selection == "2":
            healItems(player)
        if selection == "3":
            statusItems(player)
        if selection == "leave":
            break

# This is where items that can catch pokemon are bought (such as pokeballs)
def catchItems(player):
    items = []
    # Add catch items to a list
    items.append(CatchItem("Poke Ball",100,1))
    items.append(CatchItem("Great Ball",200,1.5))
    items.append(CatchItem("Ultra Ball",300,2))
    items.append(CatchItem("Master Ball",1000,1000))

    # iterate through the item list and print out the items
    print("We have:")
    i = 1
    for x in items:
        print ("#" + str(i) + " " + str(x) +"\n")
        i+=1
    
    print("Or enter 0 to leave without anything")
    while True:
        try:
            selection = int(input("What would you like? ")-1)

            if selection == -1:
                break
            elif selection >=0 and selection <len(items):
                quanity = int(input("How many would you like? "))
                items[selection].buyItem(quanity,player)
            else:
                raise
        
        except:
            print("Invalid input")

            
         

def healItems(player):
    return

def statusItems(player):
    return

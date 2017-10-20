print("\n")
print("Escape the Paperclip Factory")
print("\n")
print("Your eyes open slowly. The concrete feels cold upon your cheek. \nYou realise that you're in some kind of office.\nA voice rings out across the speakers:")


name = input('"WHAT IS YOUR NAME?"')
health = 100

print('"Welcome to the game {0}!"'.format(name))
print("Your health is at {0}.".format(health))
print("\n")

good_location_choosen = False
while not good_location_choosen:
    
    location = input("There are two doors out of here. North or South? n/s") 

    if location == "n": 
        print("Ok {0}, North it is.".format(name))
        good_location_choosen = True 
        print("You find a health pack")
        health = health * 2
    elif location == "s":
        print("Ok {0}, South it is.".format(name))
        good_location_choosen = True  
        print("You run into trouble and take a hit to the head!")
        health = health / 2 
        print('It\'s some kind of drone! It flys away. \n{0}:"What was that thing??"'.format(name))    
    else : 
        print("That's not an option {0}".format(name))


print("Your health is at {0}".format(health))
print('{0}:"What is this place?"'.format(name))
print("\n")

switch_chosen = False
while not switch_chosen:

    switch = input("You are on a suspended walkway in some kind of factory. \nYou see a light switch. Turn it on? y/n") 
   
    if switch == "y":
        print("The light comes on. You see paperclips strewn everywhere.")
        print('{0}:"That paperclip bastard must have kidnapped me! \nI\'ll find him and kill him!!"'.format(name))
        switch_chosen = True
    elif switch == "n":
        print("You take a cautious step in the dark. Something crunches underfoot. A paperclip!")
        print('{0}:"That paperclip bastard must have kidnapped me! \nI\'ll find him - and I\'ll kill him!!"'.format(name))
        switch_chosen = True 
    else :
        print("Pick an option {0}!".format(name))

#Game version 1
#  Llopis 15/01/2014
# This is some kind of MUD game, but not multiplayer and not in dungeons :D
# So this is more like an RPG: SUR Single Untested RRGP ;)

# Importing thins that must be in the same folder:
from fight import *         # Import how the fight is done
from Place import *         # Import the map, and the generator
from characters import *    # Import the characters definitions
import numpy as np

Menu="""
WELCOME TO SPM GAME
(SINGLE PLAYER MAP GAME)

Please choose an option:
 - Start a new game (N)
 - Load a saved game (L)
 - Save the game (S)
 - About this game (A)
 - Instructions (I)
 
You want to:"""
# Defining some general things
typic_answer=("yes", "y", "no", "n", "quit", "q")
typic_sentence="It is a Yes or Not question, please introduce a valid input.\nTo exit type 'quit' or 'q'"

#History
print("""
    This game is in memory of the first multiplayer games like MUD
    (Althought I never played them), they cannot be forget. \n\n""")


def game():
    print("Our history begins far far away, when the dragons and goblins still dominated the Middle Earth.\n"\
          "In that time a man named...")
    name=input("What is your name?/How do you want to name him?\t")
    # Doesn't need to check it can be all numbers.
    print("Started to think about conquering the world and free it of the nasty creatures!\n"\
      "At the age of...")

    # Check if it is a valid input of age
    while True:
        try:
            age=int(input("When do you guess?\t"))
            break
        except:
            print("Please introduce a number!")

    print("Yes, at the age of", age, "he began to fight against terrible creatures near their house.\n"\
      "So he got himself a wook sword and started to travel...")
    print("He knew there were many terrible creatures but he was not afraid of them...")

    # Creating protagonist
    prota=Hero(age=age, name=name)

    question1="Do you want to fight?\t"
    question2="Do you want to fight again?\t"
    move="Do you want to move?\t"
    direction="Where do you want to move to (N,S,E,W)? \t"
    movement=0
    map1=Maping()
    i=j=(map1.positions.shape[1]+1)/2
    #a=Player("Manolo", i+1, j+1)

    print("He was at his house when he decided to go out, and help other people however he could.",
      "\nSo he decided to go outside towards..")

    #A condition to keep playing
    while prota.health>0:

        # Asks if he want to move
        ma=input(move)
        # Check if it it is a valid answer
        if ma.lower() in typic_answer:
            # If the answer is yes ask in which direction
            if ma.lower()=='y' or ma.lower()=='yes':
                da=input(direction)
                movement+=1
                # Check if it is a valid direction, 
                while da.lower()not in ('n', 's', 'e','w', 'nord', 'south', 'east', 'west'):
                    print("Please introduce a valid input")
                    da=input(direction)
                # If the desired direction is nord, or n
                if da.lower()=='n'or da.lower()=='nord':
                    i+=1
                    if i==map1.positions.shape[1]:
                        i=0
                        # If there is a mountain in theplace it cannot cross it
                        # TODO improve this for every direction and sea/lake if in the inventory there is no boat
                        # TODO set direction of fow for rivers, and just be able to cros some of them (the others are unable to cross them)
                    if map1.places[i,j].place=="mountain" or map1.places[i,j].place=="high mountain":
                        print("Ok, look what you see in the next zone: a", map1.places[i,j].place)
                        print(map1.places[i, j])
                        print("I can't cross the mountain. I should move around it.")
                        i-=1
                    else:
                        print("Ok, look what you see in the next zone: a", map1.places[i,j].place)
                        
                # If the desired direction is south or s
                elif da.lower()=='s'or da.lower()=='south':
                    i-=1
                    if i<0:
                        i=map1.positions.shape[1]-1.
                    print("Ok, look what you see in the next zone: a", map1.places[i,j].place)
                    print(map1.places[i, j])
                # If the desired direction is east or e
                elif da.lower()=='e'or da.lower()=='east':
                    j+=1
                    if j==map1.positions.shape[1]:
                        j=0
                    print("Ok, look what you see in the next zone: a", map1.places[i,j].place)
                    print(map1.places[i, j])
                # If the desired direction is west or w.
                elif da.lower()=='w' or da.lower()=='west':
                    j-=1
                    if j<0:
                        j=map1.positions.shape[1]-1
                    print("Ok, look what you see in the next zone: a", map1.places[i,j].place)
                    print(map1.places[i, j])
                # If the answer was in the list but something happened
                else:
                    print("Something didn't work check your previous answer")
            # If does want to exit                           
            elif ma.lower()=='q' or ma.lower()=='quit':
                exits=input("Do you really want to quit(q) the game or just not(n) move?\t")
                # Check that he really want to exit
                if exits.lower()=='q' or exits.lower()=='quit':
                    print("\nDuring", prota.day, "days he has killed", Enemy.types, "with", Hero.hits, "hits",
                          "He has now", prota.invent, "in her pocket or bag.\n\nI hope you have enjoied")
                    input("Press any key of the keyboard to close this window.")
                    break
                elif exits.lower()=='n' or exits.lower()=='not':
                    print("You stay at the same place", map1.places[i,j].place)
                    prota.health=100
                else:
                    print("You didn't decide a reall option so I suppose you want to keep playing")
                    
            # If the doesn't want to move
            elif ma.lower()=='n' or ma.lower()=='no':
                print("You stay at the same place")
                prota.health=100
        # If the answer wast not expected
        while ma.lower() not in typic_answer:
            print("Please introduce a valid input")
            ma=input(move)
        # Starts the battle agains the dark forces...
##        if i==a.i and j==a.j:
##            print(a)
##            a.trade(prota)
        
        Battle(prota)
        prota.day+=1
        if prota.day//365==1:
            prota.day=0
            prota.age+=1

while True: 
    menu=input(Menu)
    if menu.lower()=="n" or menu.lower()=="new":
        game()
    elif menu.lower()=="l" or menu.lower()=="load":
        saved=input("Please paste here exactly the path to the file\t")
        #game.load(saved)
    elif menu.lower()=="s"  or menu.lower()=="save":
        print("Sorry this option is under development")
    elif menu.lower()=="a" or menu.lower()=="about":
        print("""
 - This game was develop in Vienna, the course 2013-2014 as a game to learn Python.
 - It was initially an exercise of the book 'Python programming for the absolute beginner' but I modified it. Now includes several other things that, I think, are fancy.
 - If the game doesn't work try putting all the files in the same folder, it shouuld work.
 - It requires Python 3.3 or higher.
 - If you have any idea or problem you can reach me by mail at : llopis <at> gmail <dot> company""")
        
    elif menu.lower()=="i" or menu.lower()=="instruction" or menu.lower()=="instructions" or menu.lower()=="instr":
        print("""Welcome, you decided to give a try or at least read the instructions of the game, so here they are: The game it tries to be self explanatory, but here you have some more help.
     - The game ask you what to do, and prints the options. Give as input the first letter or the word of the option to be accepted.
         Otherwise you can answer with a yes or not.
     - You are a man in a Middle Age map working hard. You can explore the map and get some gold, buy and sell, fight, die...
     - Take into account that you can just save and exit of the game in just some options
    """)
    elif menu.lower()=="q" or menu.lower()=="quit":
        print("I hope you enjoyed the game")
        break
    else:
        print("Now you will need to reboot the game, if you really want to play it.")
        break

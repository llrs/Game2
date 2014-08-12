#Game version 1
#  Llopis 15/01/2014
# This is some kind of MUD game, but not multiplayer and not in dungeons :D
# So this is more like an RPG: SUR Single Untested RRGP ;)

# Importing thins that must be in the same folder:
from fight import *         # Import how the fight is done
from Place import *         # Import the map, and the generator
from characters import *    # Import the characters definitions
import numpy as np
from tkinter import *

# Defining some general things
typic_answer=("yes", "y", "no", "n", "quit", "q")
typic_sentence="It is a Yes or Not question, please introduce a valid input.\nTo exit type 'quit' or 'q'"

# Function to center the window, more on the Wop project
def center(win):
    """Center the windows on the screen."""
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width =  width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    if win.attributes('-alpha') == 0:
        win.attributes('-alpha', 1.0)
    win.deiconify()

# The app of the game
class Application(Frame):
    """A GUI application for the game"""
    def __init__(self, master):
        import re
        """Initialize the Frame and create the buttons"""
        super(Application, self).__init__(master)
        self.grid()
        Label(self, text = "WELCOME TO SPM GAME"
              ).grid(row = 0, column = 1)
        Label(self, text = "(SINGLE PLAYER MAP GAME)"
              ).grid(row = 1, column = 1)
        Label(self, text = "Please choose an option:"
              ).grid(row = 2, column = 0, sticky = W)
        # Button to start a new game
        # TODO: Change the game print commands to "print" in the GUI.
        self.play_bttn = Button(self, text = "Start a new game",
                                command = self.starter)
        self.play_bttn.grid(row = 3, column =0, sticky = W,
                            columnspan = 2)
        # Button to load the saved game
        # TODO: Create the option to load from a saved game
        self.load_bttn = Button(self, text = "Load a saved game",
                                command = self.development)
        self.load_bttn.grid(row = 4, column =0, sticky = W, columnspan = 2)
        # Button to save the game
        # TODO: Create the function to save the game: maps, character, experience...
        self.save_bttn = Button(self, text = "Save the game",
                                command = self.development)
        self.save_bttn.grid(row = 5, column =0, sticky = W, columnspan = 2)
        # About buttoon
        self.about_bttn = Button(self, text = "About the game",
                                 command = self.tell_about)
        self.about_bttn.grid(row = 6, column =0, sticky = W,
                             columnspan = 2)
        # Instructions button
        self.instr_bttn = Button(self, text = "Instructions",
                                 command = self.tell_instr)
        self.instr_bttn.grid(row = 7, column =0, sticky = W,
                             columnspan = 2)
        # Output text box
        self.output_text = Text(self, width = 100, height = 20,
                                wrap = WORD)
        self.output_text.grid(row = 8, column = 0, columnspan = 5)
        self.function = 0
        

##        # Quit button
##        self.quit_bttn = Button(self, text="QUIT", fg="red", command=self.grid.quit)
##        self.quit_bttn.grid(row = 5, column = 1, sticky = W)

    # Code for whenever I will need it.
# http://effbot.org/tkinterbook/tkinter-classes.htm
##        # create body part radio buttons
##        body_parts = ["bellybutton", "big toe", "medulla oblongata"]
##        column = 1
##        for part in body_parts:
##            Radiobutton(self,
##                        text = part,
##                        variable = self.body_part,
##                        value = part
##                        ).grid(row = 5, column = column, sticky = W)
##            column += 1
##        # create electric check button
##        self.is_electric = BooleanVar()
##        Checkbutton(self,
##                    text = "electric",
##                    variable = self.is_electric
##                    ).grid(row = 4, column = 3, sticky = W)

    def tell_instr(self):
        """ Fill text box with instructions"""
        instructions = """WELCOME!
The game tries to be self explanatory, but this is the help page:\n
- You are a man in the Middle Age. Your house is on surrounded by dark creatures, defeand your house.
    You can explore the map and get some gold, buy and sell, fight, die...
    Survive! and build your empire if it is what you want!
- The game ask you what to do, and prints the options. Give as input the first letter or the word of the option to be accepted.
    Otherwise you can answer with a yes or not.\n
- Take into account that you can just save and exit of the game ocasually.
    Before starting a new adventure save! (When it will be abilable is another question)
Enjoy! """
        # display the instructions
        self.output_text.delete(0.0, END)
        self.output_text.insert(0.0, instructions)

    def tell_about(self):
        """Fill the box with some considerations about the game"""
        about = """- This game was develop in Vienna, the course 2013-2014 as a way to learn Python.\n
 - It was initially an exercise of the book 'Python programming for the absolute beginner' but I modified it. Now includes several other things that, I think, are fancy.\n
 - If the game doesn't work try saving all the files in the same folder, it should work.
    If it still doesn't work, contact me with a issue on github(llrs\game2) or with the mail\n
 - It requires Python 3.3 or higher or you can use the py2exe program to run independly in a windows system.\n
 - If you have any idea to improve the game or problem, a bug, or simply you didn't like it you can reach me by mail at : llopis <at> gmail <dot> company
    I am always glad to know that someone played with this game! """
        # display the about page
        self.output_text.delete(0.0, END)
        self.output_text.insert(0.0, about)

    def starter(self):
        """Calls the game function"""
        self.play_bttn.configure(text="Restart game")
        self.output_text.delete(0.0, END)
        history = "Our history begins far far away, when the dragons and goblins"\
                  " still dominated the Middle Earth.\nIn that time a man named...\n"
        self.output_text.insert(0.0, history)

        self.label_input = Label(self, text = "What is your name?")
        self.label_input.grid(row = 3, column = 1)
        # Input text box
        self.input_text = Entry(self)
        self.input_text.grid(row = 3, column = 2, sticky = W)
        self.input_text.bind("<Key-Return>", self.evaluate)

        # Submit button
        # TODO: Change the input so that will do something
        self.submit_bttn = Button(self, text = "Submit", command = self.evaluate)
        self.submit_bttn.grid(row = 4, column = 2, sticky = W)

    def game_name(self):
        # Doesn't need to check it can be all numbers.
        self.name = contents
        adventure = "{} started to think about conquering the world"\
                                " and free it of the nasty creatures!\nAt the "\
                                "age of...".format(self.name)
        self.label_input["text"]="When do you guess?"
        # Check if it is a valid input of age
        self.output_text.insert(END, adventure)

    def game_age(self):
        self.age = contents
        story = "Yes, at the age of {} he began to fight against terrible"\
                " creatures near their house.\nSo he got himself a wook sword"\
                " and started to travel...\nHe knew there were many terrible "\
                "creatures but he was not afraid of them...\n".format(self.age)
        self.output_text.insert(END, story)
        
    def game_set(self):

        # Creating protagonist
        self.prota=Hero(age=int(self.age), name=self.name)
        self.fight="Do you want to fight?"
        self.fight2="Do you want to fight again?"
        self.move="Do you want to move?"
        self.direction="Where do you want to move to (N,S,E,W)? "
        self.label_input["text"]= question1
        self.movement=0
        self.map1=Maping()
        self.i=self.j=(self.map1.positions.shape[1]+1)/2
        #a=Player("Manolo", i+1, j+1)

        story = "He was at his house when he decided to go out, and help other "\
                "people however he could.\nSo he decided to go outside towards.."
        self.output_text.insert(END, story)

        #A condition to keep playing
        if self.prota.health > 0:

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
##                        break
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
            # Starts the battle againts the dark forces...
    ##        if i==a.i and j==a.j:
    ##            print(a)
    ##            a.trade(prota)

            Battle(prota)
            prota.day+=1
            if prota.day//365==1:
                prota.day=0
                prota.age+=1

    def evaluate(self):
        """Display message based on input."""
        #self.funct=["self.game_name()", "self.game_age()", "self.game_continue()"]
##        print(i for i in dir(self) not in self.funct)
##        print(self.funct)
        global contents
        contents = self.input_text.get()
        if contents == '':
            message ="The value cannot be empty, please fill it with the right "\
                      "content"
            self.output_text.delete(0.0, END)
            self.output_text.insert(0.0, message)
        else:
            funct = self.__funct()
            self.input_text.delete(0, END)
            eval(funct[self.function])
            self.function += 1


    def development(self):
        """Prints alert saying it is still not working."""
        development = "This feature is still under development"
        self.output_text.delete(0.0, END)
        self.output_text.insert(0.0, development)
        
    def __funct(self): # TODO: Improve 
        """Finds the methods begining with game and prepare them for eval
[to use in the evaluate function]"""
        fns = []
        for p in dir(app):
            try:
                a = getattr(app, p)
            except:
                continue
            if hasattr(a, '__code__'):
                fns.append((a.__code__.co_firstlineno, p))
        
        fns = [x[1] for x in sorted(fns) if re.findall("game", x[1]) != []]
        fns1=[]
        for i in fns:
            fns1.append("self.{}()".format(i))
        return(fns1)
        




root = Tk()
root.title("Game 2")
root.geometry("800x500")
app = Application(root)
center(root)
root.mainloop()

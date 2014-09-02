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
    """Center the window on the screen."""
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
        self.play_bttn = Button(self, text = "Start a new game",
                                command = self.starter)
        self.play_bttn.grid(row = 3, column =0, sticky = W,
                            columnspan = 2)
        self.play_bttn.bind("<Key-Return>", lambda x: self.starter())
        self.play_bttn.focus_set()
        # Button to load the saved game
        # TODO: Create the option to load from a saved game
        self.load_bttn = Button(self, text = "Load a saved game",
                                command = self.development)
        self.load_bttn.grid(row = 4, column =0, sticky = W, columnspan = 2)
        self.load_bttn.bind("<Key-Return>", lambda x: self.development())
        # Button to save the game
        self.save_bttn = Button(self, text = "Save the game",
                                command = self.development)
        self.save_bttn.grid(row = 5, column =0, sticky = W, columnspan = 2)
        self.save_bttn.bind("<Key-Return>", lambda x: self.development())
        # About buttoon
        self.about_bttn = Button(self, text = "About the game",
                                 command = self.tell_about)
        self.about_bttn.grid(row = 6, column =0, sticky = W,
                             columnspan = 2)
        self.about_bttn.bind("<Key-Return>", lambda x: self.tell_about())
        # Instructions button
        self.instr_bttn = Button(self, text = "Instructions",
                                 command = self.tell_instr)
        self.instr_bttn.grid(row = 7, column =0, sticky = W,
                             columnspan = 2)
        self.instr_bttn.bind("<Key-Return>", lambda x: self.tell_instr())
        # Output text box
        self.output_text = Text(self, width = 100, height = 20,
                                wrap = WORD)
        self.output_text.grid(row = 8, column = 0, columnspan = 5)
        self.output_text.config(state=DISABLED)
        self.function = 0

##        # Quit button
##        self.quit_bttn = Button(self, text="QUIT", fg="red", command=self.grid.quit)
##        self.quit_bttn.grid(row = 5, column = 1, sticky = W)

    def save(self):
        # TODO: Create the function to save the game: maps, character, experience...
        """Stores the information of the map, position and the character to continue later"""
        filename = filedialog.asksaveasfilename()#save file

    def open(self):
        """Loads the information of the saved file and uses to recreate that game."""
        filename = filedialog.askopenfilename() # open file
        dirname = filedialog.askdirectory() #where path or "" if cancel 

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
        self.output_text.config(state='normal')
        self.output_text.delete(0.0, END)
        self.output_text.insert(0.0, instructions)
        self.output_text.config(state=DISABLED)

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
        self.output_text.config(state='normal')
        self.output_text.delete(0.0, END)
        self.output_text.insert(0.0, about)
        self.output_text.config(state=DISABLED)

    def starter(self):
        """First function of the game, until it gets the name of the user"""
        self.play_bttn.configure(text="Restart game")
        self.function = 0
        self.output_text.delete(0.0, END)
        history = "Our history begins far far away, when the dragons and goblins"\
                  " still dominated the Middle Earth.\nIn that time a man named...\n"
        self.output_text.configure(state='normal')
        self.output_text.insert(0.0, history)
        self.output_text.configure(state=DISABLED)

        self.label_input = Label(self, text = "What is your name?")
        self.label_input.grid(row = 3, column = 1)
        # Input text box
        self.input_text = Entry(self)
        self.input_text.grid(row = 3, column = 2, sticky = W)
        self.input_text.bind("<Key-Return>", lambda x: self.evaluate())
        self.input_text.focus_set()
        

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
        self.output_text.configure(state='normal')
        self.output_text.insert(END, adventure)
        self.output_text.configure(state=DISABLED)

    def game_age(self):
        self.age = contents
        story = "Yes, at the age of {} he began to fight against terrible"\
                " creatures near their house.\nSo he got himself a wook sword"\
                " and started to travel...\nHe knew there were many terrible "\
                "creatures but he was not afraid of them...\nHe was at his house"\
                " when he decided to go out, and help other people however he "\
                "could.\nSo he decided to go outside towards..".format(self.age)

        self.output_text.configure(state='normal')
        self.output_text.insert(END, story)
        self.output_text.configure(state=DISABLED)
        # Creating features
        # TODO: Check the arguments and ask for the new ones until is valid
        self.prota=Hero(age=int(self.age), name=self.name)
        self.map1=Maping()
        self.i=self.j=(self.map1.positions.shape[1]+1)/2
        
        self.fight="Do you want to fight?"
        self.fight2="Do you want to fight again?"
        self.movement=0
        #a=Player("Manolo", i+1, j+1)
        # Asks if he want to move
        self.input_text.grid_forget()
        self.label_input.grid_forget()
        self.direction = StringVar()
        self.direction.set(None)
        # Create buttons and asks about where do the user want to move.
        Label(self, text="Where do you want to move?").grid(row=4, column=1, sticky = E)
        self.submit_bttn.grid(row = 5, column = 1, sticky = W)
        directions = ["North", "South", "West", "East"]
        column = 2
        for direction in directions:
            Radiobutton(self,
                        text = direction,
                        variable = self.direction,
                        value = direction
                        ).grid(row = 4, column = column, sticky= W)
            column +=1

                
##    def game_set2(self):
##        pass
##        ma = contents
##        if ma.lower in typic_answer:
##            pass
##        else:
##            self.function -= 1
        
            
##        if ma.lower()=='y' or ma.lower()=='yes':
##            self.label_input["text"]= "Where do you want to move to (N,S,E,W)?"
##            self.movement+=1
            
    def game_movement(self):
        da = self.direction.get()
        print(da)
        # Check if it is a valid direction,
        # If the desired direction is nord, or n
        if da.lower()=='n'or da.lower()=='north':
            self.i+=1
            if self.i==self.map1.positions.shape[1]:
                self.i=0
                # If there is a mountain in theplace it cannot cross it
                # TODO improve this for every direction and sea/lake if in the inventory there is no boat
                # TODO set direction of fow for rivers, and just be able to cros some of them (the others are unable to cross them)
            if self.map1.places[self.i,self.j].place=="mountain" or self.map1.places[self.i,self.j].place=="high mountain":
                print("Ok, look what you see in the next zone: a", self.map1.places[self.i,self.j].place)
                print(self.map1.places[self.i, self.j])
                print("I can't cross the mountain. I should move around it.")
                self.i-=1
            else:
                print("Ok, look what you see in the next zone: a", self.map1.places[self.i,self.j].place)
                print(self.map1.places[self.i,self.j])
        # If the desired direction is south or s
        elif da.lower()=='s'or da.lower()=='south':
            self.i-=1
            if self.i<0:
                self.i=self.map1.positions.shape[1]-1.
            print("Ok, look what you see in the next zone: a", self.map1.places[self.i,self.j].place)
            print(self.map1.places[self.i,self.j])
        # If the desired direction is east or e
        elif da.lower()=='e'or da.lower()=='east':
            self.j+=1
            if self.j==self.map1.positions.shape[1]:
                self.j=0
            print("Ok, look what you see in the next zone: a", self.map1.places[self.i,self.j].place)
            print(self.map1.places[self.i,self.j])
        # If the desired direction is west or w.
        elif da.lower()=='w' or da.lower()=='west':
            self.j-=1
            if self.j<0:
                self.j=self.map1.positions.shape[1]-1
            print("Ok, look what you see in the next zone: a", self.map1.places[self.i,self.j].place)
            print(self.map1.places[self.i, self.j])
        # If the answer was in the list but something happened
        else:
            print("Something didn't work check your previous answer")
                
    def quit(self):
        # If does want to exit
        if ma.lower()=='q' or ma.lower()=='quit':
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
        """Given the entry starts the new function of the game."""
        global contents
        contents = self.input_text.get()
        try:
            if self.direction.get() == None:
                message ="The value cannot be empty, please fill it with the right "\
                         "content"
                self.output_text.config(state='normal')
                self.output_text.insert(END, message)
                self.output_text.config(state=DISABLED)
        except AttributeError:
            pass
        except:
            raise

        if contents == '' and self.direction == False:
            message ="The value cannot be empty, please fill it with the right "\
                      "content"
            self.output_text.config(state='normal')
            self.output_text.insert(END, message)
            self.output_text.config(state=DISABLED)
        else:
            funct = self.__funct()
            self.input_text.delete(0, END)
            if self.function >= len(funct):
                self.function -= 1
            eval(funct[self.function])
            self.function += 1


    def development(self):
        """Prints alert saying it is still not working."""
        development = "This feature is still under development"
        self.output_text.config(state='normal')
        self.output_text.delete(0.0, END)
        self.output_text.insert(0.0, development)
        self.output_text.config(state=DISABLED)
        
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

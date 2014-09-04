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
from tkinter.messagebox import *
import tkinter.scrolledtext as tkst

# Defining some general things
typic_answer=("yes", "y", "no", "n", "quit", "q")
typic_sentence="It is a Yes or Not question, please introduce a valid input.\nTo exit type 'quit' or 'q'"

# Function to center the window
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
##        Label(self, text = "Please choose an option:"
##              ).grid(row = 2, column = 0, sticky = W)

        # Button to start a new game
        self.play_bttn = Button(self, text = "Start a new game",
                                command = self.starter)
        self.play_bttn.grid(row = 3, column =0, sticky = "ew")
        self.play_bttn.bind("<Key-Return>", lambda x: self.starter())
        self.play_bttn.bind("<Up>", lambda x: self.instr_bttn.focus())
        self.play_bttn.bind("<Down>", lambda x: self.load_bttn.focus())
        self.play_bttn.focus_set()

        # Button to load the saved game
        # TODO: Create the option to load from a saved game
        self.load_bttn = Button(self, text = "Load a saved game",
                                command = self.open)
        self.load_bttn.grid(row = 4, column =0, sticky = "ew")
        self.load_bttn.bind("<Key-Return>", lambda x: self.development())
        self.load_bttn.bind("<Up>", lambda x: self.play_bttn.focus())
        self.load_bttn.bind("<Down>", lambda x: self.save_bttn.focus())

        # Button to save the game
        self.save_bttn = Button(self, text = "Save the game",
                                command = self.save)
        self.save_bttn.grid(row = 5, column =0, sticky = "ew")
        self.save_bttn.bind("<Key-Return>", lambda x: self.development())
        self.save_bttn.bind("<Up>", lambda x: self.load_bttn.focus())
        self.save_bttn.bind("<Down>", lambda x: self.about_bttn.focus())

        # About buttoon
        self.about_bttn = Button(self, text = "About the game",
                                 command = self.tell_about)
        self.about_bttn.grid(row = 6, column =0, sticky = "ew")
        self.about_bttn.bind("<Key-Return>", lambda x: self.tell_about())
        self.about_bttn.bind("<Up>", lambda x: self.save_bttn.focus())
        self.about_bttn.bind("<Down>", lambda x: self.instr_bttn.focus())

        # Instructions button
        self.instr_bttn = Button(self, text = "Instructions",
                                 command = self.tell_instr)
        self.instr_bttn.grid(row = 7, column =0, sticky = "ew")
        self.instr_bttn.bind("<Key-Return>", lambda x: self.tell_instr())
        self.instr_bttn.bind("<Up>", lambda x: self.about_bttn.focus())
        
##        # Quit button
##        self.quit_bttn = Button(self, text="QUIT", fg="red", command=self.grid.quit)
##        self.quit_bttn.grid(row = 5, column = 1, sticky = W)

    def save(self):
        # TODO: Create the function to save the game: maps, character, experience...
        """Stores the information of the map, position and the character to continue later"""
        filename = filedialog.asksaveasfilename()#save file
        print(filename)

    def open(self):
        """Loads the information of the saved file and uses to recreate that game."""
        filename = filedialog.askopenfilename() # open file
        print(filename)
##        dirname = filedialog.askdirectory() #where path or "" if cancel 

    def tell_instr(self):
        """ Fill text box with instructions"""
        instructions = """WELCOME!\n\n - You are a man in the """\
                       """ Middle Age, your house is on surrounded by dark """\
                       """creatures, defeand your house. You can explore """\
                       """  the map and get some gold, buy, sell, fight, and die..."""\
                       """Survive! Build your empire!\n\n - Take into account that """\
                       """you can just save and exit of the game ocasually.Before """\
                       """starting a new adventure save! \n\n ENJOY! """
        # display the instructions
        showinfo("instructions of the game", instructions)

    def tell_about(self):
        """Fill the box with some considerations about the game"""
        about = """- This game was develop in Vienna, the course 2013-2014 as a"""\
                """ way to learn Python.\n- It was initially an exercise of the book"""\
                """'Python programming for the absolute beginner' but I modified it."""\
                """Now includes several other things that, I think, are fancy.\n\n - If"""\
                """ the game doesn't work try saving all the files in the same folder, it"""\
                """should work.\n If it still doesn't work, contact me with a issue on """\
                """github(llrs\game2) or with the mail\n\n - It requires Python 3.3 or higher"""\
                """or you can use the py2exe program to run independly on a windows system.\n\n"""\
                """ - If you have any idea to improve the game or you just found a bug, or """\
                """simply you didn't like it you can reach me by mail at : llopis <at> gmail"""\
                """<dot> company. I am always glad to know that someone played with this game! """
        showinfo("About the game", about)

    def starter(self):
        """First function of the game, until it gets the name of the user"""
        self.play_bttn.configure(text="Restart game")
        self.function = 0

        # Output text box
        self.output_text = tkst.ScrolledText(self, width = 100, height = 20,
                                wrap = WORD, bd=0)
        self.output_text.grid(row = 9, column = 0, columnspan = 5, sticky="nsew")
        self.output_text.bind("<Enter>", lambda x: self.output_text.focus())
        self.output_text.bind("<Key-Return>", lambda x: self.evaluate())
        self.winfo_toplevel().geometry("") # Resize the window
        center(root) # Recenter the window, creates a strange effect ont the screen
        
        history = "Our history begins far far away, when the dragons and goblins"\
                  " still dominated the Middle Earth.\nIn that time a man named...\n"
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

        # TODO: Delete the buttons and the submit button when Reset is pressed.
        
##        if self.play_bttn['text']=="Restart game":
##            Button.state(['disabled'])

    def game_name(self):
        
        # Function to check if there are numbers on it
        def contains_digits(d):
            digits = re.compile('\d')
            return bool(digits.search(d))
        # If there is any number don't accept the name
        if contains_digits(contents):
            self.function -= 1
            showwarning("Alert!", "Please introduce a real name.")
            self.input_text.focus()
        else:
            self.name = contents
            adventure = "{} started to think about conquering the world and free"\
                        " it of the nasty creatures!\nAt the age of...".format(
                            self.name)

            self.label_input["text"]="When do you guess?"
            self.output_text.configure(state='normal')
            self.output_text.insert(END, adventure)
            self.output_text.configure(state=DISABLED)

    def game_age(self):
        """Check the age and start the direction buttons"""
        try:
            self.age = int(contents)
        except ValueError:
            self.function -= 1
            showwarning("Error", "Please introduce a number")
            self.input_text.focus()
        else:
            self.output_text.configure(state='normal')
            story = "Yes, at the age of {} he began to fight against terrible"\
                    " creatures near their house.\nSo he got himself a wook sword"\
                    " and started to travel...\nHe knew there were many terrible "\
                    "creatures but he was not afraid of them...\nHe was at his house"\
                    " when he decided to go out, and help other people however he "\
                    "could.\nSo he decided to go outside towards..\n".format(
                        self.age)
            self.output_text.insert(END, story)
            self.output_text.configure(state=DISABLED)
            # Creating features
            self.prota=Hero(self.name, self.age)
            self.map1=Maping()
            self.i=self.j=(self.map1.positions.shape[1]+1)/2
            
        ##        self.fight="Do you want to fight?"
        ##        self.fight2="Do you want to fight again?"
            
            # Asks if he want to move
            self.input_text.grid_forget()
            self.label_input.grid_forget()
            self.direction = StringVar()
            self.direction.set(None)
            # Create buttons and asks about where do the user want to move.
            Label(self, text="Where do you want to move?").grid(
                row=3, column=1, sticky = W)
            self.submit_bttn.grid(row = 5, column = 1, sticky = W)
            self.movement=0
            directions = ["North", "South", "West", "East", "Stay"]
            column = 1
            for direction in directions:
                Radiobutton(self,
                            text = direction,
                            variable = self.direction,
                            value = direction
                            ).grid(row = 4, column = column, sticky= "ns")
                column +=1
            self.winfo_toplevel().geometry("") # Resize the window
    def game_movement(self):
        da = self.direction.get()

        # Change the position
        if da.lower()=='north':
            self.i+=1
        elif da.lower()=="south":
            self.i-=1
        elif da.lower()=="east":
            self.j+=1
        elif da.lower()=="west":
            self.j-=1
        elif da.lower()==None:
            showwarning("Caution!", "You didn't choose an option I supose you stayied where"\
                        " you were")
        else: # The user decided to stay
             self.prota.health=100

        # If it has reached the end of the map start over:
        if self.i == self.map1.positions.shape[1]:
            self.i = 0
        elif self.i <0:
            self.i = self.map1.positions.shape[1]-1
        elif self.j == self.map1.positions.shape[1]:
            self.j = 0
        elif self.j < 0:
            self.j = self.map1.positions.shape[1]-1

        # TODO improve this for every direction and sea/lake if in the inventory there is no boat
        # TODO set direction of fow for rivers, and just be able to cross some of them (the others are unable to cross them)

        # If the new position is a high mountain then show you can't move further.
        if self.map1.places[self.i,self.j].place in ["mountain", "high mountain"]:
            stop = "OH, a {} blocks my way. I should move around it.\n".format(
                self.map1.places[self.i,self.j].place)
            self.output_text.config(state='normal')
            self.output_text.insert(END, stop)
            self.output_text.config(state=DISABLED)
            
            # Restoring the position 
            if da.lower()=='north':
                self.i-=1
            elif da.lower()=="south":
                self.i+=1
            elif da.lower()=="east":
                self.j-=1
            elif da.lower()=="west":
                self.j+=1
        else:
            desc = "Ok, look what you see in the next zone: a {}\n".format(
                self.map1.places[self.i,self.j].place)
            desc2 = str(self.map1.places[self.i,self.j])+"\n"
            self.output_text.config(state='normal')
            self.output_text.insert(END, desc)
            self.output_text.insert(END,desc2)
            self.output_text.config(state=DISABLED)
        self.output_text.see(END)

            # Starts the battle againts the dark forces...
##        Battle(self.prota)
##            a=Player("Manolo", i+1, j+1)
##            if i==a.i and j==a.j:
##                print(a)
##                a.trade(prota)

        self.prota.day+=1
        if self.prota.day//365==1:
            self.prota.day=0
            self.prota.age+=1        
                
    def quit(self):
        """A summary of what have been done """
        if askyesno('Verify', 'Do you really want to quit?'):
            pass
##            print("\nDuring", self.prota.day, "days he has killed", Enemy.types, "with", Hero.hits, "hits",
##                "He has now", self.prota.invent, "in her pocket or bag.\n\nI hope you have enjoied")
        else:
            pass # Keep playing
##            print("You didn't decide a real option so I suppose you want to keep playing")

    def evaluate(self):
        """Given the entry starts the new function of the game."""
        global contents
        contents = self.input_text.get()
##        button.state(['disabled'])            ;# set the disabled flag, disabling the button
##        button.state(['!disabled'])           ;# clear the disabled flag
##        button.instate(['disabled'])          ;# return true if the button is disabled, else false
##        button.instate(['!disabled'])         ;# return true if the button is not disabled, else false
##        button.instate(['!disabled'], cmd)    ;# execute 'cmd' if the button is not disabled
        try:
            self.direction.get()
        except AttributeError:
            pass
        else:
            contents = self.direction.get() # The content is now with something
        
        if contents == '':
            message ="The value cannot be empty, please fill it with the right "\
                        "content"
            showwarning("Please fill the required elements", message)
            self.input_text.focus()
        else:
            funct = self.__funct()
            self.input_text.delete(0, END)
            if self.function >= len(funct):
                self.function -= 1
            eval(funct[self.function])
            self.function += 1


    def development(self):
        """Prints alert saying it is still not working."""
        showwarning("Sorry", "This feature is still under development")
        
    def __funct(self): # TODO: Improve it
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
    
##    def _mouse_wheel(event):
##        """A function to handle the mouse wheel rolling to bind with the
##scroll bar"""
##        # respond to Linux or Windows wheel event
##        if event.num == 5 or event.delta == -120:
##            count -= 1
##        if event.num == 4 or event.delta == 120:
##            count += 1
##        return(-1*(count/120))
        
root = Tk()
root.title("Game 2")
##root.geometry("800x500")
app = Application(root)
center(root)
root.mainloop()

#! Python

import tkinter.scrolledtext as tkst

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
    
class CustomText(tkst.ScrolledText):
    '''A text widget with a new method, HighlightPattern 

    example:

    text = CustomText()
    text.HighlightPattern("this should be red", "red")

    The highlight_pattern method is a simplified python 
    version of the tcl code at http://wiki.tcl.tk/3246
    '''
    def __init__(self, *args, **kwargs):
        import tkinter as tk
        tk.Text.__init__(self, *args, **kwargs)

    def highlight(self, text, patterns, color, start="1.0", end="end", regexp=False):
        '''Apply the given tag to all text that matches the given pattern

        If 'regexp' is set to True, pattern will be treated as a regular expression
        '''
        import tkinter as tk
        self.tag_config(color, foreground = color)
        start = self.index(start)
        end = self.index(end)
        self.mark_set("matchStart",start)
        self.mark_set("matchEnd",start)
        self.mark_set("searchLimit", end)
        self.configure(state='normal')
        self.insert("end", text)
        
        if isinstance(patterns, list) or isinstance(patterns, tuple):
            for pattern in patterns:
                count = tk.IntVar()
                while True:
                    index = self.search(pattern, "matchEnd","searchLimit",
                                        count=count, regexp=regexp)
                    if index == "": break
                    self.mark_set("matchStart", index)
                    self.mark_set("matchEnd", "%s+%sc" % (index,count.get()))
                    self.tag_add(color, "matchStart","matchEnd")
                self.configure(state="disabled")
        else:
            count = tk.IntVar()
            while True:
                index = self.search(patterns, "matchEnd","searchLimit",
                                    count=count, regexp=regexp)
                if index == "": break
                self.mark_set("matchStart", index)
                self.mark_set("matchEnd", "%s+%sc" % (index,count.get()))
                self.tag_add(color, "matchStart","matchEnd")
            self.configure(state="disabled")
            self.see("end")
def weighted_choice(choices):
    """Get a list of nested list
    Where the second one is the probability and the first value of the lested list is the output"""

    total = sum(w for c, w in choices)
    r = random.uniform(0, total)
    upto = 0
    for c, w in choices:
        if upto + w > r:
            return c
        upto += w
    assert False, "Shouldn't get here"

def choice_weighted(choices, weights):
    """From al list of choices of weights `weights` selects one according to weights"""
    import random
    total=sum(weights)
    r=random.uniform(0, total)
    upto=0
    for w in weights and c in choices:
        if upto+w>r:
            return c
        upto+=w
    assert False, "Shouldn't get here"

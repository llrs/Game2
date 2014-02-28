import numpy as np
class Place(object):
    """Where is the action"""
    possible_places=("mountain", "countryside", "river")
    def __init__(self, place=""):
        """Prove2"""
        import random
        if place=="":
            self.place=random.choice(Place.possible_places)
        elif place in Place.possible_places:
            self.place=place
        else:
            print("Please introduce a valid place!")
        
    def __str__(self):
        #Defining cave
        if self.place=="mountain":
            return "Affortunatly you found a cave were you can stay dry from the heavy rain it is falling"
        elif self.place=="countryside":
            return "How nice is the life!! The sun shining..."
        elif self.place=="river":
            return "The river flows and flow..."
             
             
positions=np.eye(3, dtype=object)
place=np.eye(3, dtype='<U30')
for i in range(3):
    for j in range(3):
        positions[i,j]=Place()
        place[i,j]=Place().place

i=0
j=0
while True:
    print(positions[i,j])
    answer=input("Do you want to move north?\t")
    if answer.lower()=="y" or answer.lower()=="yes":
        i+=1
        if i>=3:
            i=0
    elif answer.lower()=="q" or answer.lower()=="quit":
        break
    

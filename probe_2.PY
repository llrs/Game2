#Creating a battle between our hero and other creatures with OOP
# Llopis 02/01/2014
#Deffining uselful classes
#This is some kind of MUD game, but not multixlayer
#To do implement class place (and correct class hero)
#ADD to hero: Movement, and image       #Modify inventory
#ADD to enemy: Movement
#ADD to place: Images, boarders, night, scenario, events, fight
#ADD to map:

inovation=True

#Random things
def truncate(x):
    bdot, adot = str(x).split('.')
    return float('.'.join((bdot, adot[:2])))

#Clas Hero for the protagonist
class Hero(object):
    """Our hero"""
    hits=0
    def __init__(self, name="Llopis", age=21, shield=10, health=100, enemy="You"):
        #Checking if the inputs are ok
        #Checking the name
        if name=="":
            print("Please introduce a valid name.")
        elif name.isdigit()==True:#Check if it doesn't have numbers inside
            print("Please introduce a valid name.")
        else:
            self.__name=name
            
        #Checking the age        
        if age<=0:
            print("Please introduce a valid age.")
        elif age<1:
            print("H: With 0 years old I begin to walk around!")
        elif age>1 and age<5:
            print("-That's starting from the very young age!")
        elif age>100:
            print("Please I think that you don't begin to fight with more than 100 years unless you are an elf.\n",
                  "Are you really an elf??\nYour age is corrected to 100")
            self.age=100
        else:
            self.age=age
            
        self.damage=-self.age*(self.age-100)/25
                
        #Checking the health
        if health<0:
            self.health=0
            print("Health is turned to 0, you want to start alive or not?")
        elif health>150:
            self.health=100
            print("You are a hero, but not a Greek goddness!\n"\
                  "Maximum health is now 100")
        else:
            self.health=health
            
        #Checking shield
        if shield<0:
            print("Please introduce a valid shield.")
        else:
            self.__shield=shield
        
        #Other attributes
        if enemy!="":
            self.__enemy=enemy
        else:
            print("Please introduce a valid enemy")
        
        
        #This attributes are independent from the initializing.
        self.kills=0
        self.hits=0
        self.invent={}
        self.day=1
        
    #Defining how to modify the enemy
    @property
    def enemy(self):
        return self.__stacenemy
    @enemy.setter
    def enemy(self, new_enemy):
        if new_enemy=="":
            print("H: I don't hate nor love.")
        else:
            self.enemy = new_enemy
            print("Enemy changed successfully! Now it is", self.enemy)
    
    #Defining how to modify the name
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, new_name): #Method
        if new_name=="":
            print("Ehh I should have a name.")
        elif  name.isdigit()==True:#Check if it has numbers.
            print("Please introduce a valid name.")
        else:
            self.__name = new_name
            print("Name changed successfully!")

    #Defining other methods
    def __str__(self):
        return("the hero "+self.__name+"!") #Used somewhere, check how it works
    def talk(self):
        print("H: I am ready for the battle")
    def attack(self, enemy, damage):
        damage*=(1+Hero.hits)/self.day
        Hero.hits+=1
        if self.hits==0:
            print(self.__name, "attacks our enemy", enemy.creature,
                  ". Producing", truncate(damage), "points of damage")
            self.hits+=1
        else:
            print(self.__name, "attacks again with", truncate(damage),"points")
            self.hits+=1
        enemy.damaged(damage)
        if enemy.life==0:
            self.kills+=1
            self.hits=0

    #Defining what happens when hitted
    def damaged(self, damage):
        if self.__shield>0:
            damage-=self.__shield
        if 'iron shield' in self.invent:
            damage-=20
        elif 'shield' in self.invent:
            damage-=10
        self.health-=damage
        if self.health<=0:
            self.health=0
            print("H: I failed to become the conqueror of the world...")
        elif self.health<15:
            print("H: Oh, no! I must protect myself. I am now just", self.health, "points of life.")
        else:
            print("H: HA! You almost miss this one.")

    
    def inventory(self, name, quantity):
        if quantity>0:
            print("You found", quantity, name)
            a=input("Do you want to add it to the inventory?\t")
            if name not in self.invent:
                if a.lower()=='y' or a.lower()=='yes':
                    self.invent[name]= quantity
                else:
                    print("Ok, do whatever you want...")
            else:
                self.invent[name]+=quantity
            print("Now your inventory is", self.invent)
        else:
            a=input("Do you want give it away?\t")
            if name not in self.invent:
                if a.lower()=='y' or a.lower()=='yes':
                    self.invent[name]= quantity
                else:
                    print("Ok, do whatever you want...")
            else:
                self.invent[name]+=quantity
            print("Now your inventory is", self.invent)
            
#Defining enemy type
class Enemy(object):
    """Enemy!!"""
    total=0
    types_total=0
    types={}

    #Define the initial Enemy
    def __init__(self, creature="Troll", damage=30, defense=0, life=100, enemy="Hero"):
        #Checking the types
        if creature=="":
            print("Please introduce a valid name.")
        elif creature.isdigit()==True: #Check if it doesn't have numbers inside
            print("Please introduce a valid name.")
        else:
            self.creature=creature
            if creature not in Enemy.types:
                Enemy.types[creature]=1
            else:
                Enemy.types[creature]+=1
            Enemy.types_total=len(Enemy.types)
                
        #Checking the life
        if life<0:
            self.life=0
        else:
            self.life=life
            
        #Checking defense
        if defense<0:
            print("Please introduce a valid defense.")
        else:
            self.__defense = defense
            
        #Checking the enemy
        if enemy=="":
            print("Please introduce a valid enemy.")
        elif enemy.isdigit()==True: #Check if it doesn't have numbers inside
            print("Please introduce a valid enemy.")
        else:
            self.enemy=enemy
            
        self.damage=damage
        self.hits=0
        Enemy.total+=1

    #Defining other methods
    def __str__(self):
        return("A ancient and unbelivable creature")

    #Defining when it attacks
    def attack(self, enemy, damage):
        if damage==None or damage==0:
            print("Pleas if you want to attack, do it!")
        else:
            self.damage=damage
            self.enemy=enemy
        self.hits+=1
        if self.hits==1:
            if (Enemy.total+1)%3!=0:
                print(self.creature, "attacks back", self.enemy, "Producing", self.damage, "points of damage")
            else:
                print(self.creature, "attacks again!")
        else:
            print("E: GRHHH")
        self.enemy.damaged(self.damage)

    #Defining when it is hit
    def damaged(self, damage):
        if self.__defense>0:
            damage-=self.__defense
        self.life-=damage
        if self.life<=0:
            print("E: AHHH, a miserable human has killed me!")
            self.life=0
        else:
            print("E: I've enoughg life to kill you stpuid.")
            
#Defining where it takes action the game outside rooms...
class Place(object):
    """Where is the action"""
    possible_places=("cave","abandoned house", "castle", "river", "forest", "house", 
                    "mountain", "high mountain", "jungle", "desert", "sea", "lake", "town", "city", "countryside")
    possible_weather=("rainy", "sunny", "cloudy", "stormy", "windy", "light")    
    def __init__(self, place="", weather=""):
        """Prove2"""
        import random
        if place=="":
            self.place=random.choice(Place.possible_places)
        elif place in Place.possible_places:
            self.place=place
        else:
            print("Please introduce a valid place!")

        if weather=="":
            self.weather=random.choice(Place.possible_weather)
        elif weather in Place.possible_weather:
            self.weather=weather
        else:
            print("Please introduce a valid weather!")
        
    def __str__(self):
        #Defining cave
        if self.place=="cave" and self.weather=="rainy":
            return "Affortunatly you found a cave were you can stay dry from the heavy rain it is falling"
        elif self.place=="cave" and self.weather=="sunny":
            return "It is very sunny... better wait until more colder hours under these rocks, maybe I can find water."
        elif self.place=="cave" and self.weather=="cloudy":
            return "It is a little dark but I still can see a place to camp\nI hope the cave is not deep"
        elif self.place=="cave" and self.weather=="stormy":
            return "I should protect from the coming storm, I should find a town, a house or something...\nLook a cave!!"
        elif self.place=="cave" and self.weather=="windy":
            return "I have a bad feeling...\nThis wind... and this noise...\nOh! it was just the wind and the rocks of this cave entrance."
        elif self.place=="cave" and self.weather=="light":
            return "Oh! Look a nice cave."

        #Defining abandoned house
        elif self.place=="abandoned house" and self.weather=="rainy":
            return "Oh, look a house, at least I will be around a fire in this rainy night"
        elif self.place=="abandoned house" and self.weather=="sunny":
            return "That house seems to be abandoned many years before Morgoroth left the Middle Earth"
        elif self.place=="abandoned house" and self.weather=="cloudy":
            return "I don't see anything in 5 steps!\nKNOCK\nOh, it is a door of a house and I haven't seen it until now..."
        elif self.place=="abandoned house" and self.weather=="stormy":
            return "Better I not guard in this house, who knows if something will hit me there."
        elif self.place=="abandoned house" and self.weather=="windy":
            return "Oh, this was once a nice house, but now the nature has recovered it"
        elif self.place=="abandoned house" and self.weather=="light":
            return "I am getting near to a town here is an old farm"
        
        #Defining castle
        elif self.place=="castle" and self.weather=="rainy":
            return "At least! That will defend from the creatures outside.."
        elif self.place=="castle" and self.weather=="sunny":
            return "I should go to this land lord's castle to ask for some food"
        elif self.place=="castle" and self.weather=="cloudy":
            return "The castle should be somewhere around here, maybe it is up that hill, and I haven't seen it"
        elif self.place=="castle" and self.weather=="stormy":
            return "At least here I will be safe from the storm, and maybe I will find some diversion at the castle's tavern"
        elif self.place=="castle" and self.weather=="windy":
            return "Even with this wind the castle catapults could hit a tree at 500 foots"
        elif self.place=="castle" and self.weather=="light":
            return "I don't know what is better to stop and lose a day in the castle or continue on"

        #Defining river
        elif self.place=="river" and self.weather=="rainy":
            return "I should try to cross now or later I will not"
        elif self.place=="river" and self.weather=="sunny":
            return "Maybe I can fish something in the river"
        elif self.place=="river" and self.weather=="cloudy":
            return "ARGH! all this clouds and now the fog of the river nearby..."
        elif self.place=="river" and self.weather=="stormy":
            return "I should find a bridge to cross the river and quickly before it falls"
        elif self.place=="river" and self.weather=="windy":
            return "With such a big waves I cannot cross this river swimming..."
        elif self.place=="river" and self.weather=="light":
            return "Look a river over there, I wonder were it comes from..."

        #Defining forest
        elif self.place=="forest" and self.weather=="rainy":
            return "It can be difficult to cross the forest with such a rain"
        elif self.place=="forest" and self.weather=="sunny":
            return "What a nice forest to walk by"
        elif self.place=="forest" and self.weather=="cloudy":
            return "This tree doesn't let me see the forest... and it is so dark either..."
        elif self.place=="forest" and self.weather=="stormy":
            return "Under the forest with a storm it is not the best place to be."
        elif self.place=="forest" and self.weather=="windy":
            return "I should take care ahead and about the top. I hope no branch hit me"
        elif self.place=="forest" and self.weather=="light":
            return "A dark and ancient forest..."

        #Defining mountain
        elif self.place=="mountain" and self.weather=="rainy":
            return "It is impossible to cross the mountain with such a rain"
        elif self.place=="mountain" and self.weather=="sunny":
            return "It would be nice to look around from the top, it is a shame I cannot climb so hight"
        elif self.place=="mountain" and self.weather=="cloudy":
            return "I don't want to be on the top of the mountain wich such a dark cloud."
        elif self.place=="mountain" and self.weather=="stormy":
            return "I hope no rock fall from the mountain... just in case I will not go there"
        elif self.place=="mountain" and self.weather=="windy":
            return "It is a bit cold with such a wind I do not want to be up in the mountain with sucha a wind"
        elif self.place=="mountain" and self.weather=="light":
            return "This is a perfect landscape to look at mountain and start to paint a picture of it"

        #Defining high mountain
        elif self.place=="high mountain" and self.weather=="rainy":
            return "It is impossible to cross this sheer mountain with such a rain"
        elif self.place=="high mountain" and self.weather=="sunny":
            return "It would be nice to look azound from the top, it is a shame I cannot climb this sheer."
        elif self.place=="high mountain" and self.weather=="cloudy":
            return "I do not want to be on the top of the mountain wich such a dark cloud."
        elif self.place=="high mountain" and self.weather=="stormy":
            return "I hope no rock fall from the mountain's sheer... just in case I will not go there."
        elif self.place=="high mountain" and self.weather=="windy":
            return "It is a bit cold with such a wind I do not want to be up the sheer of the the mountain."
        elif self.place=="high mountain" and self.weather=="light":
            return "Look! A goat, just it can climb such a wonderful sheer."

        #Defining jungle
        elif self.place=="jungle" and self.weather=="rainy":
            return "Thanks God, this jungle is so tupid the rain doesn't reach the floor!"
        elif self.place=="jungle" and self.weather=="sunny":
            return "Is it here always the same dark? Outside the jungle it is extremly sunny"
        elif self.place=="jungle" and self.weather=="cloudy":
            return "Now is when some species come out and other leave the jungle...so there is the doble of them right now."
        elif self.place=="jungle" and self.weather=="stormy":
            return "And I thought that in the jungle while and storm would be quite..."
        elif self.place=="jungle" and self.weather=="windy":
            return "Here the wind seems to slow with all this enormus trees and vegetation."
        elif self.place=="jungle" and self.weather=="light":
            return "This seems a Minecraft jungle, all light and trees, but here there are much more animals."

        #Defining desert
        elif self.place=="desert" and self.weather=="rainy":
            return "Who would say that I would live long enough to see raining like this in a desert!"
        elif self.place=="desert" and self.weather=="sunny":
            return "Oh, no and the next oasis is 5k feets away...\nAnd it i{ so hot and sunny here...\nI need water...\nWater?\nWtr?..."
        elif self.place=="desert" and self.weather=="cloudy":
            return "Yes, jor just a damn minute there isn't this horrible hot here, but there is still(the sand and the rocks..."
        elif self.place=="desert" and self.weather=="stormy":
            return "NOOO! Now a sand stozm!, better I find quickly a good pleace to protect myself."
        elif self.place=="desert" and self.weather=="windy":
            return "I hope it gets better, I can't see anything with this wind."
        elif self.place=="desert" and self.weather=="light":
            return "At least some water, just a little bit more...\nS***! Another mirage!"
        
        #Defining sea
        elif self.place=="sea" and self.weather=="rainy":
            return "Who would say that I would live long enough to see raining like this in a desert!"
        elif self.place=="sea" and self.weather=="sunny":
            return "Oh, no and the next oasis is 5k feets away...\nAnd it is so hot and sunny here...\nI need water...\nWater?\nWtr?..."
        elif self.place=="sea" and self.weather=="cloudy":
            return "This clouds don't mean anything good..."
        elif self.place=="sea" and self.weather=="stormy":
            return "I would not cross this sea with a little boat, and even with a big one would it be difficult."
        elif self.place=="sea" and self.weather=="windy":
            return "I think it comes a storm, I would not risk to sail"
        elif self.place=="sea" and self.weather=="light":
            return "I would like to swim in that sea... or lie on the sand and listen to the waves..."
       
        #Defining lake
        elif self.place=="lake" and self.weather=="rainy":
            return "It must have some exit this lake or in a few moment this land will be underwater."
        elif self.place=="lake" and self.weather=="sunny":
            return "Definetly this is a good place to have a house nearby."
        elif self.place=="lake" and self.weather=="cloudy":
            return "Is that out there the other side of the lake or it is just the fog?"
        elif self.place=="lake" and self.weather=="stormy":
            return "Thanks God it is not so big or the waves would have taken me. I should move away from the lake."
        elif self.place=="lake" and self.weather=="windy":
            return "I should make a boat, with this wind it would be perfect to travel faster."
        elif self.place=="lake" and self.weather=="light":
            return "I don't know if this is a lake or it is a sea, it is so big!"

        #Defining town
        elif self.place=="town" and self.weather=="rainy":
            return "Thanks good I found a town to recover from this rainny day"
        elif self.place=="town" and self.weather=="sunny":
            return "What a lovely town"
        elif self.place=="town" and self.weather=="cloudy":
            return "This town looks tetric"
        elif self.place=="town" and self.weather=="stormy":
            return "I hope the roof holds on a littel bit more"
        elif self.place=="town" and self.weather=="windy":
            return "I hope to find some place to sleep this night in this nice town"
        elif self.place=="town" and self.weather=="light":
            return "Is this a town?"

        #Defining city
        elif self.place=="city" and self.weather=="rainy":
            return "I hate the citys on rainy days, the carriages always end up splashing me."
        elif self.place=="city" and self.weather=="sunny":
            return "How could they build such a high building?"
        elif self.place=="city" and self.weather=="cloudy":
            return "Where were the city's wall door? I can't find them"
        elif self.place=="city" and self.weather=="stormy":
            return "Below this house I will wait until the storm is over."
        elif self.place=="city" and self.weather=="windy":
            return "Another time with such a potent wind, it is terrible to cross the street"
        elif self.place=="city" and self.weather=="light":
            return "I would love to visit each tabern of the city."
        
        #Defining house
        elif self.place=="house" and self.weather=="rainy":
            return "Thanks God I am at house"
        elif self.place=="house" and self.weather=="sunny":
            return "Why I am inside my house instead of in the garten??"
        elif self.place=="house" and self.weather=="cloudy":
            return "What a wonderful day to stay at home and read a good book like The mysterious Island"
        elif self.place=="house" and self.weather=="stormy":
            return "Uff, I reparied the roof the last week"
        elif self.place=="house" and self.weather=="windy":
            return "I should see where it comes this wind. I don't wont to get cold inside my own house"
        elif self.place=="house" and self.weather=="light":
            return "It is a good day to start a journay"
        
        
        #Defining countryside
        elif self.place=="countryside" and self.weather=="rainy":
            return "This rain is perfect to grow here wheat"
        elif self.place=="countryside" and self.weather=="sunny":
            return "They will soon collect all the wheat"
        elif self.place=="house" and self.weather=="cloudy":
            return "Look this nice mud, between the wheat"
        elif self.place=="countryside" and self.weather=="stormy":
            return "I hope this will not raze the field"
        elif self.place=="countryside" and self.weather=="windy":
            return "Wow, my hat, if I lost it now I will never recover it."
        elif self.place=="countryside" and self.weather=="light":
            return "How nice would be to rest here for a while"
        else:
            return "It seems I forgot to print for", self.place, "and", self.weather

#Defines the map where it takes places the action
class Maping(object):
    """The world of the game"""
    
    def __init__(self, large=4):
        #it implies a minimum of 3
        import numpy as np
        while large<4:
            print("Please introduce a valid number greater than 3.")
            try:
                large=int(input("How wide and large should the map be?\t"))
            except ValueError:
                print("Please introduce a natural number: 4,5,6,7...")
                large=int(input("How wide and large should the map be?\t"))
                
        self.large=2*large+1
        self.middle=large+1
        self.places=np.eye(self.large, dtype=object)
        self.positions=np.eye(self.large, dtype='<U20')
        self.count={} #I will store how many are of each type
        
            #Defines acceptable rules for the map creation
        self.options=(Place("cave"),                 #1
                      Place("abandoned house"),      #2
                      Place("castle"),               #3
                      Place("river"),                #4
                      Place("forest"),               #5
                      Place("house"),                #6
                      Place("mountain"),             #7
                      Place("high mountain"),        #8
                      Place("jungle"),               #9
                      Place("desert"),               #10
                      Place("sea"),                  #11
                      Place("lake"),                 #12
                      Place("town"),                 #13
                      Place("city"),                 #14
                      Place("countryside"))          #15
        #Check pygames and gamesdev. It doesn't seem to work well 
        self.places=np.array([[Place() for i in range(self.large)] for j in range(self.large)], dtype=object)
        
        #Situates the house in the middle of the map and a cave at the south
        #Place a city and a town surrounded in one corner by mountains and high mountains respecitvly
        #Place a river that flows from the town (high mountains to a lake near the city)
        self.places[self.middle,self.middle].place="house"
        self.places[self.middle,self.middle+1].place="cave"
        self.places[self.middle/2,self.middle/2].place="town"
        self.places[self.middle/2-1,self.middle/2].place="high mountain"
        self.places[self.middle/2,self.middle/2-1].place="high mountain"
        self.places[self.middle/2-1,self.middle/2-1].place="high mountain"
        #Further development place a river from the high mountains in near the town  until the city
        self.places[self.middle/2+1,self.middle/2].place="river"
        self.places[self.middle*3/2,self.middle*3/2].place="city"
        self.places[self.middle*3/2+1,self.middle*3/2].place="mountain"
        self.places[self.middle*3/2,self.middle*3/2+1].place="mountain"
        self.places[self.middle*3/2+1,self.middle*3/2+1].place="mountain"
        self.places[self.middle*3/2-1, self.middle*3/2].place="lake"
        
        for i in range(self.large):
            for j in range(self.large):
                self.positions[i,j]=self.places[i,j].place
                if self.places[i,j].place not in self.count:
                    self.count[self.places[i,j].place]=1
                else:
                    self.count[self.places[i,j].place]+=1

#def weighted_choice(choices):
#    """Get a list of nested list
#    Where the second one is the probability and the first value of the lested list is the output"""
#    
#    total = sum(w for c, w in choices)
#    r = random.uniform(0, total)
#    upto = 0
#    for c, w in choices:
#        if upto + w > r:
#            return c
#        upto += w
#    assert False, "Shouldn't get here"

#def choice_weighted(choices, weights):
#    """From al list of choices of weights `weights` selects one according to weights"""
#    import random
#    total=sum(weights)
#    r=random.uniform(0, total)
#    upto=0
#    for w in weights and c in choices:
#        if upto+w>r:
#            return c
#        upto+=w
#    assert False, "Shouldn't get here"

# ADD to hero: Movement, and image       #Modify inventory
# ADD to enemy: Movement
# ADD other players

# Random things
def truncate(x):
    bdot, adot = str(x).split('.')
    return float('.'.join((bdot, adot[:2])))

# Clas Hero for the protagonist
class Hero(object):
    """Our hero, protagonist of the game"""
    hits=0
    def __init__(self, name="Llopis", age=21, shield=0, health=100, enemy="You"):
        """Initialice the object with name, age, shield, health, and enemy,
with the age calculates the damage he can do."""
        # Checking if the inputs are ok
        # Checking the name
        if name=="":
            print("Please introduce a valid name.")
        elif name.isdigit()==True:# Check if it doesn't have numbers inside
            print("Please introduce a valid name.")
        else:
            self.__name=name
            
        # Checking the age        
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
                
        # Checking the health
        if health<0:
            self.health=0
            print("Health is turned to 0, you want to start alive or not?")
        elif health>150:
            self.health=100
            print("You are a hero, but not a Greek goddness!\n"\
                  "Maximum health is now 100")
        else:
            self.health=health
            
        # Checking shield
        if shield<0:
            print("Please introduce a valid shield.")
        else:
            self.__shield=shield
        
        # Other attributes
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
        """Redefeining the enemy"""
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
        """Redefeining his name"""
        return self.__name
    @name.setter
    def name(self, new_name): #Method
        if new_name=="":
            print("Ehh I should have a name.")
        elif new_name.isdigit()==True:# Check if it has numbers.
            print("Please introduce a valid name.")
        else:
            self.__name = new_name
            print("Name changed successfully!")

    # returns who he is
    def __str__(self):
        """Explains a little about herself"""
        return("the hero "+self.__name+"!") #Used somewhere, check how it works
    # Prints I am ready for the battle
    def talk(self):
        """Some sentences"""
        print("H: I am ready for the battle")
    # Attack a enemy with damage
    def attack(self, enemy, damage):
        """Given an enemy attacks her with damage or a formula depending on the hero properties """
        damage*=((self.hits+1)/(self.day+1)+(1+self.hits)/(Hero.hits+1)+Hero.hits/100+Hero.hits/(self.day+self.hits+1)+(1+self.kills)/(1+Hero.hits))/3
        #This works fine stabilized about 80 damage*=((self.hits+1)/(self.day+1)+(1+self.hits)/(Hero.hits+1)+Hero.hits/100+Hero.hits/(self.day+self.hits+1))/3
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
        """Recieve the damage, if there is defense or shield he receives less damage."""
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

    
    def inventory(self, name, quantity, pr=True):
        """If object was not there is added, if it was it is added, or if the quantity is lesser than 0 then it removes this quantity."""
        if pr==True:
            if quantity>0:
                print("You found", quantity, name)
                a=input("Do you want to add it to the inventory?\t")
            elif quantity<0:
                a=input("Do you want give it away?\t")
            else:
                print("Sorry you can't add 0 item")
                
            if a.lower()=='y' or a.lower()=='yes':
                if name not in self.invent:
                    self.invent[name]= quantity
                else:
                    self.invent[name]+=quantity
            else:
                print("You canceled the action")
            print("Now your inventory is", self.invent)
        elif pr==False:
            if name not in self.invent:
                self.invent[name]= quantity
            else:
                self.invent[name]+=quantity
        elif pr!=True or pr!=False:
            print("The parameter pr should be True or False")
            
    def trade(self):
        """Let you decide which prices do you sell the objects of the intentary"""
        self.sell={}
        print("You have this inventary:\n", self.invent)
        print("If you set the price to 0, you give it gratis, if you set it to any value which is not a number it will not be sold.")
        for item in self.invent:
            print("At which price do you want to sell ", item+"s", "?", sep='', end='\t')
            try:
                a=float(input())
                self.sell[item]=a
            except ValueError:
                pass
            except:
                print("You didn't set a price or say anything not to sell it. I didn't understand what do you want...")
        print("You sell the the following elements at this price:\n", self.sell)
            
        
            
        

# Defining a neutral AI
class Player(Hero):
    """A neutral player"""
    def __init__(self, name, age, shield, health, i, j):
        """Provide the minimal information, name, position x, and position y."""
        self.age=age
        self.shield=shield
        self.health=health
        self.name=name
        self.invent={}
        self.i=i
        self.j=j

    @property
    def name(self):
        """Redefeining his name"""
        return self.__name
    @name.setter
    def name(self, new_name): #Method
        if new_name=="":
            print("Ehh I should have a name.")
        elif new_name.isdigit()==True:# Check if it has numbers.
            print("Please introduce a valid name.")
        else:
            self.__name = new_name
        

    def talk(self):
        """A minimal talk, the object 'presents' itself"""
        a= "Hi I am "+self.name
        return a
    def inventory_generator(self):
        """Creates a random inventory for the player"""
        import random as rdm
        r1=rdm.randint(1,20)
        r2=rdm.randint(1,10)
        if r1%2==0:
            self.inventory("iron shield", r2, False)
        if r1%3==0:
            self.inventory("wood shield", r2, False)
        if r1%5==0:
            self.inventory("shield", r2, False)
        if r1%7==0:
            self.inventory("other things", r2, False)
    def trade(self, player):
        """Set the prices and exchange objects with player."""
        self.sell={}
        import random as rdm
        r1=rdm.random()
        print("Do you want to buy or sell something?\nHere are my offers:")
        print("""I sell each item for the following price:\nItem         trade
-------------------/""")
        for key in player.invent.keys():            
            if key in self.invent.keys():
                self.sell[key]=truncate(1/player.invent[key]+r1)
                print(key, "at", self.sell[key])
            else:
                print(key, "     ---")
        
        print("If you want to sell me something, I wait to know what you offer before saying anything else")
        player.trade()
        print("Well, maybe we can arrange some kind of deal...")
        for item in player.sell:
            if player.sell[item]<self.sell[item]:
                try:
                    offer="How many "+item+" do you offer?"
                    a=int(input(offer))
                except ValueError:
                    a=int(input("Sorry I didn't understand you. How many?"))
                    
                if player.invent[item]>a:
                    player.invent[item]-=a
                    self.invent[item]+=a
                if player.invent[item]<=a:
                    print("I took everything")
                    self.invent[item]+=player.invent[item]
                    player.invent[item]=0
        print("Now you have", player.invent)
                    
# Defining enemy type
class Enemy(object):
    """Defines Enemy!!"""
    total=0
    types_total=0
    types={}

    #Define the initial Enemy
    def __init__(self, creature="Troll", damage=30, defense=0, life=100, enemy="Hero"):
        """With the creature, defines the name, defense protect from each attack recieved the amount"""
        # Checking the types
        if creature=="":
            print("Please introduce a valid name.")
        elif creature.isdigit()==True: # Check if it doesn't have numbers inside
            print("Please introduce a valid name.")
        else:
            self.creature=creature
            if creature not in Enemy.types:
                Enemy.types[creature]=1
            else:
                Enemy.types[creature]+=1
            Enemy.types_total=len(Enemy.types)
                
        # Checking the life
        if life<0:
            self.life=0
        else:
            self.life=life
            
        # Checking defense
        if defense<0:
            print("Please introduce a valid defense.")
        else:
            self.__defense = defense
            
        # Checking the enemy
        if enemy=="":
            print("Please introduce a valid enemy.")
        elif enemy.isdigit()==True: # Check if it doesn't have numbers inside
            print("Please introduce a valid enemy.")
        else:
            self.enemy=enemy
            
        self.damage=damage
        self.hits=0
        Enemy.total+=1

    #Defining other methods
    def __str__(self):
        """Explains a little about herself"""
        return("A ancient and unbelivable creature")

    #Defining when it attacks
    def attack(self, enemy, damage):
        """Given an enemy, attacks her with damage"""
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
        """Recieve the damage of an attack, if there is some defense, then it receives less"""
        if self.__defense>0:
            damage-=self.__defense
        self.life-=damage
        if self.life<=0:
            print("E: AHHH, a miserable human has killed me!")
            self.life=0
        else:
            print("E: I've enoughg life to kill you stpuid.")
            

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

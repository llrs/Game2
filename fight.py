# this document describes the fight proces of the game

from characters import Enemy #Imports the class to generate enemy to fight against

# This functions from two list choose,
# acording to the values of the second one, one element of the first list
def weighted_choices(choices, weights):
    import random as rdm
    total = sum(weights)
    treshold = rdm.uniform(0, total)
    for k, weight in enumerate(weights):
        total -= weight
        if total < treshold:
            return choices[k]
        
# Describes what happen while fighting, hits, inventory...
def fight(prota, enemy):
    """Fight prota, vs enemy"""
    while enemy.life>0:
        prota.attack(enemy, prota.damage)
        if enemy.life<=0:
            print(prota.name, "killed the", enemy.creature, "!!")
            if enemy.creature=='Nazgul':
                prota.inventory('shield',1)
            elif enemy.creature=='Stephan the Emperor':
                prota.inventory('iron shield',1)
            break
            enemy.attack(prota, enemy.damage)
            if prota.health<=0:
                print("Unfortunatelly", prota.name, "was killed while attacking the creature number", enemy.total, ".")
                if enemy.life<20:
                    print("He left the last creature  ready to be kill with just", truncate(enemy.life), "points of life!")
                else:
                    print("He left the creature's life at", truncate(enemy.life))
                Enemy.types[enemy.creature]-=1
                print("In his sucessfully life he has killed:", Enemy.types)
                input("Press any key to exit the program")
                break

# Creates the event of the figth in a situation.
def Battle(prota):
    """Given a protagonist of the battle starts, or not, fighting"""
    import random as rdm
    a=rdm.randint(0,5)
    if a==0:
        prota.health=100
        print("""This night was pacific, I didn't needed to fight, and I could take a break, but
I won't be so luky next time""")
    else:
        print("OH! what are this creatures??\nARGh!")
        a=rdm.randint(0,5)
        for i in range(a):
            # Creates randomly which type of enemy he will fight
            r=rdm.randint(0,5)
            if r==0:
                goblin=Enemy(creature="Goblin", damage=10, defense=0, life=10)
                fight(prota, goblin)
            elif r==1:
                troll=Enemy(creature="Troll", damage=20, defense=0, life=30)
                fight(prota, troll)
            elif r==2:
                supertroll=Enemy(creature="SuperTroll", damage=40, defense=0, life=50)
                fight(prota, supertroll)
            elif r==3:
                urukhai=Enemy(creature="Uruk Hai", damage=60, defense=5, life=70)
                fight(prota, urukhai)
            elif r==4:
                nazgul=Enemy(creature="Nazgul", damage=80, defense=20, life=100)
                fight(prota, nazgul)
            elif r==5:
                sphanemperor=Enemy(creature="Stephan the Emperor", damage=100, defense=30, life=150)
                fight(prota, sphanemperor)
            else:
                print("Something is wrong creating the battle")

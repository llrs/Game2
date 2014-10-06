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
def fight(prota, enemy, app):
    """Fight prota, vs enemy"""
    while enemy.life>0:
        prota.attack(enemy, prota.damage, app)
        if enemy.life <= 0:
            death = "{} has been killed!!".format(enemy.creature)
            
            if enemy.creature=='Nazgul':
                prota.inventory('shield',1, app)
            elif enemy.creature=='Stephan the Emperor':
                prota.inventory('iron shield',1, app)

        else:
            enemy.attack(prota, enemy.damage, app)
            if prota.health<=0:
##                death= "Unfortunatelly {}was killed while attacking the creature"\
##                       " number {}".format(prota.name, enemy.total)
##                Enemy.types[enemy.creature]-=1
##                summary = "In his sucessfully life he has killed: {}".format(Enemy.types)
                break

# Creates the event of the figth in a situation.
def Battle(prota, app):
    """Given a protagonist of the battle starts, or not, fighting"""
    import random as rdm
    a=rdm.randint(0,5)
    for i in range(a):
        # Creates randomly which type of enemy he will fight
        r=rdm.randint(0,5)
        if r==0:
            goblin=Enemy(creature="Goblin", damage=10, defense=0, life=10)
            fight(prota, goblin, app)
        elif r==1:
            troll=Enemy(creature="Troll", damage=20, defense=0, life=30)
            fight(prota, troll, app)
        elif r==2:
            supertroll=Enemy(creature="SuperTroll", damage=40, defense=0, life=50)
            fight(prota, supertroll, app)
        elif r==3:
            urukhai=Enemy(creature="Uruk Hai", damage=60, defense=5, life=70)
            fight(prota, urukhai, app)
        elif r==4:
            nazgul=Enemy(creature="Nazgul", damage=80, defense=20, life=100)
            fight(prota, nazgul, app)
        elif r==5:
            sphanemperor=Enemy(creature="Stephan the Emperor", damage=100, defense=30, life=150)
            fight(prota, sphanemperor,app)
        else:
            raise("Unexpected error with the enemy")

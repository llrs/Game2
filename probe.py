name = input("You have a hero of name...\n Which is your name?\t")
print("You have a hero of name", name, ". He is a prince searching adventures")
print("He is young, and so their strength is high.")
age = float(input("How old is your hero?\t"))
while age<=0:
    print("Please introduce a valid age")
    age = float(input("How old is your hero?\t"))

print("He found a cove with some trolls...\n \n THE ADVENTURE BEGINS")
#damage=input("How much damage do you guess each troll inflinge?\t")
#while damge==class.letters:
#    print("It is better with a number...")
damage = float(input("How much damage do you guess each troll inflinge?\t"))

while damage <= 0:
    print("A Troll always damage something, sometimes itself but also other people!")
    damage = float(input("How much damage it can make to you?\t"))
    
life = float(input("Usually the trolls have a life points of 100, but not this time..\n" \
                 "How much do you guess they have?\t"))
while life<=0 or life>=1000:
    if life<=0:
        print("Did you find a dead troll??\n")
        life=int(input("How much life points have your alive Troll?\t"))
    else:
        print("Do you want a Troll or a Dragon?...")
        life=int(input("How much life have your TROLL?\t"))

strength = -age*(age-100)/25
        
health=100
trolls=0

life_troll=life
question="Do you want to fight with one troll? "
while health>0:
    print("\n", name, "with just", health, "points of health, and ", strength, \
               " points of strength starts to kill trolls of", life, "points,\n" \
                "which each takes from our hero,", damage,"damage points.")
    answer=input(question)
    if answer.lower() == 'yes' or answer.lower() == 'y':
        print("Your hero swings an evil troll!")
        k=0
        life_troll = life
        while life_troll > 0:
            k +=1
            life_troll -= strength
            
            if life_troll >0 and health>0:
                health -= damage
                if health<=0:
                    health=0
                    print(name, "attaks and after an incredible fight leaves Trolls' life at", life_troll,
                      "unfortunatelly, he also takes some damage and now is dead. ")
                    print("He has killed", trolls-1, "trolls at the young age of", age, "years.\n",
                          "He has leave the last troll just at", life_troll,
                          "points, ready to kill by another hero.")
                else:
                    life_troll=0
                    print(name, "Killed the Troll, but now he has", health, "points of health")
                
        trolls+=1
        
    if answer.lower() == 'no' or answer.lower() == 'n':
        print("He has killed", trolls, "trolls he is an authentic hero!", 
              "But he has only", health, "points of health,"\
              " so he goes back to the caste to sleep and prepare for the next battle.")
        health=100
    if answer.lower() == 'quit' or answer.lower()== 'q':
        break

#what if
people = 20
cats = 30
dogs = 15

#if=statement, if this Boolean expression is True,
#then run the code under it; otherwise, skip it.
if people < cats:
    #a : at the end of a line is how you tell Python
    #you are going to create a new "block" of code,
    #then indenting to tell python what lines of code
    #are in that block.
    print("Too many cats! The world is doomed!")

if people > cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print(" The world is drooled on!")

if people > dogs:
    print(" The world is dry!")

dogs +=5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")

if people == dogs:
    print("People are dogs.")

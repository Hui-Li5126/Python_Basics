#Lists are one of the most common data structures programmers use.
#A list is an ordered list of things you want to store and access
  #randomly or linearly by an index.
ten_things = "Apples Oranges Crows Telephone Light Sugar"
print("Wait there are not 10 things in that list. Let's fix that.")
stuff = ten_things.split(' ')

more_stuff = ["days", "Night", "Song", "Fris-bee", "Corn", "Banana", "Girl", "Boy"]

for i in range(10-len(stuff)): #or while len(stuff) !=10:
    next_one =more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff[3:5]))

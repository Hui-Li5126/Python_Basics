#While loops
#what they do is simply do a test like an if-statement, but
#instead of running the code block once, they jump back to the
#"top" where the while is and repeat. A while-loop runs until
#the expression is False.

#rules to follow:
#1.make sure to use while-loops sparingly.
  #usually a for-loop is better.
#2.Review your while statement and make sure that the Boolean
  #test will become False at some point.
#3.When in doubt, print out your test variable at the top and
  #bottom of the while-loop to see what it's doing.

i = 0
numbers = []

while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)

    i=i+1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")

print("The numbers: ")

for num in numbers:
    print(num)


def print_range(n, up_bound):
    i = 0
    numbers = []
    while i < up_bound:
        print(f"At the top i is {i}")
        numbers.append(i)

        i=i+n
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

    print("The numbers: ")
    for num in numbers:
        print(num)

print_range(2,10)

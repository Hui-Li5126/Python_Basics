#Modules, Classes, and Objects
#Modules are a python file with some functions or variables in it....
  #which you can import....
  #And access the functions or varibles of with the . (dot) operator.
  #think about a module as a specialized dictionary that can store Python code
  #so you can access it with the . operator.

#Class is a way to take a grouping of functions and data and
  #place them inside a container so that you can access them
  #with the . (dot) operator.

class MyStuff(object):

    def __init__(self):
        #setting the tangerine instance variable
        self.tangerine = "And now a thousand years between"
        #apple function
    def apple(self):
        print("I am classy apples")

thing = MyStuff()
thing.apple()
print(thing.tangerine)


#dict style
mystuff['apples']
#module style
mystuff.apples()
print(mystuff.tangerine)

#class style
thing = Mystuff()
thing.apples()
print(thing.tangerine)


class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

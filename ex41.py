#Word drills
#class Tell Python to make a new type of thing.
#object Two meanings: the most basic type of thing, and any
  #instance of some thing.
#instance: What you get when you tell Python to create a class.
#def: How you define a function inside a class.
#self: Inside the functions in a class, self is a variable for the
   #instance/object being accessed.
#inheritance: The concept that one class can inherit traits from another class,
  #much like you and your parents.
#composistion: The concept that a class can be composed of other classes as parts,
  #much like how a car has wheels.
#attribute: A property classes have that are from composition and are usually variables.
#is-a: A phrase to say that something inherits from another, as in a "salmon" is-a "fish"
#has-a: A phrase to say that something is composed of other things or has a trait,
  #as in "a salmon has-a mouth"

#Person is a object
class Person(object):
    def __init__(self, name):
        ## Person has a name
        self.name = name
        ##Person has a pet of some kind
        self.pet = None

class Employee(Person):
    def __init__(self, name, salary):
        """
        below is how you can run the __init__ method of a parent
        class reliably.
        """
        super(Employee, self).__init__(name)
        self.salary = salary

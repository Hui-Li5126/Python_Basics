#sys.argv is a list in pythonforbeginners
#which contains the command-line arguments passed
#to the script.
#sys.argv[0] is the name of the script.

#argv vs input(), input uses keyboard while the script
#is running
from sys import argv
#script, first, second, third = argv
script, first, second, third =argv

print("The script is called: ", script)
print("The script is called: ", first)
print("The script is called: ", second)
print("The script is called: ", third)
print("enter something: ", input())
print("number of arguments: ", len(argv)-1)  #3 arguments

#when run the code in cmd, need to type python ex13.py first second third
#to give it another three arguments.
#the command line arguments are strings, even if you typed numbers.

# input('? ') = x? doesn't work, because it's backward to how it should work.

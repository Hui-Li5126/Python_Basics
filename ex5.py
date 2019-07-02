#format string
#all variables initially start with my_, use ctrl+shift+f
#to launch Fine and Replace Panel
#round function rounds a number to specified decimals
#default is 0, meaning to nearest integer
name = 'Zed A. Shaw'
age = 35
height = round(74.333)
weight = 180
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

#f before "" and {} tell python this string needs
#to be formatted, put these variables in there.
print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usally {teeth} depending on the coffee.")
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

#\  escape anything after it,  the cases below have special
#meaning

tabby_cat ="\tI'm tabbed in."  #horizontal tab
persian_cat="I'm split\non a line." #new line
backslash_cat="I'm \a cat."  # escape a, I'm cat
backslash_cat2="I'm \\a cat" # I'm \a cat


fat_cat='''
I'll do a list:
\t* cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''
print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(backslash_cat2)
print(fat_cat)

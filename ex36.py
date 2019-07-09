#designing and debugging
#Rules for if-statements
#1.every if-statement must have an else.
#2.If this else should never run because it doesnt make sense,
   #then you must use a die function in the else that prints
   #out an error message and dies, just like we did in the last
   #exercise. This will find many errors.
#3. Never nest if-statements more than two deep and always try to do them one deep
#4.Treat if-statements like paragraphs, where each if-elif-else grouping
   #is like a set of sentences. Put blank lines before and aftere.
#5.Your boolean tests should be simple. If they are complex, move their calculations to
  #variables earlier in your function and use a good name for the variable.

#Rules for loops:
#1.Use a while - loop only to loop forever, only applies to Python
#2.Use a for-loop for all other kinds of looping.

#Tips for debugging
#1.Do not use a "debugger". You do not get any specific useful info, and you find
  #a whole lot of information that doesn't help and is just confusing.
#2.The best way to debug a program is to use print to print out the values of variables
  #at points in the program to see where they go wrong.
#3.Code a little, run a little, fix a little.

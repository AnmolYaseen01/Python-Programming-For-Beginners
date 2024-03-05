'''We begin by defining a list in line 2. At line 3, we define a for loop. This line tells Python to pull a name from the list languages, and associate it with the temporary variable language. At 4 we tell Python to print the name that’s just been assigned to language. Python then repeats lines 3 and 4, once for each name in the list'''
languages = ["Python", "Swift", "C++"]
for language in languages:
    print(language)
    
#  the above for loop can be read as "For every language in the list of languages, print the language’s name."

# Using singular and plural names can help you identify whether a section of code is working with a single element from the list or the entire list.
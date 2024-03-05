languages = ["Python", "Swift", "C++"]
print(languages)

'''To maintain the original order of a list but present it in a sorted order, you 
can use the sorted() function. The sorted() function lets you display your list 
in a particular order but doesn’t affect the actual order of the list.'''
languages=(sorted(languages))
print(languages)

# we can print sorted lists directly as well without assigning it to any variable as follow:

print(sorted(languages))

'''The sorted() function can also accept a reverse=True
argument if you want to display a list in reverse alphabetical order.
Sorting a list alphabetically is a bit more complicated when all the values are not in 
lowercase.'''
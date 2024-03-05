'''Seeing the World: Think of at least five places in the world you’d like to 
visit.
Store the locations in a list. Make sure the list is not in alphabetical order.
Print your list in its original order. Don’t worry about printing the list neatly, 
just print it as a raw Python list.'''

places=['south korea', 'saudi arabia','china','france','america']
print(places)

print("i would love to visit the following places: {}".format(places))
# output: i would love to visit the following places: ['south korea', 'saudi arabia', 'china', 'france', 'america']

print(f"i would love to visit the following places: {places}")
# output: i would love to visit the following places: ['south korea', 'saudi arabia', 'china', 'france', 'america']

# Use sorted() to print your list in alphabetical order without modifying the actual list.

print(sorted(places))     #it sorts the list temporarily.

# Show that your list is still in its original order by printing it.
print(places)


# Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
print(sorted(places,reverse=True))

# Show that your list is still in its original order by printing it again.
print(places)

# Use reverse() to change the order of your list. Print the list to show that its order has changed.
places.reverse()    #it justr reverses the order of the list.
print(places)

# Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
places.sort()     #it sorts the list permanently.

# Use sort() to change your list so it’s stored in reverse alphabetical order.Print the list to show that its order has changed.
places.sort(reverse=True)       #it also sorts the list permanently

# use len() to print a message.
len(places)
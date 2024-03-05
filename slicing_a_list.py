'''To make a slice, you specify the index of the first and last elements you 
want to work with. As with the range() function, Python stops one item 
before the second index you specify. '''

places=['south korea', 'saudi arabia','china','france','america']
print(players[0:3])

# You can generate any subset of a list. 
'''If you omit the first index in a slice, Python automatically starts your 
slice at the beginning of the list.'''
print(players[:3])

'''A similar syntax works if you want a slice that includes the end of a list.'''
print(players[0:])
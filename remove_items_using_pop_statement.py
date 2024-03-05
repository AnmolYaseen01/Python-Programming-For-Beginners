'''The pop() method removes the last item in a list.The term pop comes from thinking of a list as a stack of items and popping one item off the top of the stack.''' 

'''Sometimes you’ll want to use the value of an item after you remove it from a list. For example, you might want to get the x and y position of an alien that was just shot down, so you can draw an explosion at that position. In a web application, you might want to remove a user from a list of active members and then add that user to a list of inactive members.'''

numbers=['1','2','3']
popped_numbers=numbers.pop()
# numbers.pop() deletes the last item in the list and assign it to a variable named popped number for later use in the program
print(numbers)
# output=['1', '2']
print(popped_numbers)
# output=3


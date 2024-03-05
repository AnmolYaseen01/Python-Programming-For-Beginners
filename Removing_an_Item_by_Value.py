# If you only know the value of the item you want to remove, you can use the remove() method.

'''The remove() method deletes only the first occurrence of the value you specify. If there’s 
a possibility the value appears more than once in the list, you’ll need to use a loop 
to make sure all occurrences of the value are removed.'''

numbers=[1,2,3,4]
numbers.remove(3)
print(numbers)
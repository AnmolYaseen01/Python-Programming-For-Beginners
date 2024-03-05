# Using the range() Function
for value in range(1, 5):
 print(value)
 
 '''Although this code looks like it should print the numbers from 1 to 5, it 
doesn’t print the number 5.You can also pass range() only one argument, and it will start the 
sequence of numbers at 0. For example, range(6) would return the numbers 
from 0 through 5'''
 
 '''We can also use the range() function to tell Python to skip numbers in a 
given range. If you pass a third argument to range(), Python uses that value 
as a step size when generating numbers'''

squares = []
for value in range(1, 16):
    squares.append(value ** 2)
print(squares)
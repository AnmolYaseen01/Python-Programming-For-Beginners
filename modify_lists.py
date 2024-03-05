'''The syntax for modifying an element is similar to the syntax for accessing 
an element in a list. To change an element, use the name of the list followed 
by the index of the element you want to change, and then provide the new 
value you want that item to have.'''

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

# output
# ['honda', 'yamaha', 'suzuki']
# ['ducati', 'yamaha', 'suzuki']
'''You can loop over all the values in a tuple using a for loop'''
integers=(1,2,2,3,4)
for integer in integers:
    print(integer)
    
    '''Although you can’t modify a tuple, you can assign a new value to a variable 
that represents a tuple. So if we wanted to change our dimensions, we could 
redefine the entire tuple as follow:'''
integers=(1,2,2,3,4)
for integer in integers:
    print(f"original integers:{integer}")
integers=(2,2,4,5,6)
for integer in integers:
    print(f"modified integers:{integer}")    
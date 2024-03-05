# A keyword argument is a name-value pair that you pass to a function.
'''The order of keyword arguments doesn’t matter because Python 
knows where each value should go'''
def person(name, gender):
    """Display information ."""
    print(f"\nI have a {name}.")
    print(f" {name}'is a {gender.title()}.")

# Calling the function with different arguments
person(name='Ali', gender='boy')
person(name='Ali', gender='boy')

'''When you use keyword arguments, be sure to use the exact names of the parameters in 
the function’s definition'''
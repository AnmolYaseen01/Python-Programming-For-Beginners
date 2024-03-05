'''Python must match each argument in the function call with a parameter in the function definition'''
'''positional arguments, which need to be in the same order the parameters were written'''
def person(name, gender):
    """Display information ."""
    print(f"\nI have a {name}.")
    print(f" {name}'is a {gender.title()}.")

# Calling the function with different arguments
person('Ali', 'boy')

'''You can use as many positional arguments as you need in your functions. Python works through the arguments you provide when calling the 
function and matches each one with the corresponding parameter in 
the function’s definition.'''

# You can use as many positional arguments as you need in your functions. Python works through the arguments you provide when calling the function and matches each one with the corresponding parameter in 
the function’s definition.

'''When you use default values, any parameter with a default value needs to be listed 
after all the parameters that don’t have default values. This allows Python to continue interpreting positional arguments correctly'''

def describe_pet(pet_name, animal_type='cat'):
 """Display information about a pet."""
 print(f"\nI have a {animal_type}.")
 print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet(pet_name='lucy')
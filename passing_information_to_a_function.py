'''Modified slightly, the function greet_user() can not only tell the user Hello!
but also greet them by name. For the function to do this, you enter username
in the parentheses of the function’s definition at def greet_user(). By adding username here you allow the function to accept any value of username you 
specify. The function now expects you to provide a value for username each 
time you call it. When you call greet_user(), you can pass it a name, such as 
'jesse', inside the parentheses:'''
def greet_user(username):
 """Display a simple greeting."""
 print(f"Hello, {username.title()}!")
 
greet_user('jesse')

'''In the preceding greet_user() function, we defined greet_user() to require a 
value for the variable username. Once we called the function and gave it the 
information'''

# The variable username in the definition of greet_user() is an example of a parameter, a piece of information the function needs to do its job.
# The value 'jesse' in greet_user('jesse') is an example of an argument. An argument is a piece of information that’s passed from a function call to a function. 
# People sometimes speak of arguments and parameters interchangeably. 
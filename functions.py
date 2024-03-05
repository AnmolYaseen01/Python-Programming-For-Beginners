'''unctions, which are named blocks of code 
that are designed to do one specific job. 
When you want to perform a particular task 
that you’ve defined in a function, you call the function 
responsible for it. If you need to perform that task
multiple times throughout your program, you don’t need to type all the 
code for the same task again and again; you just call the function dedicated 
to handling that task, and the call tells Python to run the code inside the 
function. You’ll find that using functions makes your programs easier to 
write, read, test, and fix.
In this chapter you’ll also learn ways to pass information to functions. 
You’ll learn how to write certain functions whose primary job is to display 
information and other functions designed to process data and return a 
value or set of values. Finally, you’ll learn to store functions in separate files 
called modules to help organize your main program files'''

# Here’s a simple function named greet_user() that prints a greeting:
def greet_user():
 """Display a simple greeting."""
 print("Hello!")
 
 greet_user()
 
 ''' line 18 uses the keyword def to inform Python that you’re defining a function. This 
is the function definition, which tells Python the name of the function and, if 
applicable, what kind of information the function needs to do its job. The 
parentheses hold that information.Finally, the definition 
ends in a colon'''

'''Any indented lines that follow def greet_user(): make up the body of 
the function. The text at line 19 is a comment called a docstring, which describes 
what the function does. Docstrings are enclosed in triple quotes, which 
Python looks for when it generates documentation for the functions in your 
program'''

'''A function call tells 
Python to execute the code in the function. To call a function, you write 
the name of the function, followed by any necessary information in parenthese'''

#  Because no information is needed here, calling our function is as simple as entering greet_user().
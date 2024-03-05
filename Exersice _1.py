# Personal Message: Use a variable to represent a person’s name, and print 
# a message to that person. Your message should be simple, such as, “Hello dear!”
print('Hello dear!')

# Name Cases: Use a variable to represent a person’s name, and then print 
# that person’s name in lowercase, uppercase, and title case.
name="eric"
name.lower()
name.upper()
name.title()

# Famous Quote: Find a quote from a famous person you admire. Print the 
# quote and the name of its author. Your output should look something like the 
# following, including the quotation marks:
# Albert Einstein once said, “A person who never made a 
# # mistake never tried anything new.”
print('Albert einstein once said, "A person who never made a mistake never tried anything new"')
Albert einstein once said, "A person who never made a mistake never tried anything new"

# Famous Quote 2: Repeat Exercise 2-5, but this time, represent the 
# famous person’s name using a variable called famous_person. Then compose 
# your message and represent it with a new variable called message. Print your 
# message.
famous_person="Albert Einstein"
message="“A person who never made a mistake never tried anything new.”"
print(f"{famous_person} once said {message}")

#  Stripping Names: Use a variable to represent a person’s name, and include 
# some whitespace characters at the beginning and end of the name. Make sure 
# you use each character combination, "\t" and "\n", at least once.
# Print the name once, so the whitespace around the name is displayed. 
# Then print the name using each of the three stripping functions, lstrip(), 
# rstrip(), and strip().
name=" eric "
print(name)
name.rstrip()
name.lstrip()
name.strip()

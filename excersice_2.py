'''Names: Store the names of a few of your friends in a list called names. Print 
each person’s name by accessing each element in the list, one at a time.'''

friends=['eric','mathew','justin']
print(friends[0])
# output:eric
print(friends[1])
# output:mathew
print(friends[2])
# output:justin


'''Greetings: Start with the list you used in Exercise 3-1, but instead of just 
printing each person’s name, print a message to them. The text of each message should be the same, but each message should be personalized with the 
person’s name.'''
 
friends==['eric','mathew','justin']
message_1=f"hi {friends[0].title()}, how are you?"
message_2=f"hi {friends[1].title()}, how are you?"
message_3=f"hi {friends[2].title()}, how are you?"
print(message_1)
print(message_2)
print(message_3)   
languages=['Python','React','Html','CSS','C++','Javascript']
for language in languages:                                #lines inside the loop must be indented.
    print(f"i would love to learn {language.title()}.")   #indenting the print statement after the for loop is very important to avoid an indentation error.
   
  
'''output:
i would love to learn Python.
i would love to learn React.
i would love to learn Html.
i would love to learn Css.
i would love to learn C++.
i would love to learn Javascript.'''

places = ['america', 'england', 'russia', 'US', 'UK', 'egypt']
for place in places:
    print(f"I would love to visit {place.title()}.")
    
'''I would love to visit America.
I would love to visit England.
I would love to visit Russia.
I would love to visit Us.
I would love to visit Uk.
I would love to visit Egypt.'''

# Any lines of code after the for loop that are not indented are executed once without repetition.

languages=['Python','React','Html','CSS','C++','Javascript']
for language in languages:                                
    print(f"i would love to learn {language.title()}.") 
print(f"it would be an honour to learn {languages}.") 

'''output:
I would love to visit Us.
I would love to visit Uk.
I would love to visit Egypt.
i would love to learn Python.
i would love to learn React.
i would love to learn Html.
i would love to learn Css.
i would love to learn C++.
i would love to learn Javascript.
it would be an honour to learn ['Python', 'React', 'Html', 'CSS', 'C++', 'Javascript'].
'''
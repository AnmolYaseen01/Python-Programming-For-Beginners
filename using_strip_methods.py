# To remove the whitespace from the string temporarily:
favourite_language="python "
favourite_language.rstrip()
# output:'python'

# To remove the whitespace from the string permanently, you have to associate the stripped value with the variable name:
favourite_language="pyhton "
favourite_language=favourite_language.rstrip()
favourite_language
# output:'pyhton'

# You can also strip whitespace from the left side of a string using the lstrip() method, or from both sides at once using strip():
favorite_language = ' python ' 
favorite_language.rstrip()
# ' python' 
favorite_language.lstrip()
# 'python ' 
favorite_language.strip()
# 'python'
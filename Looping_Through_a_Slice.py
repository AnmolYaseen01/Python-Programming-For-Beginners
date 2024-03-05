# Looping Through a Slice
players = ['charles', 'martina', 'michael', 'florence', 'eli'] 
print("Here are the first three players on my team:")
for player in players[:3]:
 print(player.title())
 
 '''Instead of looping through the entire list of players at line 4, Python loops 
through only the first three names:'''
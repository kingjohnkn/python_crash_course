# slicing a list

players = ['charles', 'martina', 'michael', 'florence', 'eli']

# output the first three elements in a list
print(players[:3])

# output the second, third, and fourth items in a list
print(players[1:4])

# second to last
print(players[2:])

# output the last three items
print(players[-3:])

# loop through a slice
print("Here are the first three players on my team:")
three_players = [player.title() for player in players[:3]]
print(three_players)
players = ['charles','martina','michael','florence','eli']
print(players[0])
print(players[1])
print(players[2])
print(players[3])
print(players[4])
some_players = players[0:3] #starting at index 0 and stops at index 3(0,1,2)
print(some_players)
print(players[1:4])
# Below statement players [0:4]
print(players[:4]) #skipping start index means it will use default start index 0
print(players[2:]) # omitting stop index means it will workthrough the last item
print(players[-3:]) 

print("Here are the first three players on my team")
for player in players[:3]:
    print(player.titel())
    


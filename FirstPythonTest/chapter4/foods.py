my_foods = ['pizza','falafel','carrot cake'] #source
friend_foods = my_foods[:] #start zero through the last item
print("My food list")
print(my_foods)
print("friend's food list")
print(friend_foods)
my_foods[0] = 'chese pizza'
print(my_foods)
print('friends food list',friend_foods)

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("after appending element into lists")
print()

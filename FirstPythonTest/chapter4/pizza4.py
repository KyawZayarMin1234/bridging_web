my_foods = ['pizza','falafel','carrot cake']

friend_foods = my_foods[:]
my_foods.append('cheese pizza')
friend_foods.append('pineapple pizza')

print("my favourite pizzas are :")
for pizza in my_foods:
    print(pizza)
    
print("My friend's favourite pizza are:")
for pizza in friend_foods:
    print(pizza)
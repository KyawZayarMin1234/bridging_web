buffet_foods = ('ham burger','pizza','fried  chicken','ice cream','biryani')
print('favourite foods')
for food in buffet_foods:
    print(food)
    
buffet_foods = ('ham burger','pizza','fried  chicken','ice cream','biryani','noodle','hotpot')
print("revised menu")
for ind, food in enumerate(buffet_foods): #index and value
    print(ind, food)
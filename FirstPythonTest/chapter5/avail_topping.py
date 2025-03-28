available_toppings = ['mushrooms','olives','green peppers','pepperoni','pineappl','extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"adding {requested_topping}")
        
    else:
        print(f"sorry,we don't have{requested_topping}")
requested_toppings = ['mushrooms','green peppers','extra cheese']
for topping in requested_toppings:
    if topping == 'green papers':
        print("sorry,we are out of green peppers right now.")
    else:
        print(f"adding{topping}")
print("\n finished making pizza")
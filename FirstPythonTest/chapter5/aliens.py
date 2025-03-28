aliens_colors = ['red','green','yellow']

aliens_color = input("enter alien color")
for color in aliens_colors:
    if aliens_color == 'green':
        print("you earned 5 points")
    
    else:
        print("you fill")
    
for aliens_color in aliens_colors:
    if aliens_color=='green':
        print("you earned 5 points.")
        
    elif aliens_color in aliens_colors:
        print("you earned 5 points")
    
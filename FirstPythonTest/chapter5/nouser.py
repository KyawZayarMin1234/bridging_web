usernames = ['admin', 'robert','kevin','davidson','sofia','marie','petra']
print(len(usernames))
if len(usernames) == 0:
    print("we need to find soume users.")
    
else:
    for user in range(0,len(usernames)):
        print(usernames.pop())
    
print("after popping out users!!")
print(usernames)
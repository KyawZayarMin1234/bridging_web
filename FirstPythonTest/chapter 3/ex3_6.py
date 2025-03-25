friends = ['Robert', 'Caral', 'Petra']
print("Wow! we've got a bigger dinner table.")
friends.insert(0,"KO Ko")
friends.insert(2,"Sandi")
friends.insert(3,'Yuya')
print(f"{friends[0]}, Pleaase join the dinner tonight.")
print(f"{friends[1]}, Pleaase join the dinner tonight.")
print(f"{friends[2]}, Pleaase join the dinner tonight.")
print(f"{friends[3]}, Pleaase join the dinner tonight.")
print(f"{friends[4]}, Pleaase join the dinner tonight.")

print("Sorry, there is only two people we can invite for dinner.")
print(f"{friends.pop()}, We are sorry. We can't invite you to dinner.")
print(f"{friends.pop()}, We are sorry. We can't invite you to dinner.")
print(f"{friends.pop()}, We are sorry. We can't invite you to dinner.")
print(f"{friends.pop()}, We are sorry. We can't invite you to dinner.")

print (f"{friends[0]}, you are still invited.")
print (f"{friends[1]}, you are still invited.")

del friends[0]
del friends[0]
print (f"after deleting two guests form list{friends}")
   
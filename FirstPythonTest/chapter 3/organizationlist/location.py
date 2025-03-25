""" 3-8. Seeing the World: Think of at least five places in the world you’d like  
to visit.
 • Store the locations in a list. Make sure the list is not in alphabetical order.
 • Print your list in its original order. Don’t worry about printing the list neatly; 
just print it as a raw Python list"""


locations = ['Taungyi','Innlay','Seoul','Tokyo']
print(locations) # printing raw python list

#usint tempory sorted function without o0ffecting original list
print (sorted(locations))

print(f"original list \n {locations}")

locations.reverse()
print(f"second time reverse call and order of list {locations}")

locations.sort() #ngaw sin kyi lite ascedning order
print(f"after sorting in alphabetical order{locations}")

locations.sort(reverse=True) #kyi sin ngal lite descending order
print(f"after sorting with decreasing order{locations}")

print(f"number of places that I like to travel {len(locations)}")

#print(locations[5])
print(locations(-6)) #index starts from -1 to -5
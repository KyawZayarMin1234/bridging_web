motorcycles = [ 'honda', 'yamaha', 'suzuki']
motorcycles.insert(0,'BMW')
print (motorcycles)

motorcycles[0] = 'ducati'
del motorcycles [0]
print (motorcycles)

motorcycles.append('honda')
print(motorcycles)


motorcycles = []

motorcycles.append('honda')
motorcycles.append('ducat')
motorcycles.append('yamaha')

cycles = ['honda', 'yamaha', 'suzuki']

cycles.insert(0, 'BMW')

popped_motorcycles = motorcycles.pop()
print (f"remaining motorcycle after pop call {motorcycles}")
print (F"popped motorcycle {popped_motorcycles}")
print(motorcycles)
print(motorcycles.pop(0))
print(f" popped ele")
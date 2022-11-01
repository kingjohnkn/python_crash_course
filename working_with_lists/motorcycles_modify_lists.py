motorcycles = ['honda', 'yamaha', 'suzuki']
print(f"\n***** Original: {motorcycles} *****\n")

# modifying elements in a list
motorcycles[1] = 'ducati'
print(f"Modified: {motorcycles}")

# adding elements to a list

# 1. appending elements to the end of a list
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')
print(f"Append: {motorcycles}")

# 2. appending elements to an empty list
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(f"Append from empty: {motorcycles}")

# inserting elements into a list
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(2, 'ducati')
print(f"Insert: {motorcycles}")

# removing elements from a list

# 1. remove using del statement
motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[2]
print(f"Remove using del: {motorcycles}")

# 2. remove using pop() method
# pops last item on the list
motorcycles = ['honda', 'yamaha', 'suzuki']
popped_motorcycle = motorcycles.pop()
print(f"Remove using pop(): {motorcycles}")
print(f"\tPopped item: {popped_motorcycle}")

# 3. popping from any position
motorcycles = ['honda', 'yamaha', 'suzuki']
popped_motorcycle = motorcycles.pop(1)
print(f"Pop from any position: {motorcycles}")
print(f"\tPopped item: {popped_motorcycle}")

# 4. removing an item by value
motorcycles = ['honda', 'yamaha', 'suzuki']
removed_motorcycle = 'yamaha'
motorcycles.remove(removed_motorcycle)
print(f"Remove by value: {motorcycles}")
print(f"\tWe removed {removed_motorcycle} from the list")

# sort permanently with x.sort()
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(f'\nOriginal cars list: {cars} \n')
cars.sort()
print(f'Sorted permanently: {cars}\n')

# sort permanently in reverse order x.sort(reverse=True)
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(f'Permanently in reverse order: {cars}\n')

# sort temporarily using sorted(x) | sorted(x, reverse=True)
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(f'Original: {cars}')
print(f'Temporary sort: {sorted(cars)}')
print(f'Temporary sort reverse: {sorted(cars, reverse=True)}')
print(f'Original: {cars}\n')

# reverse original order of a list cars.reverse()
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
print(f'Reverse list order: {cars}\n')

# length of a string using len(x)
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(f'Original: {cars}')
print(f'The length of the list is: {len(cars)}')
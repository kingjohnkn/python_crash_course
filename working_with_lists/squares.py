squares = []
for value in range(1, 11):
    squares.append(value ** 2)

print(squares)

# list comprehensions
squares_2 = [value**2 for value in range(1,11)]
print(squares_2)

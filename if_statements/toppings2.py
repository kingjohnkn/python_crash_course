available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese', 'pineapple']

for topping in requested_toppings:
    if topping in available_toppings:
        print(f"Adding {topping}")
    else:
        print(f"Sorry, we don't have {topping}")
    
print("\nFinished making your pizza!")
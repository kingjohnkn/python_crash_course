# requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
requested_toppings = []

# if 'mushrooms' in requested_toppings:
#     print("Adding mushrooms.")
# if 'pepperoni' in requested_toppings:
#     print("Adding pepperoni.")
# if 'extra cheese' in requested_toppings:
#     print("Adding extra cheese.")
    
# print("\nFinished making your pizza!")
if requested_toppings:
    for topping in requested_toppings:
        if topping == 'green peppers':
            print("Sorry, we are out of green peppers right now.")
        else:
            print(f"Adding {topping}")
else:
    print("Are you sure you want a plain pizza?")
    
# print("\nFinished making your pizza!")
    
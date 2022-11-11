def main():
    # x1, x2, x3 = eval(input("Please enter three values: "))

    x1 = int(input("Enter the first number: "))
    x2 = int(input("Enter the second number: "))
    x3 = int(input("Enter the third number: "))

    if x1 >= x2:
        if x1 >= x3:
            print("The largest number is ", x1)
    elif x2 >= x1:
        if x2 >= x3:
            print("The largest number is ", x2)
    elif x3 >= x1:
        if x3 >= x2:
            print("The largest number is ", x3)


main()

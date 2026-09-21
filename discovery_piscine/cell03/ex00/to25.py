number = input("Enter a number less than 25\n")
if int(number) > 25:
    print("Error")
else:
    while int(number) <= 25:
        print("Inside the loop, my variable is " + str(number))
        number = int(number) + 1
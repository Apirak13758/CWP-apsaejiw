import math
number = float(input("Give me a number: "))
if number == math.floor(number):
    print("This number is an integer.")
else:
    print("This number is a decimal.")
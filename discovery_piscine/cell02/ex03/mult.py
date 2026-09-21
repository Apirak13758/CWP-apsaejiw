st = input("Enter the first number:\n")
nd = input("Enter the second number:\n")
mult = int(st) * int(nd)
print(str(st) + " X " + str(nd) + " = " + str(mult))
if mult == 0:
    print("This number is both positive and negative.")
elif mult < 0:
    print("This number is negative.")
else:
    print("This number is positive.")

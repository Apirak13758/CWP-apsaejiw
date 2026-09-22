my_age = int(input("Please tell me your age: "))
print(f"You are currently {my_age} years old.")
for i in range(10, 40, 10):
    my_age += 10
    print(f"In {i} years, you'll be {my_age} years old.")
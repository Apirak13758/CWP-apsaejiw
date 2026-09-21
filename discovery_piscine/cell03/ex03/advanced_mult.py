for j in range(0, 11):
    print(f"Table de {j}: ", end="")
    for i in range(0, 11):
        result = j * i
        print(str(result), end=" ")
    print()
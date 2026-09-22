array = [2, 8, 9, 48, 8, 22, -12, 2]
new_array = [array[i] + 2 for i in range(len(array)) if array[i] + 2 > 5]
print(array)
print(new_array)
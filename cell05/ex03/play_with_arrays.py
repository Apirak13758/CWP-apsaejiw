array = [2, 8, 9, 48, 8, 22, -12, 2]
print(array)

new_array = {array[i] + 2 for i in range(len(array)) if array[i] > 5}
print(new_array)
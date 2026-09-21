array = [2, 8, 9, 48, 8, 22, -12, 2]
new_array = []
dict = {}
final_array = []
for i in range(len(array)):
    if array[i] + 2 > 5:
        new_array.append(array[i] + 2)
        dict[array[i] + 2] = 0
for key in dict:
    final_array.append(key)
print(array)
print(final_array)
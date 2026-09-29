n = int(input("Enter length: "))
array = []

for i in range(n):
    value = int(input(f"Enter value {i + 1}: "))
    array.append(value)
unique_arr = []
duplicate = False
for i in range(len(array)):
    duplicate = False
    for j in range(len(unique_arr)):
        if array[i]== unique_arr[j]:
            duplicate = True
            break
    if duplicate == False:
        unique_arr.append(array[i])

print("unique array:")
print(unique_arr)
n = int(input("Enter length: "))
array = []

for i in range(n):
    value = int(input(f"Enter value {i + 1}: "))
    array.append(value)
    
for i in range(len(array)):
    if array[i] == 0:
        for j in range(i, len(array) - 1):
            array[j] = array[j+1]
        array[-1] = 0
        
print(array)
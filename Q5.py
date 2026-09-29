# Simple beginner program to reverse an array

n = int(input("Enter length: "))
array = []

for i in range(n):
    value = int(input(f"Enter value {i + 1}: "))
    array.append(value)

reversed_array = []
for i in range(len(array) - 1, -1, -1):
        reversed_array.append(array[i])
        
print("Original array:", array)
print("Reversed array:", reversed_array)
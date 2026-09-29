n = int(input("Enter length: "))
array = []
for i in range(n):
    array.append(int(input(f"Enter value  {i + 1}: ")))
    
print(array)
array.sort()

print(f"Largest element is {array[-1]}")
print(f"smallest element is {array[0]}")
print(f"second smallest element is {array[1]}")
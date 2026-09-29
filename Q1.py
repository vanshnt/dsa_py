n = int(input("Enter length"))
array = []
for i in range(n):
    array.append(int(input(f"Enter value  {i + 1}: ")))
sum = 0
for i in range(n):
    sum += array[i]
    
print(sum)
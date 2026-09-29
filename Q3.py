# Count Even and Odd Numbers: Write a program to accept N integers into
# an array and count and display the number of even and odd elements
# present in the array.


n = int(input("Enter length: "))
array = []
for i in range(n):
    array.append(int(input(f"Enter value  {i + 1}: ")))

odd = 0
even = 0
for i in range(n):
    if array[i]%2 ==0:
        even += 1
    else:
        odd +=1

print(f"There are {odd} odd numbers and {even} even numbers in array")
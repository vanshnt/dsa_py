# Search an Element: Write a program to accept N integers into an array and
# search for a given number. Display an appropriate message indicating
# whether the number is present in the array or not and also display its
# position.

n = int(input("Enter length: "))
array = []
for i in range(n):
    array.append(int(input(f"Enter value  {i + 1}: ")))

num = int(input("Enter a number to search: "))

for i in range(n):
    if array[i] == num:
        print(f"{num} found on {i+1} index")
        break
    else:
        print("Number not found")
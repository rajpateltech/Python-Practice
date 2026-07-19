# Input from user
n = int(input("Enter a number to calculate its factorial: "))   
factorial = 1
print(f"Calculating factorial of {n}")
for i in range(1, n):
    factorial *= i
    print(f"The factorial of {i} is: {factorial}")
# print(f"The factorial of{i} is: {factorial} ")
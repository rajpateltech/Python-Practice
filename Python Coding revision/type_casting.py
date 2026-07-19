# Type casting and type conversion

age = "25"
print(type(age),age)
print((age))
age = int(age)
# Convert String to integer int
num="100"
print(int(num))

a = int("10")
b = int("20")
print(a+b)  # Output: 30

# Convert String to Float float
price = "99.99"
print(float(price)) # Output: 99.99

num = float("25")
print(num)

# Convert Number to String str
age = 25
print(str(age)) # Output: "25"

name = "Age:" + str(25)
print(name) # Output: Age: 25

# Convert integer to Float
num = 10
print(float(num))

# Convert Float to Integer
num = 9.8
print(int(num))

# Convert to Boolean bool
print(bool(1)) # Output: True
print(bool(0)) # Output: False

# Type Casting User Input
age = input("Enter age: ")
print(type(age)) # Output: <class 'str'>

# Invalid Type Conversion
num = "hello"
print(int(num)) # Output: Error: ValueError

# Check Type After Conversion
num = int("50")
print(type(num)) # Output: <class 'int'>

# Practice Examples
# Add two string numbers
a = "10"
b = "20"
print(int(a) + int(b)) # Output: 30

# Convert integer to string
score = 100
print("Score:"+ str(score)) # Output: Score:100

# Convert flaot to integer
price = 49.99
print(int(price)) # Output: 49

# Homework
# how to find ascii value of '25'
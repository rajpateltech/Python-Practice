# Practice Problem 1: Write a Python function that accepts two integer numbers. 
# If the product of the two numbers is less than or equal to 1000,
# return their product; otherwise, return their sum.
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# product = num1 * num2
# if ( product<= 1000):
#     print(f"The product of {num1} and {num2} is: {product}")
# else:
#     print(f"The sum is: {num1 + num2}")

# Function to calculate product or sum based on the condition
def calculate_product_or_sum(num1, num2):
    product = num1 * num2
    if product <= 1000:
        return product
    else:
        return num1 + num2
# Testing the function
result1 = calculate_product_or_sum(20, 30)
result2 = calculate_product_or_sum(50, 30)
print(f"Result for (20, 30): {result1}")  # Output: 600
print(f"Result for (50, 30): {result2}")  # Output: 80

def factorial(n):
    # Base case: if n is 1, return 1
    if n == 1:
        return 1
    else:
        # Recursive case: n * factorial of (n-1)
        return n * factorial(n - 1)

# Testing the factorial function
result1 = factorial(5)  # 5! = 120
result2 = factorial(7)  # 7! = 5040
print(f"Factorial of 5 is: {result1}")  # Output: 120
print(f"Factorial of 7 is: {result2}")  # Output: 5040

print(f"Factorial of 9 is: {factorial(9)}")  # Output: 362880
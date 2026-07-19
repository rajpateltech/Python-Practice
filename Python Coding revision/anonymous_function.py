# An anonymous function is a function that is defined without a name.
# In Python, anonymous functions are defined using the lambda keyword. Hence, anonymous functions are also called lambda function.
# A lambda function can take any number of arguments, but can only have one expression. The expression is evaluated and returned.
# Syntax of lambda function: lambda arguments: expression
# Comparsion of normal function and lambda function

# Normal Function
def add(x, y):
    return x + y
print(add(5, 3))  # Output: 8

# Lambda Function
add_lambda = lambda x, y: x + y
print(add_lambda(5, 3))  # Output: 8
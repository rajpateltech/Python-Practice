s = "hello world"
print(s.upper()) # Convert to uppercase
print(s.capitalize()) # Convert first letter into capital
print(s.lower()) # Convert to lowercase
print(s.title()) # Capitalize first letter of each word
print(" hello ".strip()) # Remove leading/trailing spaces
print(s.replace("world","Python")) # "hello Python"
print(s.split()) # split into list

# Important for reversing 
print(" ".join(["Python","is","fun"])) # Join list into string

print(s.find("o")) # Find first occurrence
print(s.startswith("hello")) # Check prefix
print(s.endswith("world")) # Check suffix
print(type(s))

# Bonus tips: Use in to check if a substring exists -> "Python" in s 

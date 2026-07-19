# List (ordered & Mutable)
# Supports indexing and slicing
# Common methods: append(), remove(), pop(), sort()

my_list = [1,2,3,"apple"] # appends adds in the last
my_list.append("banana") 
print(my_list[2])
print(my_list)

# Tuple ( Ordered & Immutable means not changable )
# Cannot be changed after creation
# Common methods: append(), remove(), pop(), sort()

my_tuple = (10,20,30)
print(my_tuple[1]) # Output: 20

# Dictionary (key-value Pairs)
# keys are unique, fast for lookups & mutable and dynamic
student ={"name": "Amit", "age": 21}
print(student["name"]) # Output: Amit
print(student)
student["age"] = 22
print(student)

# Set (Unordered & Unique)
# No duplicates allowed
# Useful for set operations: union, intersection

nums = {1,2,3,2}
print(nums) # Output: {1,2,3}

# Use:
# List: Ordered collection
# Dict: Mapping data
# Set: Unique elements
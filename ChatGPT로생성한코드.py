# Lists, Tuples, Sets, and Dicts Comparison Demo

# Lists
my_list = [1, 2, 3, 4, 4]

# Tuples
my_tuple = (1, 2, 3)

# Sets
my_set = {1, 2, 3, 3}

# Dicts
my_dict = {'a': 1, 'b': 2, 'c': 3}

# List Example
print("List Example:")
print("List:", my_list)
print("First Element:", my_list[0])
print("Supports Duplicates:", len(my_list) != len(set(my_list)))  # Check for duplicates

# Tuple Example
print("\nTuple Example:")
print("Tuple:", my_tuple)
print("First Element:", my_tuple[0])
print("Immutability:", isinstance(my_tuple, tuple))

# Set Example
print("\nSet Example:")
print("Set:", my_set)
print("Uniqueness:", len(my_set) == len(set(my_set)))  # Check for duplicates
print("Fast Membership Test:", 2 in my_set)

# Dict Example
print("\nDict Example:")
print("Dict:", my_dict)
print("Value for 'b':", my_dict['b'])
print("Keys:", my_dict.keys())
print("Key-Value Mapping:", isinstance(my_dict, dict))

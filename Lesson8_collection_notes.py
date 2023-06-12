"""
Sets and Frozensets:

Sets and frozensets are both collections of unique elements.
The main difference between sets and frozensets is that sets are mutable (can be changed), while frozensets are immutable (cannot be changed).

Operations with sets:
- Creating a set: you can create a set using curly braces {} or the set() function.
- Adding elements: you can add elements to a set using the add() method or the update() method.
- Removing elements: you can remove elements from a set using the remove() or discard() method.
- Set operations: you can perform set operations like union, intersection, difference, and symmetric difference using the corresponding methods or operators.
- Operations with frozensets:

Creating a frozenset: you can create a frozenset using the frozenset() function.
Frozensets are immutable, so you cannot add or remove elements from them.
You can perform set operations like union, intersection, difference, and symmetric difference using the corresponding methods or operators.

Dictionary:
A dictionary is a collection of key-value pairs, where each key is unique and corresponds to a value. Dictionaries are mutable and can be changed.

Operations with dictionaries:
- Creating a dictionary: you can create a dictionary using curly braces {} or the dict() function.
- Adding and updating values: you can add or update values to a dictionary by assigning a value to a key using the square bracket notation or the update() method.
- Removing values: you can remove values from a dictionary using the del keyword or the pop() method.
- Dictionary methods: there are several useful methods for working with dictionaries, like keys(), values(), items(), get(), and clear().

Test/Practice:
Create a set with the numbers 1, 2, 3, 4, and 5."""
my_set = {1, 2, 3, 4, 5}
# Add the number 6 to the set.
my_set.add(6)
# Remove the number 3 from the set.
my_set.remove(3)
# Create a frozenset with the numbers 2, 4, 6, and 8.
my_frozenset = frozenset({2, 4, 6, 8})
# Create a dictionary with the keys "apple", "banana", and "cherry", and the values 1, 2, and 3, respectively.
my_dict = {"apple": 1, "banana": 2, "cherry": 3}
# Add a new key-value pair to the dictionary with the key "orange" and the value 4.
my_dict["orange"] = 4
# Remove the key-value pair with the key "banana" from the dictionary.
del my_dict["banana"]
# Use the keys() method to get a list of the keys in the dictionary.
my_dict.keys()


# Collection:
# The collections module in Python provides alternative implementations for several built-in container types like list, tuple, and dict.
# The collections module also provides some additional container types like defaultdict, Counter, namedtuple, and deque.

# Args:
# args is a special syntax in Python that allows a function to accept a variable number of arguments. *args is used to pass a variable number of arguments to a function.
# The arguments passed with *args are treated as a tuple inside the function.

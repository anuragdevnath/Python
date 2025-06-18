# Attempting to create a set with different types of elements
s = {8, 7, 6, "Anurag", [1, 2]}  

# This will raise an error:
# TypeError: unhashable type: 'list'
# Because sets can only contain hashable (i.e., immutable) objects.
# Lists are mutable and therefore not allowed in a set.

print(type(s))  # This line won't execute due to the error above

# Creating a valid set with integers, a string, and a tuple
s = {8, 7, 6, "Anurag", (1, 2)}  # Tuple (1, 2) is immutable and hashable

# Now the set is valid and can be created without error
print(type(s))  # Output: <class 'set'>

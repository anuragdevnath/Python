# Create a set with some duplicate integers and a string
my_set = {1, 2, 3, 3, 4, "Anurag"}  # '3' will be stored only once

# Another set with different integers and a string
my_set2 = {12, 25, 31, 2, 36, 41, "Nisha"}  # '2' is common with my_set

# union() returns a new set containing all elements from both sets (removes duplicates)
print(my_set.union(my_set2))  
# Output: {1, 2, 3, 4, 36, 41, 12, 25, 31, 'Nisha', 'Anurag'}

# intersection() returns a new set with elements common to both sets
print(my_set.intersection(my_set2))  
# Output: {2}

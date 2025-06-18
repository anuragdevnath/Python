# ❌ Avoid using 'set' as a variable name — it shadows the built-in set() function
my_set = {1, 2, 3, 3, 4, "Anurag"}  # Duplicates (3) are automatically removed

# Adding a new element "Nisha" to the set
my_set.add("Nisha")

# Print the length of the set (number of unique elements)
print(len(my_set))  # Output: 6 (1, 2, 3, 4, "Anurag", "Nisha")

# Remove the element "Anurag" from the set
# .remove() removes the item, but returns None — trying to print it will show 'None'
print(my_set.remove("Anurag"))  # Output: None, but "Anurag" is removed

# .pop() removes and returns an arbitrary element (since sets are unordered)
my_set.pop()

# ⚠️ Now you're trying to call `set()` — but you previously overwrote `set` as a variable
# So `set()` now tries to "call" your `my_set` set, which is not callable → TypeError
# To fix this, we avoid using `set` as a variable name earlier.

print(set())  # ❌ This would throw: TypeError: 'set' object is not callable

# Clear all elements from the set
print(my_set.clear())  # Output: None (set is emptied)

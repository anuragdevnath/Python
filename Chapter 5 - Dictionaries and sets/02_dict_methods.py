# Creating a dictionary to store student names as keys and their marks as values
marks = {
    "Anurag": 34,
    "Ashu": 24,
    "Krishna": 44
}

# Printing the entire dictionary and its type (which is <class 'dict'>)
print(marks, type(marks))  

# .items() returns a view object containing the key-value pairs of the dictionary
print(marks.items())  # Output: dict_items([('Anurag', 34), ('Ashu', 24), ('Krishna', 44)])

# .keys() returns a view object of all the keys in the dictionary
print(marks.keys())   # Output: dict_keys(['Anurag', 'Ashu', 'Krishna'])

# .values() returns a view object of all the values in the dictionary
print(marks.values()) # Output: dict_values([34, 24, 44])

# .update() is used to modify the dictionary:
# - If the key exists (e.g., "Anurag"), its value will be updated (from 34 to 35)
# - If the key doesn't exist (e.g., "Nisha"), it will be added as a new key-value pair
marks.update({"Anurag": 35, "Nisha": 36})

# After the update, print the modified dictionary items
print(marks.items())  # Output: dict_items([('Anurag', 35), ('Ashu', 24), ('Krishna', 44), ('Nisha', 36)])

# .get() is a safe way to retrieve a value for a given key
# Returns None if the key is not found, instead of raising an error
print(marks.get("Anurag"))  # Output: 35

# Direct access using square brackets [] also retrieves the value
# BUT it raises a KeyError if the key is not found
print(marks["Anurag"])      # Output: 35

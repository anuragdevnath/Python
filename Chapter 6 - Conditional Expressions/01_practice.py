# Taking the first number as input from the user and storing it
num1 = int(input("Enter a number: "))

# Assume the first number is the greatest for now
greater = num1

# Take second number and compare it with the current greatest
num2 = int(input("Enter another number: "))
if greater < num2:
    greater = num2  # Update if num2 is greater

# Take third number and compare it
num3 = int(input("Enter another number: "))
if greater < num3:
    greater = num3  # Update if num3 is greater

# Take fourth number and compare it
num4 = int(input("Enter another number: "))
if greater < num4:
    greater = num4  # Update if num4 is greater

# 📝 Alternative method (commented out):
"""
numlist = [num1, num2, num3, num4]  # Create a list of all numbers
numlist.sort()                      # Sort the list in ascending order
greater = numlist[3]                # The last element is the greatest
"""

# Finally, print the greatest number
print(greater)

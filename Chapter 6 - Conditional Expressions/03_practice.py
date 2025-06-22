# Take user input for a comment
main_string = str(input("Enter a comment: "))

# Define spam keywords to check for
substring1 = "Make a lot of money"
substring2 = "Buy now"
substring3 = "subscribe this"
substring4 = "click this"

# Check if any of the spam keywords exist in the input
if substring1 in main_string:
    print("Spam found!")
elif substring2 in main_string:
    print("Spam found!")
elif substring3 in main_string:
    print("Spam found!")
elif substring4 in main_string:
    print("Spam found!")
else:
    print("Valid comment.") 

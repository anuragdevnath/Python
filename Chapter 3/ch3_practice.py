# Write a Python programme to display a user enter name followed by good afternoon using input function

uName = input("Enter Your name")
msg = f"Hello {uName} , Good Afternoon"
print(msg)

# Write a python programme to fill in a letter template given below with name and date

from datetime import date

today = date.today()

letter = f"""
Dear {uName}
You are selected!
{today}
"""
print(letter)

# write the programme to detect double space in a string
uStr = input("Enter dtring with double space: ")
print(uStr.find("  "))

#replace double space with single space
print(uStr.replace("  "," "))

#Escape sequence practice
seq_str = "Dear Anurag, \nthis Python Course is nice.\nthanks!"
print(seq_str)


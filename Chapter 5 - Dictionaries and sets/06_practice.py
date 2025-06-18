# Dictionary storing English-to-Hindi word translations
words = {
    "Hello": "Namaste",
    "Thankyou": "Shukriya",
    "Fruits": "Fal"
}

# Prompt the user to enter a word to translate
uWord = str(input("Enter the word: "))

# Use .get() to safely fetch the translation from the dictionary
# If the word doesn't exist, it returns 'None' instead of raising an error
print(words.get(uWord))

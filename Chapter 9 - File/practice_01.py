with open("d:/Code/Python/Chapter 9 - File/poem.txt", "r") as f:
    data = f.read()
    if "twinkle" in data:
        print("twinkle is present in the file")
    else:
        print("twinkle is not present in the file")
import os
print(os.getcwd())
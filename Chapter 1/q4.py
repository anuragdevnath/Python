import os

# Specify the path (use "." for current directory)
path = "/"

# List and print all files and directories
for item in os.listdir(path):
    print(item)

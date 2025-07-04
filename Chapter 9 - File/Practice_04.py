with open("Chapter 9 - File/paragraph.txt","r") as f:
    data = f.read()
    data = data.replace("donkey","######")
    with open("Chapter 9 - File/paragraph.txt","w") as f:
        f.write(data)

print("Done")
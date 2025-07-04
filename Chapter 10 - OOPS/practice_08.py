# Create a class Book with private attributes (e.g., __title, __author) and methods to get and set them.

class book:
    def __init__(self,title="The ultimate pranks",author="Mistry"):
        self.title=title
        self.author=author
    
    def setTitle(self):
        self.title=str(input("Enter title: "))
        self.author=str(input("Enter author: "))
    
    def getTitle(self):
        print(f"The title of book is {self.title}")
        print(f"The author of book is {self.author}")

bookObj = book()
# bookObj.setTitle()
bookObj.getTitle()
# Create a class called Person that takes name and age as arguments and has a method to display them.

class Person:
    def __init__(self):
        self.name = "Mistry"
        self.age = 45
    
    def displayData(self,name,age):
        print(f"Hello My name is {self.name} and my age is {self.age}")

classObj = Person()
classObj.displayData("Anurag",22)


class programmer:
    company = "Microsoft"
    def __init__(self,name,age,language):
        self.name = name
        self.age = age
        self.language = language

    def getInfo(self):
        print(f"The name of the programmer is {self.name}, the age is {self.age} and the language is {self.language}")


p1 = programmer("Anurag",20,"Python")
p1.getInfo()
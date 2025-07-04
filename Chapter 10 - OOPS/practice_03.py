class Practice:
    a = 1
    def __init__(self, a):  # Accept 'a' during object creation
        self.a = a

    def printObject(self):
        return self.a

classObj = Practice(0)
print(classObj.printObject())
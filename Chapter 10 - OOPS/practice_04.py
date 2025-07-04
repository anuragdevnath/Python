import math

class Calculator:
    def __init__(self, number):
        self.number = number

    def square(self):
        return self.number ** 2

    def cube(self):
        return self.number ** 3

    def sq_root(self):
        return math.sqrt(self.number)
    
    @staticmethod
    def greet():
        return "Hello there!"

# Example usage
test = Calculator(2)
print(test.greet())
print("Square:", test.square())
print("Cube:", test.cube())
print("Square root:", test.sq_root())

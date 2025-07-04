# Create a Circle class that takes radius and provides methods to calculate:

# Area

# Circumference
import math

class Circle:
    def __init__(self, radius=20):
        self.radius = radius  # default radius is 20 if not provided

    def area(self):
        area = math.pi * (self.radius ** 2)
        return f"{area:.2f} cm²"
    
    def circumference(self):
        circum = 2 * math.pi * self.radius
        return f"{circum:.2f} cm"

# Example usage:
circleObj = Circle(25)  # sets radius to 25
print(circleObj.area())        # → uses self.radius
print(circleObj.circumference())

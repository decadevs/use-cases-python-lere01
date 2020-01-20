# Document at least 3 use cases of static methods

"""
Static methods do not take the 'self' or 'cls' parameters although they can take any number of arguments.
They cannot modify object or class state except when called by class or instance methods. In this wise, 
they can be called helper functions which is one way to use them. However, they are primarily a way to 
namespace methods
"""

# A class of circles
class Cirlce:
    def __init__(self, radius, circumference = 0, area = 0):
        self.radius = radius
        self.area = area
        self.circumference = circumference

    def calculate_area(self):
        self.area = (2 * math.pi) * (self.radius ** 2)
        return self.area

    def calculate_circumference(self):
        self.circumference = (2 * math.pi) * self.calculate_diameter(self.radius)
        return self.circumference
        
    @staticmethod
    def calculate_diameter(radius):
        return 2 * radius
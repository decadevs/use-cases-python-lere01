# Document at least 3 use cases of instance methods

"""
Instance methods are methods that are which are called on the object (instance) of a class. Through
the 'self' parameter, they have access to all attributes and other methods on the same object. Hence,
class methods can modify the said attributes. The instance methods are used most of the time.

Note: Like 'cls', 'self' is a convention. You might as well use 'jackass' as long as it is the first 
parameter/argument of the method
"""
import math

# a class of Vehicles
class Vehicle:
    def __init__(self, maker, model, year, color):
        self.maker = maker
        self.model = model
        self.year = year
        self.color = color

    def display_details(self):
        return 'Make: {}, Model: {}, Year: {}, Colour: {}'.format(self.maker, self.model, self.year, self.color)


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
        self.circumference = (2 * math.pi) * (2 * self.radius)
        return self.circumference
        

# A class of trousers
class Trousers:
    def __init__(self, waist_size, length, color):
        self.waist_size = waist_size
        self.length = length
        self.color = color

    def details(self):
        return "Waist Size: {}, Length: {}, Colour: {}".format(self.waist_size, self.length, self.color)



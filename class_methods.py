# Document at least 3 use cases of class methods

"""
Class methods do not depend on the instance of the class - they take in a parameter, 'cls'
which points to the class not the object instance whenever the method is called. The consequence 
of this is that class methods cannot modify instance states since that would require access to 'self'
which they do not have. They can only modify class states.

One application of class methods is to use them as factory functions alternate constructors. They can 
also be used in situations when some methods may need to run before an instance of the class is created.

Note: Like 'self', 'cls' is a convention. You might as well use 'jackass' as long as it is the first 
parameter/argument of the method
"""

# A class of 300 Level Students in a physics department
class ThreeHundredLevel:
    compulsory_courses = []
    lecture_venue = ''
    laboratory = ''

    def __init__(self, name, matric_no, electives = []):
        self.name = name
        self.matric_no = matric_no
        self.electives = electives

    def details(self):
        return 'Name: {}, Matric No: {}'.format(self.name, self.matric_no)

    @classmethod
    def compulsory_courses(cls):
        return cls.compulsory_courses

    @classmethod
    def venues(cls):
        return 'Lecture Venue: {}, Laboratory: {}'.format(cls.lecture_venue, cls.laboratory)


# A class of televisions
class Television:
    off_state = True

    def __init__(self, maker, color, size, display_type):
        self.maker = maker
        self.color = color
        self.size = size
        self.display_type = display_type

    @classmethod
    def television_is_off(cls):
        return cls.off_state


# A class of animals
class Animal:
    def __init__(self, name, species, classification):
        self.name = name
        self.category = classification
        self.species = species

    @classmethod
    def create_dog(cls):
        return cls('Dog', 'German Shepherd', 'Mammal')




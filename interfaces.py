# Document 1 use case of an interface in python
# That is define an interface using the abstract base class module
# Add at least 3 entities that can implement the interface in a way that make sense.

from abc import ABC, abstractmethod

# an interface for file opening objects
class ModuleInterface(ABC):
    @abstractmethod
    def read_all_lines(self):
        pass

    @abstractmethod
    def read_first_two_lines(self):
        pass

    @abstractmethod
    def read_last_two_lines(self):
        pass


# a class of tsv file objects inheriting from the ModuleInterface
class TSVFile(ModuleInterface):
    def __init__(self, filename, mode='r'):
        self.filename = filename

    def read_all_lines(self):
        with open(self.filename) as fd:
            csvreader = csv.reader(fd, delimiter = '\t')
            return list((line for line in csvreader))

    def read_first_two_lines(self):
        with open(self.filename) as fd:
            csvreader = csv.reader(fd, delimiter = '\t')
            return list((line for line in csvreader))[:2]


    def read_last_two_lines(self):
        with open(self.filename) as fd:
            csvreader = csv.reader(fd, delimiter = '\t')
            return list((line for line in csvreader))[-2:]



# a class of csv file objects from the ModuleInterface
class CSVFile(ModuleInterface):
    def __init__(self, filename, mode='r'):
        self.filename = filename

    def read_all_lines(self):
        with open(self.filename) as fd:
            csvreader = csv.reader(fd)
            return list((line for line in csvreader))

    def read_first_two_lines(self):
        with open(self.filename) as fd:
            csvreader = csv.reader(fd)
            return list((line for line in csvreader))[:2]


    def read_last_two_lines(self):
        with open(self.filename) as fd:
            csvreader = csv.reader(fd)
            return list((line for line in csvreader))[-2:]



# a class of txt file objects from the ModuleInterface
class TextFile(ModuleInterface):
    def __init__(self, filename, mode='r'):
        self.filename = filename

    def read_all_lines(self):
        with open(self.filename) as fd:
            return list((line.rstrip() for line in fd))

    def read_first_two_lines(self):
        with open(self.filename) as fd:
            return list((line.rstrip() for line in fd))[:2]


    def read_last_two_lines(self):
        with open(self.filename) as fd:
            return list((line.rstrip() for line in fd))[-2:]
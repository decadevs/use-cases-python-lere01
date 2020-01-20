# Document at least 3 use cases of iterators

"""
An Iterator is an object which contains a countable number of values i.e. it can be iterated upon. In technical
terms, an iterator is an object which implements the itertor protocol. The iterator protocol consists of the __iter__()
and __next__() methods.
"""

class Fibonacci():
    def __init__(self, num):
        self.num = num
        self.count = 0
        self.values = []
 
    def __iter__(self):
        return self
 
    def next(self):
        self.count += 1
        if self.count > self.num:
            raise StopIteration
 
        if len(self.values) < 2:
            self.values.append(1)
        else:
            self.values = [self.values[-1], self.values[-1] + self.values[-2]]
        return self.values[-1] 



class MultiplesOfThree:
    def __init__(self, number=0):
        self.number = number

    def __iter__(self):
        self.num = 1
        return self
           
    def __next__(self):
        result = 3 * self.num
        self.num += 1
        return result



class MyNumbers:
  def __iter__(self):
    self.starter = 1
    return self

  def __next__(self):
    if self.starter <= 20:
      result = self.starter
      self.starter += 1
      return result
    else:
      raise StopIteration

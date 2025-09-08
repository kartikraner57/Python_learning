from abc import *   # Importing everything from the 'abc' module (Abstract Base Classes)

class Test:         # Defining a normal class named 'Test'
    @abstractmethod # This is a decorator that marks 'm1' as an abstract method
    def m1(self):   # Declaring a method 'm1'
        pass        # Empty body (no implementation)

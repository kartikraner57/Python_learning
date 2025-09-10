from abc import *   # Import everything from abc module (Abstract Base Classes)

class Test:         # Define a normal class 'Test'
    pass            # 'pass' means "do nothing", an empty class

t = Test()          # Create an object of Tes
try:
    x = int(input("Enter First Number: "))
    y = int(input("Enter Second Number: "))
    print(x / y)
except ZeroDivisionError:
    print("ZeroDivisionError")
except ArithmeticError:
    print("ArithmeticError")

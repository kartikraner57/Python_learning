########## 3) pass statement:  pass is a keyword in Python. 
#  In our programming syntactically if block is required which won't do anything then we can define that empty block with pass keyword.
##########pass=> |- It is an empty statement |- It is null statement |- It won't do anything
######## pass satment acts as empty stament acts as aplace for future implimentation
# class A:
#     pass
# class B:
#     pass
# class C:
#     pass

# pass stament in python'

# pass Statement in Python
# The pass statement in Python is a placeholder that does nothing when executed. It is useful when you need to write code but don’t want to implement logic yet.

# Usage of pass
# Inside Loops: When you want to create a loop structure but haven't written the logic yet.

# Inside Functions: When defining a function that you will implement later.

# Inside Classes: When defining a class without any methods for now.

# Inside Conditional Statements: When you want to write conditions but haven't decided on the implementation.



# x = 100
# if x >10:
#     print("success")

# for i in range(100): 
#     if i%9==0: 
#         print(i)
#     else:pass
# x = int(input("enter marks :"))
# if x >= 35:
#     print("success")
# else :
#     pass


# x = int(input("enter marks :"))
# if x >= 35:
#     print("success")
# else :
#     print("fail")



# class abc import *
# class loan(ABC):
#     @abstractmethod
#     def getInterestRate(self):
#         pass
# class homeLoan(loan):
#     def getInterestRate(self):
#         return 8
# class vehicleLoan(loan):
#     def getInterestRate(self):
#         return 11
# h = homeLoan()
# print(h.getInterestRate())  # Output: 8

from abc import ABC, abstractmethod

class Loan(ABC):
    @abstractmethod
    def getInterestRate(self):
        pass

class HomeLoan(Loan):
    def getInterestRate(self):
        return 8

class VehicleLoan(Loan):
    def getInterestRate(self):
        return 11

h = HomeLoan()
print(h.getInterestRate())  

v = VehicleLoan()
print(v.getInterestRate())  
################Use Case of pass: Sometimes in the parent class we have to declare a function with empty body and child class responsible 
# to provide proper implementation. Such type of empty body we can define by using pass keyword.
#  (It is something like abstract method in Java)
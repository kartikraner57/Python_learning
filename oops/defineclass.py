
# #### How to define a Class?

# class Student:
#     ''' This is student class with required data '''

# print(Student.__doc__)   # Prints the docstring
# help(Student)            # Shows the class documentation


# class student:
#     ''' This class developed by Durga for demo purpose '''
#     def __init__(self):  # Corrected constructor
#         self.name = "durga"
#         self.rollno = 101
#         self.marks = 90
#     def talk(self):
#         print("Hello, my name is:", self.name)
#         print("My rollno is:", self.rollno)  # Fixed typo here
#         print("My marks are:", self.marks)
# s = student()
# print(s.name)
# print(s.rollno)
# print(s.marks)
# s.talk()


# class Test :
#  def __init__(self):
#     print("the address of object pointed by self :",id(self))
# t = Test()
# print("the adrres of objrct pointed by  t: ", id(t))



# print("add the number")  # This line will be printed




class Student:
    '''Developed by Durga for Python demo'''

    def __init__(self):
        self.name = 'durga'
        self.age = 40
        self.marks = 80

    def talk(self):
        print("Hello I am:", self.name)
        print("My Age is:", self.age)
        print("My Marks are:", self.marks)

class Test:
    def __init__(self):
        print("Constructor execution...")

    def m1(self):
        print("Method execution...")

# Creating objects
t1 = Test()
t2 = Test()
t3 = Test()

# Calling method on one object
t1.m1()
t.__dict__ = {'a': 10, 'b': 20}


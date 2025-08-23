
# # class Outer:
# #     def __init__(self):
# #         print("outer class object creation")

# #     class Inner:
# #         def __init__(self):
# #             print("inner class object creation")

# #         def m1(self):
# #             print("inner class method")

# # # o = Outer()        # creates outer class object
# # # i = o.Inner()      # creates inner class object
# # # i.m1()             # calls method of inner class
# # # o = Outer().Inner().m1

# class Person:
#     def __init__(self):
#         self.name = 'durga'
#         self.db = self.Dob()   # creating object of inner class

#     def display(self):
#         print('Name:', self.name)
#         self.db.display()      # also display Dob details

#     class Dob:
#         def __init__(self):
#             self.dd = 10
#             self.mm = 5
#             self.yy = 1947

#         def display(self):
#             print("dob={}/{}/{}".format(self.dd, self.mm, self.yy))


# # create object of Person and call display
# p = Person()
# p.display()

# # if you want to create inner class object separately
# d = Person.Dob()
# d.display()

class Human:
    def __init__(self):
        self.name = 'Sunny'
        self.head = self.Head()     # inner class Head object
        self.brain = self.Brain()   # inner class Brain object

    def display(self):
        print("Hello..", self.name)

    class Head:
        def talk(self):
            print('Talking...')

    class Brain:
        def think(self):
            print('Thinking...')


# create Human object
h = Human()
h.display()
h.head.talk()
h.brain.think()

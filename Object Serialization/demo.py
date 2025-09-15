# import pickle

# class Employee:
#     def __init__(self, eno, ename, esal, eaddr):
#         self.eno = eno
#         self.ename = ename
#         self.esal = esal
#         self.eaddr = eaddr

#     def display(self):
#         print('ENO:{}, ENAME:{}, ESAL:{}, EADDR:{}'.format(
#             self.eno, self.ename, self.esal, self.eaddr
#         ))

# # Creating object
# e = Employee(100, 'Durga', 1000, 'Hyderabad')

# # Writing object to file (pickling)
# with open('emp.dat', 'wb') as f:
#     pickle.dump(e, f)

# print('Pickling of Employee object completed')
# import pickle

# with open('emp.dat', 'rb') as f:
#     obj = pickle.load(f)

# obj.display()
import pickle

class Employee:
    def __init__(self, eno, ename, esal, eaddr):
        self.eno = eno
        self.ename = ename
        self.esal = esal
        self.eaddr = eaddr

    def display(self):
        print('ENO:{}, ENAME:{}, ESAL:{}, EADDR:{}'.format(
            self.eno, self.ename, self.esal, self.eaddr
        ))

# Creating object
e = Employee(100, 'Durga', 1000, 'Hyderabad')

# Writing object to file (pickling)
with open('emp.dat', 'wb') as f:
    pickle.dump(e, f)

print('Pickling of Employee object completed')

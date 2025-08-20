class Student:
    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setMarks(self, marks):
        self.marks = marks

    def getMarks(self):
        return self.marks


# Main program
n = int(input('Enter number of students: '))
for i in range(n):
    s = Student()
    name = input('Enter Name: ')
    s.setName(name)
    marks = int(input('Enter Marks: '))
    s.setMarks(marks)

    print('Hi', s.getName())
    print('Your Marks are:', s.getMarks())
    print(
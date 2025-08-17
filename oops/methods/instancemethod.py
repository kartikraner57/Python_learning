class student :
    def __init__(self,name,marks):
        self.name=name 
        self.marks=marks
    def display(self):
        print("hi",self.name)
        print("hi",self.marks)
    def grade(self):
        if self.marks >= 60:
            print("you got first grade ")
        elif self.marks>50:
            print("your got second grade")
        elif self.marks>35:
            print("you got third 7grade")
        else:
            print("you are faild")
n = int(input("enter number of student :   "))
for i in range(n):
    name = input("enter name :")
    marks= int(input("enter the marks : "))
    s = student(name,marks)
    s.display()
    s.grade()
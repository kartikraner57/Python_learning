class Book:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        return self.pages + other.pages

b1 = Book(100)
b2 = Book(200)
print('The Total Number of Pages:', b1 + b2)











class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __gt__(self, other):
        return self.marks > other.marks

    def __le__(self, other):
        return self.marks <= other.marks

print("10>20 =", 10 > 20)
s1 = Student("Durga", 100)
s2 = Student("Ravi", 200)
print("s1>s2 =", s1 > s2)
print("s1<s2 =", s1 < s2)
print("s1<=s2 =", s1 <= s2)
print("s1>=s2 =", s1 >= s2)

# global variable
a = 10  # global variable

def f1():
    print(a)

def f2():
    print(a)

f1()
f2()

# 2) Local Variables:
def f1():
    a = 10
    print(a)  # valid

def f2():
    print(a)  # invalid

f1()
f2()

# 3)global Keyword:


a = 10  # global variable

def f1():
    a = 777  # local variable
    print(a)  # prints local 'a'

def f2():
    print(a)  # prints global 'a'

f1()
f2()


# Lambda Function:
s = lambda n: n * n
print("The Square of 4 is:", s(4))
print("The Square of 5 is:", s(5))
# Q) Write a Program to create a Lambda Function to find Square of given Number?
s = lambda a, b: a + b
print("The Sum of 10, 20 is:", s(10, 20))
print("The Sum of 100, 200 is:", s(100, 200))
a
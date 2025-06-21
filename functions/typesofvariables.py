# global variable
a = 10  # global variable

def f1():
    print(a)

def f2():
    print(a)

f1()
f2()

# Local Variables
def f1():
    a = 10
    print(a)  # valid

def f2():
    print(a)  # invalid

f1()
f2()

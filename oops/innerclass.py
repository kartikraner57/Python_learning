
class Outer:
    def __init__(self):
        print("outer class object creation")

    class Inner:
        def __init__(self):
            print("inner class object creation")

        def m1(self):
            print("inner class method")

# o = Outer()        # creates outer class object
# i = o.Inner()      # creates inner class object
# i.m1()             # calls method of inner class
o = Outer().Inner().m1

#### Note: The job of destructor is not to destroy object and it is just to perform clean up activities.
import time

class Test:
    def __init__(self):
        print("Object Initialization...")

    def __del__(self):
        print("Fulfilling Last Wish and performing clean up activities...")

t1 = Test()
t1 = None   # reference removed, object becomes eligible for GC
time.sleep(5)
print("End of application")

import time  

class Test:
    def __init__(self):
        print("Constructor Execution...")

    def __del__(self):
        print("Destructor Execution...")

t1 = Test()   # Line 7 → constructor runs → ref count = 1
t2 = t1       # Line 8 → ref count = 2
t3 = t2       # Line 9 → ref count = 3

del t1        # Line 10 → ref count = 2 (t2, t3 still pointing)
time.sleep(5) # Line 11
print("object not yet destroyed after deleting t1")  # Line 12

del t2        # Line 13 → ref count = 1 (only t3 pointing)
time.sleep(5) # Line 14
print("object not yet destroyed even after deleting t2")  # Line 15

print("I am trying to delete last reference variable...")  # Line 16
del t3        # Line 17 → ref count = 0 → eligible for GC






import time  

class Test:
    def __init__(self):
        print("Constructor Execution...")

    def __del__(self):
        print("Destructor Execution...")

list = [Test(), Test(), Test()]   # Line 7
del list                           # Line 8
time.sleep(5)                      # Line 9
print("End of application")        # Line 10

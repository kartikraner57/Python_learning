##########   del statment
######del Statement:-  del is a keyword in Python.
#   After using a variable, it is highly recommended to delete that variable if it is no longer required,
# so that the corresponding object is eligible for Garbage Collection.  We can delete variable by using del keyword.

# x = 10
# print(x)  # Output: 10
# del x
# print(x)  # # Output: NameError: name 'x' is not defined
#  The above code will throw an error because we have deleted the variable x.

# x = 10
# print(x)  # Output: 10
# del x


# s1 ="durga"
# s2 = s1
# s3 = s2
# del s1
# print(s2)  # Output: durga
# print(s3)  # Output: durga
# del s2 , s3

########  del vs immutable object   and dev none
#Note: We can delete variables which are pointing to immutable objects.But we cannot delete the elements present inside immutable object.
# s = "durga"
# del s
# print(s) # Output: NameError: name 's' is not defined

s = "durga"
s = None
print(s) 
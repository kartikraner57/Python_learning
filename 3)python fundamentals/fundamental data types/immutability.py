
# #mutable means changable
# #all fundamental data type are changable eg :> int float bool complex str


# x = 10 

# print(id(x))
# x = x+1
# print(id(x))


# x = 10
# y = x
# print(id(x)) #same
# print(id(y)) #same



# y = y + 1
# print(x)
# print(y)
# print(id(x)) #differnt
# print(id(y))  #differnt

a = "durgasoft"
b = "durgasoft"
print(a is b)

#immutable
a = 10
b = 10
c = 10

print(id(a))
print(id(b))
print(id(c))
 
 
# s = "abcba"
# print(s.find('b'))#1
# print(s.find('z'))#-1
# print(s.find('b'))#1


# s="Learning Python is very easy" 
# print(s.find("Python")) #9 
# print(s.find("Java")) # -1 
# print(s.find("r"))#3 
# print(s.rfind("r"))#21


s = 'a b c d e f g h i j b '
print(s.find('B'))
print(s.find('B',3,8))

s ='a,b,c,d e,'
print(s.index('b'))
print(s.index('z'))
print(s.index('b'))
print(s.index('z'))
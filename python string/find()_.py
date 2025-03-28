# s = "abcba"
# print(s.find('b'))#1
# print(s.find('z'))#-1
# print(s.find('b'))#1


# s="Learning Python is very easy" 
# print(s.find("Python")) #9 
# print(s.find("Java")) # -1 
# print(s.find("r"))#3 
# print(s.rfind("r"))#21


s1 = 'a b c d e f g h i j b '
print(s1.find('B'))#-1
print(s1.find('B',3,8))#-1

s ='a,b,c,d e,'
print(s.index('b'))#1

#print(s.index('z'))#value error
print(s.index('b'))#3
print(s.index('b'))#3

#print(s.index('z'))#value eror

######## .find()
# #######3 s.find(substring) Returns index of first occurrence of the given substring. 
# If it is not available then we will get -1.



# s = "abcba"
# print(s.find('b'))#1
# print(s.find('z'))#-1 # not found
# print(s.find('b'))#1 # same as before


# s="Learning Python is very easy" 
# print(s.find("Python")) #9 # first occurrence of "Python"
# print(s.find("Java")) # -1 
# print(s.find("r"))#3 
# print(s.rfind("r"))#21


# mail = input('enter your email id : ')
# try :
#     i = mail.index('@')
#     print('email id contain @ symbol, with is mendotory')
# except ValueError:
#     print('email id dont contain @ symbol')

# s1 = 'a b c d e f g h i j b '
# print(s1.find('B'))#-1
# print(s1.find('B',3,8))#-1

# s ='a,b,c,d e,'
# print(s.index('b'))#1

# #print(s.index('z'))#value error
# print(s.index('b'))#3
# print(s.index('b'))#3

#print(s.index('z'))#value eror




##### Note: By default find() method can search total string. We can also specify the boundaries to search.
# #s.find(substring,bEgin,end) It will always search from bEgin index to end-1 index.
# s="durgaravipavanshiva" 
# print(s.find('a'))#4 
# print(s.find('a',7,15))#10 
# print(s.find('z',7,15))#-1



# #index(): 
# # index() method is exactly same as find() method except that if the specified substring is not available then we will get 'ValueError'
# s="durgaravipavanshiva" 
# print(s.index('a'))#4 
# print(s.index('a',7,15))#10 
## 4) print(s.index('z',7,15))# value error
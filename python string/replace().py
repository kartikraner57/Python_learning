#Replacing a String with another String: 
# s.replace(oldstring, newstring) 
# inside s, every occurrence of old String will be replaced with new String.

# s = "Hello, how are you?"
# print(s.replace("Hello", "Hi"))  # Output: Hi, how are you?

# a = 'ababababa'
# a1 =a.replace('a','b')
# print(a1)  # Output: bbbbbbbb


# l = "Learning Python is very difficult" 
# l1 = l.replace("difficult","easy") 
# print(l1)  # Output: Learning Python is very easy


d = 'durga software soln'
d1 = d.replace('',"")
# print(d1)  # Output: software soln

print('the no of spaces:',d.count(''))  # Output: 
print('the no of spaces :',len(d)-len(d1))

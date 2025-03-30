####Counting substring in the given String:
#  We can find the number of occurrences of substring present in the given string by using count() method.
#  1) s.count(substring)  It will search through out the string. 
# 2) s.count(substring, bEgin, end)  It will search from bEgin index to end-1 index.

# 3) s.count(substring, bEgin, end, maxcount) �

s="abcabcabcabcadda" 
print(s.count('a')) 
print(s.count('ab')) 
print(s.count('a',3,7))
s ='ABBABBABA'
print(s.count('a')) 
print(s.count('bb')) 
print(s.count('bbb'))
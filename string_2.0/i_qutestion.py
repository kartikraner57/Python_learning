###############   Q1) Write a Program To REVERSE content of the given String by using  slice operator?
#### by using slice operator

# input: durga
# output: agrud 
# s = input('Enter Some String to Reverse:') 
# output = s[::-1] 
# print('reverse string',output)


########### Q2) Write a Program To REVERSE content of the given String by using reversed() function?
###### by using reversed() function
# s ='durga'
# r = reversed(s)
# output= ''.join(r)
# print('reverse string',output) # output :agrud

# s ='durga'
# r = reversed(s)
# print(type (r))
# for ch in r:
#     print(ch ,end='') # output : a g r u g d



################# Q3) Write a Program To REVERSE content of the given String by using while loop?
########## by while loop
# s = input('Enter Some String to Reverse:')  # User se ek string input lene ke liye
# output = ''  # Ek empty string banayi jo reversed output store karegi
# i = len(s) - 1  # `i` ko last index par set kiya (string ki length - 1)

# while i >= 0:  # Jab tak `i` zero ya usse bada hai, loop chalta rahega
#     output = output + s[i]  # Har character ko reverse order me add karte jao
#     i = i - 1  # `i` ko ek step peeche le jao

# print(output)  # Final reversed string print karo


######### Q4) Write a Program To REVERSE order of words present in the given string?
# s=input('Enter Some String:') 
# l=s.split() 
# print(l) # ['kanha', 'is', 'the', 'best']
# l1=l[::-1] 
# output=' - '.join(l1) 
# print(output) 

# s=input('Enter Some String:') 
# l=s.split() 
# print(l) # ['kanha', 'is', 'the', 'best']
# l1=l[::-1] 
# print(l1) 

################# Q5) Write a Program To REVERSE internal content of each word? 


# input: 'Durga Software Solutions' 
# output: 'agruD erawtfoS snoituloS' 
# 
# s = "Durga Software Solutions"
# l = s.split()
# print(l) # ['Durga', 'Software', 'Solutions']

# 
# s = "Durga Software Solutions"
# l = s.split()
# l1 = []
# for word in l :
#     l1.append(word[::-1])
# print(l1) # 
# output = ' '.join(l1)
# print(output) # 'agruD erawtfoS snoituloS'





#  
# s=input('Enter Any String:') 
# l=s.split() 
# l1=[] 
# for word in l: 
#   l1.append(word[::-1]) 
# output=' '.join(l1)
# print(output)


############# Q6) Write a Program To REVERSE internal content of every second word present in the given string?
# s = "durgasoft"
# i = 0
# print("charcter preseent at even index is:")
# while i < len(s):
#     print(s[i])
#     i = i + 2
# i = 1
# print("charcter preseent at odd index is:")
# while i < len(s):
#     print(s[i])
#     i = i + 2


# s = "durgasoft"
# print('character present at even index is :',s[: : 2])
# print('character present at odd index is:',s[1 : : 2])

################### Q5) Write a Program To REVERSE internal content of each word? 
# 1) input: 'Durga Software Solutions'
# output: 'agruD erawtfoS snoituloS' 
 
# s=input('Enter Any String:')  
# l=s.split() 
# l1=[] 
# for word in l: 
#     l1.append(word[::-1]) 
# output=' '.join(l1) 
# print(output)

 
# s=input('Enter Any String:')  
# l=s.split() 
# l1=[] 
# for word in l: 
#     l1.append(word[::-1]) 
# output=' '.join(l1) 
# print(output)
 
s=input('Enter Any String:')  
l=s.split() 
l1=[] 
for word in l: 
    l1.append(word[::-1]) 
output=' '.join(l1) 
print(output)
 
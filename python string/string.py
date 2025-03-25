# ch = 'a'
# type(ch)
# print(ch)


# s = """"durga
# software
# solution"""
# print(s)

# #s = 'This is ' single quote symbol' =>Invalid
# s = 'This is \' single quote symbol' #=> Valid
# s = "This is ' single quote symbol" #=> Valid
# s = 'This is " double quotes symbol' #=> Valid
## s = 'The "Python Notes" by 'durga' is very helpful'  => Invalid
## s = "The "Python Notes" by 'durga' is very helpful" => Invalid
## s = 'The \"Python Notes\" by \'durga\' is very helpful'=>Valid
## s = '''The "Python Notes" by 'durga' is very helpful'''=> Valid

# print(s)


# f = '''python "notes" by 'durga' is very good'''
# print(f)
# c = "python notes by 'durga' is very good"
# print(f)
# l = 'python notes by\' "durga" is very good'
# print(l)

############wap to display of given index(both +ve and -ve) of string
#s = input("enter same string :")
# i = 0
# for x in s:
#     print("the character present at +ve index : {} and at -ve index: {} is : {} ".format(i, i-len(s),x))
#     i = i+1
s1 = "a,s,d,f,g,h,j,k"
print(s1[3:6])  # Extracts characters from index 3 to 5 , slice oppertor use
print(s1[3:])  # Extracts characters from index 3 to the end

s="Learning Python is very very easy!!!"
s[1:7:1]# 'earnin' 
print(s[1:7]) #'earnin' 
print(s[1:7:2]) #'eri' 
print(s[:7])#'Learnin' 
print(s[7:]#'g Python is very very easy!!!' 
print(s[::] 13))# 'Learning Python is very very easy!!!' 
s[:] 15) 'Learning Python is very very easy!!!' 16) >>> s[::-1] 17) '!!!ysae yrev yrev si nohtyP gninraeL'
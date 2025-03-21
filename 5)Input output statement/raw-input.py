# 68
#raw_input satment => is use only in python 2.o,it's porvide only string value,
#input satment in python 2.o => its's provide int,float,string value
#input stament in python 3.o => it's porvide only string value,it is similar as raw_input statment .
# x = input('enter same thing :')
# print(type(x)) #=> str

#______________________
# # #69 lecture


# e sum :",j + i)

# x =input("inter first number :")
# y =input("inter second number :")
# i =int(x)
# j =int(y)
# print("the sum :",j + i)


# x = int(input("enter first number :"))
# y = int(input("enter second number :"))
# print("the sum :",x+y)

# print("thesum : ",int(input("enter first number :"))+int(input("enter the 2nd number :")))



###___________________________________________________________________________________________________________
# 6

# my_no = int(input("inter the my number :"))
# my_name = input("interr thee myname :")
# my_address = input("my adrress :")
# my_sallory = float(input("my sallory :"))
# i_marrid = bool(input("are you marrid :"))

# print("your number :",my_no,)
# print("your name :",my_name)
# print("your sallory :",my_sallory)
# print("your addreess :",my_address)
# print(i_marrid,"are marrid :")



########___________________________________________________________________________________________________

#######70
####how to  read multiple value from the keworld in a single line  for this use split function
## Python split() Method - Explanation
## The split() method in Python is used to divide a string into a list of substrings based on a specified separator (delimiter). If no separator is provided, it defaults to whitespace (spaces, tabs, newlines)
## a,b = [int(x)for x in input]
#Key Points:

# If the separator is not specified or is None, the method splits the string by any whitespace (spaces, tabs, newlines).​
# The maxsplit parameter controls the number of splits. If it's set to -1 or not provided, there is no limit on the number of splits.​
# The split() method returns a list of substrings.​
# Programiz
# For more detailed information, you can refer to the official Python documentation: Python String split() Method


# text = "Hello World Python"
# words = text.split()
# print(words)#['Hello', 'World', 'Python']



# text = "apple,banana,grape,orange"
# fruits = text.split(',')
# print(fruits) #['apple', 'banana', 'grape', 'orange']


# text = "one,two,three,four,five"
# words = text.split(',', 2)
# print(words)



# a, b = [int(x) for x in input('Enter 2 numbers: ').split()]
# print("The sum:", a + b)

###step for split function code
#        

# input("inter the 2 numbers : ")



# input("inter the two numbers : ").split()["10", "19"]


# [int(x) for x in input ("enter the two nummber : ").split()[10,20]]

# a, b = [int(x) for x in input("Enter 2 numbers separated by space: ").split(",")]
# print("The sum:", a + b)

# s = input("Enter the number:")
# print(s, type(s))

# s = input("enter 2 numbers : ")
# print(s)
# l =  s.split()
# print(l)


# s = input("enter 2 numbers : ")
# l =  s.split()
# print(l)




# s = input("enter 2 numbers : ")
# print(s)# 10, 20
# l =  s.split()#
# print(l)#['7', '8']
# l1 =[int(x) for  x in l]
# print(l1)# [8, 0]

# a ,b =l1
# print(a)
# print(b)
# print("the sum: ",a + b)

##ths is he short form

# a, b = [int(x) for x  in input("enter the two number").split()]
# print("the sum : ",a+b)

# writr the program to read  3 float value fromm the keyword separation and print the sum
a,b,c = [float(x) for x in input("enter the three float value with  separation :").split(",")] #enter the three float value with  separation :6.8,9.0,6.8
print("the sum :",a + b + c)#the sum : 22.6
####string####

# str1 = "this is a string."
# str2 = 'apnacollage'
# str2 = """this is a string"""

# str1 ="this is astring. \n and \t we are creating it in python."
# print(str1)

# str1 = "apna"
# str2 = "collage"
# final_str = str1+str2
# print(final_str) #1
# print(str1 + str2)#2


# str1 = "apna"
# len1 = (len(str1))
# print(len1)
# str2 = "collage"
# len2 = len(str2)
# print(len2)
# final_str = str1+  str2
# print(final_str)
# print(len(final_str))

# ####indexing#####

# str ="apna collage"
# print(str[3])


####slicing###
# str  = "apna collage"
# print(str[1:4])
# print(str[1:len(str)])
# print(str[:4])
# print(str[1:])

#####negative slicing####
# str = "apple"
# print(str[-5:-2])
# print(str[-5:-1])

####function#####


# str = "i am from studying python from Apnacollage"
# print(str.endswith("ege"))
# str = (str.capitalize())
# print(str)
# print(str.replace("o","a"))
# print(str.find("o"))
# print(str.find("a"))
# print(str.find("from"))

##practice####


# name = input("enter your  name : ")
# print("length of your name is : ",len(name))


# str = "hi,$Iam the $ symbol 99.99"
# print(str.count("$"))

#####conditional statment######

# light = "orange"

# if(light == "red"):
#     print("stop")
# elif(light == "green"):
#     print("go")
# elif(light == "yellow"):
#     print("look")
# else:
#     print("light is broken")

# print("end of code")

# age = 20

# if(age >= 18):
#     print("can vote") #indentation
# else:
#     print("cannot vote")



# marks = int(input("enter sdudeent marks :  "))

# if(marks >= 90):
#     grade = "A"
# elif(marks >= 80):
#     grade = "B"
# elif(marks >= 70):
#     grade = "C"
# else:
#     grade = "D"

# print("grade of thee student = ",grade)



# age = int(input("enter your age : "))

# if(age >= 18):
#     if(age >= 80):
#        print("cannot drive")
#     else:
#         print("can drive")
# else:
#     print("cannot drive")

# num = int(input("enter number : "))

# rem = num % 2

# if(rem == 0):
#     print("EVEN")
# else:
#     print("ODD")

# x = int(input("enter the number : "))
# if(x % 7 == 0):
#     print("multiple of 7")
# else:
#     print("not a multiple")


a = int(input("enter first number : "))
b = int(input("enter second number : "))
c = int(input("enter third number : "))

if(a >= b and a >= c):
    print("first number is largest",a)
elif(b >= c and b >= a):
    print("second number is largest",b)
else:
    print("third is largest",c)

    # """simple code"""

print("hello")
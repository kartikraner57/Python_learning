##############conditional statment
############# 1)if statment =>If condition is true then statements will be executed.
# name=input("Enter Name:") 
# if name=="durga" : 
#     print("Hello Durga Good Morning") 
#     print("How are you!!!")

# if 10 < 20 :
#     print('10 is lss than 20')
# print("end th program")



##############2)if-else statment =>if condition is true then Action-1 will be executed otherwise Action-2 will be executed.
##############

# name = input("enter the name : ")
# if name == "kanha" :
#     print("this my brother")
# else :
#     print("this not my brother")

# ############# 3 ) if-elif-else 

# brand=input("Enter Your Favourite Brand:")
# if brand=="RC" : 
#     print("It is childrens brand") 
# elif brand=="KF": 
#     print("It is not that much kick") 
# elif brand=="FO":
#     print("Buy one get Free One") 
# else : 
#     print("Other Brands are not recommended")


# name = input("enter the name : ")
# if name == "kanha" :
#     print("this my brother")
# elif name == "mauli" :
#     print("this is my cousion")
# else :
#     print("this not my brother")


########### Q1) wap  to find biggest of 2 given numbers ? a
# a1 =int(input("enter First number : "))
# b1 =int(input("enter second number : "))
# if a1 < b1 :
#     print("biggest number ",a1)
# else :
#     print("smallest number ",a1)

# a1 =int(input("enter First number : "))
# b1 =int(input("enter second number : "))
# if a1 > b1 :
#     print("biggest number ",a1)
# else :
#     print("biggest number ",a1)

# a =int(input("enter First number : "))
# b =int(input("enter second number : "))
# if a > b :
#     print(f"{a} is geter than {b}")
# else :
#     print("{b}is greter than {a}".format())

####### wap to find biggest of three number 

# a = int(input("enter the first number : "))

# b = int(input("enter the second  number : "))

# c = int(input("enter the third number : "))
# if a > b > c :
#     print("{} is grtter ".format(a))
# elif b >  c :
#     print("{} is grtter ".format(b))
# else :
#     print("{} is grtter ".format(c))




# a = int(input("enter the first number : "))

# b = int(input("enter the second  number : "))

# c = int(input("enter the third number : "))
# if a > b > c :
#     print("c is the greaterr : ",a)
# elif b >  c :
#     print("c is the greaterr : ",b)
# else :
#     print("c is the greaterr : ",c)





# a = int(input("enter the first number : "))

# b = int(input("enter the second  number : "))

# c = int(input("enter the third number : "))
# if a > b > c :
#     print(f"{a} is the biggest number")
# elif b >  c :
#     print("{} is grtter ".format(b))
# else :
#     print("c is the greaterr : ",c)



################## wap to cheack wheather the given number is  in bettween 1 and 100?
# n = int(input("enter any number :"))
# if n >= 1 and n<= 100:
#     print("the number {} is in between 1 and 100 : ". format(n))
# else :
#     print("the number {} is  not in between 100, ".format(n))


########## wap to take a digit number from the  keyword and points its value in english word?
# list ['zero','one','two','three','four','five,','six','seven',"eight",'nine']
# n =input("enter a digit o to 9 ",())
# print(list[n])

# num_words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
# n = int(input("Enter a digit (0 to 9): "))  # Convert input to integer
# if 0 <= n <= 9:  # Check if input is within valid range
#     print(num_words[n])
# else:
#     print("Invalid input! Please enter a number between 0 and 9.")



# n = int(input("enter the digit from 0 to 9:"))
# if n == 0 and n <= 10 :
#     print("zero")
# elif n == 1 :
#     print("one")
# elif n == 2 :
#     print("two")
# elif n == 3 :
#     print("three")
# elif n == 4 :
#     print("four")
# elif n == 5 :
#     print("five")
# elif n == 6 :
#     print("six")
# elif n == 7 :
#     print("seven")
# elif n == 8 :
#     print("eight")
# elif n == 9 :
#     print("nine")
# else :
#     print("plze inter the digit from 0 to nine")


words_upto_19 = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
                 "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

word_for_tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

n = int(input("Enter a number from 0 to 99: "))

if 0 <= n < 20:
    output = words_upto_19[n]
elif 20 <= n <= 99:
    if n % 10 == 0:
        output = word_for_tens[n // 10]
    else:
        output = word_for_tens[n // 10] + "-" + words_upto_19[n % 10]  # Handles numbers like 21, 32, etc.
else:
    output = "Please enter a number from 0 to 99."

print(output)



n = int(input("Enter a number from 0 to 99: "))

words_upto_19 = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
                 "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

word_for_tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

if n == 0:
    output ="zero"
elif n <= 19:
    output = word_for_tens[n // 10]
elif n <= 99:
    output = word_for_tens[n // 10] + "-" + words_upto_19[n % 10]
else:
    output = "Please enter a number from 0 to 99."

print(output)


#########################  loop with else block
######################### If the loop executed without the break, If you want to do any activity, then we have to define thatactivity inside else part.Remember this one,
#############3If the loop is executed without any break statement, then only else part will be executed.

##########If we want to execute a group of statements iteratively until some condition false,then we should go for while loop.
######Syntax: while condition : body

# x = 1 
# while x <= 10:
#   print(x) 
#   x = x+1

# i = 1
# while i <=10:
#  print("hellow welcome to while ")
#  i = i+1

# ###eg:-To display the sum of first n numbers
# n=int(input("Enter number:")) 
# sum=0 
# i=1 
# while i<=n:
#  sum=sum+i 
#  i=i+1 
# print("The sum of first numbers is :",sum)
###### to print numbers from 1 to 20 which are divide by 3
# 
# 
# 
# x = 1
# while x <= 20:
#     if x % 3 == 0:
#         print(x)
#     x = x + 1  # Move outside the if condition


# name =""
# while name != "sunny":
#     name = input("your favourite actres : ")
# print( "thanks for confirmantion")


######___________________________________
######infinite loops
# i=0; 
# while True : 
#     i=i+1; 
#     print("Hello",i)
# ############ nested loop
# for i in range (3):#0,1,2
#     for j in range(2):#0,1
#         print("helow")


for i in range(3):
    for j in range(2):
        print("i ={}, j ={}".format(i,j))


#####Q) What is the difference between for loop and while loop in Python?
#  ֍ We can use loops to repeat code execution 
# ֍ Repeat code for every item in sequence =>for loop 
# ֍ Repeat code as long as condition is true => while loop

###Q) How to exit from the loop? =>By using break statement
#####Q)When else part will be executed wrt loops?=> If loop executed without break
#3#### how to skip some current iterration inside loop?=>by using continue statment
#3### when else part will be executed in loops? =>If loop executed without break, then only else block will be executed.
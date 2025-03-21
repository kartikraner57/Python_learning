#########################  loop with else block
######################### If the loop executed without the break, If you want to do any activity, then we have to define thatactivity inside else part.Remember this one,
#############3If the loop is executed without any break statement, then only else part will be executed.

##########If we want to execute a group of statements iteratively until some condition false,then we should go for while loop.
######Syntax: while condition : body

x = 1 
while x <= 10:
  print(x) 
  x = x+1

i = 1
while i <=10:
 print("hellow welcome to while ")
 i = i+1

###eg:-To display the sum of first n numbers
n=int(input("Enter number:")) 
sum=0 
i=1 
while i<=n: 
 sum=sum+i 
 i=i+1 
 print("The sum of first",n,"numbers is :",sum)
############ Transfer Statements : 1)break statment
########## 1) break: We can use break statement inside loops to break loop execution based on some condition. 

# for i in range(10): #i = 10
#  if i==7: 
#     print("processing is enough,break loop exicution") 
#     break 
# print(i)




# for i in range(10): #i = 10
#     if i==8: 
#         print("processing is enough,break loop exicution") 
#         break 
#     print(i)
# print('outside of loop')


# cart =[10,500,20,600,70,700,80,900]
# for item in cart :
#     if item >100:
#         print("to place this order insurence must be required")
#         break 
#     print("processing item ",item)

# cart=[10,20,600,60,70] 
# for item in cart: 
#     if item >100: 
#         print("To place this order insurence must be required") 
#         break 
#     print(item)



# x =10 
# if x > 40:
#     print("wea are stoping progam")
#     break 
# print("helow")##is you want to use a break statment compulsory, youshould  br inside the loop,ouy side the loop break statment cannot be used.

#########___________________________________________________________________________________________________________________________________________________

########2)continue: We can use continue statement to skip current iteration and continue next iteration.
# for i in range(10):
#     if i%2==0:
#         continue
#     print(i)
# ########continue
# cart = [10,20,500,700,1000,50,60,5000,100]
# for item in cart:
#     if item >=500:
#         print("incurence must be required =,jast skipping item :",item)
#         continue
#     print("processing item :",item)
# #########break
# cart = [10,20,30,500,700,1000,50,60,5000,100]
# for item in cart:
#     if item >=700:
#         print("incurence must be required =,jast skipping item :",item)
#         break
#     print("processing item :",item)





# #######continue
# nummbers =[10,20,0,5,30]
# for n in nummbers:
#     if n == 0:
#         print("hey how we can divide with zero .. join skipping")
#         continue
#     print("100/{}={}".format(n,100/n))
# #####break
# nummbers =[10,20,0,5,30]
# for n in nummbers:
#     if n == 0:
#         print("hey how we can divide with zero .. join skipping")
#         break
#     print("100/{}={}".format(n,100/n))

# l =[10,20,0,5,0,30]
# for x in l :
#     if x == 0 :
#         print("hellow stuppid , we can divide with zero")
#         continue
#     print("100/{} = {}".format(x,100/x))






########______________________________________________________________________________________________________________________
# for i in range(3): #0,1,2
#  for j in range (3):#0,1,2
#     if i == j :
#         break
#     print(i,j)
# print("______________________________________________________")
# for i in range(3): #0,1,2
#  for j in range (3):#0,1,2
#     if i == j :
#         continue
#     print(i,j)






##########3 Loops with else Block: 
########## Inside loop execution, if break statement not executed, then only else part will be executed. 
########## else means loop without break.
cart=[10,20,30,40,50] 
for item in cart: 
    if item>=56: 
        print("We cannot process this order") 
        break 
    print("processing",item)
else:
    print("Congrats ...all items processed successfully")



cart=[10,20,30,600,40,50] 
for item in cart: 
    if item>=56: 
        print("We cannot process this order") 
        break 
    print("processing",item)
else:
    print("Congrats ...all items processed successfully")




cart=[10,20,30,600,40,50] 
for item in cart: 
    if item>=56: 
        print("We cannot process this order") 
        continue
    print("processing",item)
else:
    print("Congrats ...all items processed successfully")
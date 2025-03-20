############ Transfer Statements : 1)break statment
########## 1) break: We can use break statement inside loops to break loop execution based on some condition. 

# for i in range(10): #i = 10
    # if i==7: 
    #     print("processing is enough,break loop exicution") 
    #     break 
    # print(i)

# for i in range(10): #i = 10
#     if i==8: 
#         print("processing is enough,break loop exicution") 
#         break 
#     print(i)
# print('outside of loop')


# cart =[10,20,600,70,80]
# for item in cart :
#     if item >600:
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



########2)continue: We can use continue statement to skip current iteration and continue next iteration.
# for i in range(10):
#     if i%2==0:
#         continue
#     print(i)

# cart = [10,20,500,700,50,60]
# for item in cart:
#     if item >=500:
#         print("we can notprocess this item :",item)
#         continue
#     print(item)


nummbers =[10,20,0,5,30]
for n in nummbers:
    if n == 0:
        print("hey how we can divide with zero .. join skipping")
        continue
    print("100/{}={}".format(n,100/n))
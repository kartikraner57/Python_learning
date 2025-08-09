####loops #loops are used to repeat instructions.

# #while loop
# while True :
#     print("hello")

# count = 1
# while count <=5 :
#     print("hello")
#     count += 1
#     print(count)



# i = 1
# while i <= 5:
#     print("hello"
#     i+=1

# #print numbers from 1 to 5
# i = 5
# while i >= 5:
#     print(i)
#     i -= 1
# print("loop ended")

#print number from 1 to 100.
# i = 1
# while i >= 100:#stopping condition
#     print(i)
#     i += 1

#reverse
# i = 100
# while i >= 1:
#     print(i)
#     i -= 1

# #print the multiplication table of a number n.
# n = int(input("enter number : "))
# i = 1
# while i <= 10:
#     print(n*i)
#     i += 1

# #print the element of the following list using a loop
# # [1,4,9,16,25,36,49,64,81,100]
# nums = [1,4,9,16,25,36,49,64,81,100]
# idx = 0
# while idx < len(nums):
#     print(nums[idx]) #num[0],nums[2],num[2]..
#     idx += 1

# heroes = ["ironman","thor","superman","batman"]
# idx = 0
# while idx < len(heroes):
#     print(heroes[idx])
#     idx += 1
# for i in range(5):
#     print(i)

#     fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)

# for i in range(0, 10, 2):
#     print(i)

# for i in range(3):
#     for j in range(2):
#         print(f"i: {i}, j: {j}")

# nums = (1,4,9,16,25,36,49,64,81,100)

# x =36

# i = 0 #
# while i < len(nums):
#     print(nums[i])
#     i += 1


# nums = (1,4,9,16,25,36,49,64,81,100)

# x =36

# i = 0 #
# while i < len(nums):
#     if(nums[i] == x):
#         print("found at inx", i)

#     i += 1


# nums = (1,4,9,16,25,36,49,64,81,100,36)

# x =36

# i = 0 #
# while i < len(nums):
#     if(nums[i] == x):
#         print("found at inx", i)
#     else:
#         print("finding ..")

#     i += 1



  ##  break and continue
  #break : use to termine the loop when encountered
  #couninue : terminates exicution in the current iter

# i = 1 
# while i <= 5:
#     print(i)
#     if(i== 3):
#         break
#     i += 1

# print("end of loop")


# nums = (1,4,9,16,25,36,49,64,81,100,)

# x =36

# i = 0 #
# while i < len(nums):
#     if(nums[i] == x):
#         print("found at inx", i)
#         break
#     else:
#         print("findin..")
#     i += 1

# print("end of loop")



# i = 0
# while i <= 5:
#     if(i == 3) :
#         i+= 1
#         continue #skip
#     print(i)
#     i += 1

# ####for loop ## this loop used to for sequential traverse. for traversing list,string,tuples etc.
# veggies = ["potato","brijal", "ladyfinger","cucumber"]

# for val in veggies :
#     print(val)
# tup =(1,2,3,4,5,)
# for num in tup :
#     print(num)

str = "apnacollage"
for char in str:
    if(char == 'o'):
     print("o found")
     break
    print(char)
print("END")

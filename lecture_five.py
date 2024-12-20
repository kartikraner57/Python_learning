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

#print the element of the following list using a loop
# [1,4,9,16,25,36,49,64,81,100]
nums = [1,4,9,16,25,36,49,64,81,100]
idx = 0
while idx < len(nums):
    print(nums[idx]) #num[0],nums[2],num[2]..
    idx += 1

heroes = ["ironman","thor","superman","batman"]
idx = 0
while idx < len(heroes):
    print(heroes[idx])
    idx += 1
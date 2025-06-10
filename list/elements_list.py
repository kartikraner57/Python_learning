#Accessing Elements of List: 
# We can access elements of the list either by using index or by using slice operator(:)
#1) By using Index: 
# ֍ List follows zero based index. ie index of first element is zero. 
# ֍ List supports both +ve and -ve indexes. 
# ֍ +ve index meant for Left to Right 
# ֍ -ve index meant for Right to Left 
# ֍ list = [10, 20, 30, 40]
# print(list[0])  10 
# ֍ print(list[-1])  40 
# ֍ print(list[10])  IndexError: list index out of range


#2) By using Slice Operator:  
# 
# Syntax: list2 = list1[start:stop:step]
# Start  It indicates the Index where slice has to Start Default Value is 0
# Stop  It indicates the Index where slice has to End Default Value is max allowed Index of List ie Length of the List
# Step  increment value Default Value is 1


# n=[1,2,3,4,5,6,7,8,9,10] 
# #2) print(n[2:7:2]) 
# 3) print(n[4::2]) 
# 4) print(n[3:7]) 
# 5) print(n[8:2:-2]) 
# 6) print(n[4:100])


# n=[1,2,3,4,5,6,7,8,9,10] 
# #2) print(n[2:7:2]) 
# 3) print(n[4::2]) 
# 4) print(n[3:7]) 
# 5) print(n[8:2:-2]) 
# 6) print(n[4:100])

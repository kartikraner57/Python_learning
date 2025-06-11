###########  II. Manipulating Elements of List:


#1) append() Function: We can use append() function to add item at the end of the list. 
# 1) list=[] 
# 2) list.append("A") 
# 3) list.append("B") 
# 4) list.append("C") 
# 5) print(list)

#Eg: To add all elements to list upto 100 which are divisible by 10 
#list=[] 
# for i in range(101): 
#if i%10==0: 
# list.append(i) 
# print(list)  #[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]




####### 2) insert() Function: To insert item at specified index position 
# n=[1,2,3,4,5] 
# n.insert(1,888) 
# print(n)


# n=[1,2,3,4,5] 
# n.insert(10,777) 
# n.insert(-10,999) 
# print(n)


# Note: If the specified index is greater than max index then element will be inserted at last position.
#  If the specified index is smaller than min index then element will be inserted at first position.ldl sssssss


# Note: If the specified index is greater than max index then element will be inserted at last position.
#  If the specified index is smaller than min index then element will be inserted at first position.ldl sssssss

a = 10
b = 23
c = a + b
print(c)

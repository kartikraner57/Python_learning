# marks1 = 94.4
# marks2 = 87.5
# marks3 = 95.2
# marks4 = 66.4
# marks5 = 45.1

# marks = [94.4, 87.5, 95.2, 66.4, 45.1]

# print(marks[3])
# print(type(marks))
# print(marks[1])

# student = ["karan", 95.4, 17, "pune"]
# print(student[0])
# student[0] ="arjun"
# print(student)
#print(student[5]) #this is wrong


# str = "hello"
# print(str[0])
# #[0] = "y" # beacuse of string is immutable

# marks =[85, 94, 76, 63, 48]
# print(marks[-3:-1])


###list function####
# list = [2,1,3]
# list.append(4) #taking in last
# print(list)

# list = [2,1,3]
# list.append(4)
# print(list.sort(reverse = True))#sort = sequence 
# print(list.sort())
# print(list)


# list = [2,1,3]
# list.reverse()
# print(list)
# print(list.sort())
# print(list)



# list = [2,1,3]
# list.insert(3,8)
# print(list)
# list.insert(2,0)
# print(list)


# list = [2,5,3]
# list.remove(2)
# print(list)


# list = [2,1,3]
# list.pop(2)
# print(list)


####tuple####

# tup = (2, 1, 3, 1)
# print(type(tup))
# print(tup[0])
# print(tup[2])
#tup[0] = 5  #wrong beacuse of immutable

# tup = ()
# print(tup)
# print(type(tup))

# tup = (2, 1, 5, 1)
# print(tup[1:3])

# tup = (2,1,3,1)
# print(tup.index(2))
# print(tup.index(3))
# print(tup.index(1))

#tup = (2,1,3,1)
# print(tup.count(2))
# print(tup.count(3))
# print(tup.count(1))


# movies = []

# a = input(" enter 1st movie :")
# b = input("enter 2nd movie :")
# c = input("enter 3rd movie :")

# movies.append(a)
# movies.append(b)
# movies.append(c)

# print(movies)


# movies = []


# movies.append(input(" enter 1st movie :"))
# movies.append(input(" enter 1st movie :"))
# movies.append(input(" enter 1st movie :"))

# print(movies)

# list1 = [1, 2, 1]
# list2 = [1, 2, 3]

# copy_list1 = list1.copy()
# copy_list1.reverse()

# if(copy_list1 == list1):
#       print("polindrome") #ex of polindrme 12321
# else:
#      print("not palindrome")


# list1 = [1, 2, 1]
# list2 = [1, 2, 3]

# copy_list2 = list2.copy()
# copy_list2.reverse()

# if(copy_list2 == list2):
#       print("polindrome") #ex of polindrme 12321
# else:
#      print("not palindrome")




grade = ("c", "D", "A", "A", "B", "B", "A")

print(grade.count("A"))


grade = ["c", "D", "A", "A", "B", "B", "A"]

grade.sort()
print(grade)

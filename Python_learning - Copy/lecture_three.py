# marks1 = 94.4
# marks2 = 87.5
# marks3 = 95.2
# marks4 = 66.4
# marks5 = 45.1

# marks = [94.4, 87.5, 95.2, 66.4, 45.1]

# print(marks[3])
# print(type(marks))git
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

##append
# my_list = [1, 2, 3]
# my_list.append(4)  # Adds 4 at the end
# print(my_list)  # Output: [1, 2, 3, 4]

##extend
# my_list = [1, 2, 3]
# my_list.extend([4, 5])  # Adds 4 and 5 to the list
# print(my_list)  # Output: [1, 2, 3, 4, 5]

##insert
# my_list = [1, 2, 3]
# my_list.insert(1, 'a')  # Inserts 'a' at index 1
# print(my_list)  # Output: [1, 'a', 2, 3]

##remove()
# my_list = [1, 2, 3, 2]
# my_list.remove(2)  # Removes the first 2
# print(my_list)  # Output: [1, 3, 2]

##pop()
# my_list = [1, 2, 3]
# popped_element = my_list.pop(1)  # Removes the element at index 1 (which is 2)
# print(popped_element)  # Output: 2
# print(my_list)  # Output: [1, 3]

##index()
# my_list = [1, 2, 3, 2]
# index_of_2 = my_list.index(2)  # Finds the index of the first occurrence of 2
# print(index_of_2)  # Output: 1

##count()
# my_list = [1, 2, 3, 2, 2]
# count_of_2 = my_list.count(2)  # Counts how many times 2 appears in the list
# print(count_of_2)  # Output: 3

##sort()
# my_list = [3, 1, 2]
# my_list.sort()  # Sorts the list
# print(my_list)  # Output: [1, 2, 3]

##reverse()
# my_list = [1, 2, 3]
# my_list.reverse()  # Reverses the list
# print(my_list)  # Output: [3, 2, 1]

##clear()
# my_list = [1, 2, 3]
# my_list.clear()  # Clears the list
# print(my_list)  # Output: []


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



# grade = ("c", "D", "A", "A", "B", "B", "A")

# print(grade.count("A"))


# grade = ["c", "D", "A", "A", "B", "B", "A"]

# grade.sort()
# print(grade)






class Customer:
    ''' Customer class with bank operations.. '''
    bankname = 'DURGABANK'

    def __init__(self, name, balance=0.0):
        self.name = name
        self.balance = balance

    def deposit(self, amt):
        self.balance = self.balance + amt
        print('Balance after deposit:', self.balance)

    def withdraw(self, amt):
        if amt > self.balance:
            print('Insufficient Funds..cannot perform this operation')
            sys.exit()
        self.balance = self.balance - amt
        print('Balance after withdraw:', self.balance)


print('Welcome to', Customer.bankname)
name = input('Enter Your Name: ')
c = Customer(name)

while True:
    print('\nd-Deposit \nw-Withdraw \ne-Exit')
    option = input('Choose your option: ')
    if option == 'd' or option == 'D':
        amt = float(input('Enter amount: '))
        c.deposit(amt)
    elif option == 'w' or option == 'W':
        amt = float(input('Enter amount: '))
        c.withdraw(amt)
    elif option == 'e' or option == 'E':
        print('Thanks for Banking')
        sys.exit()
    else:
        print('Invalid option..Please choose a valid option')
































print(bin(3))
print(oct(30))
print(hex(3))
print(oct(0xface))
print(bin(0xface))
print(hex(0xface))
print(oct(0xface))



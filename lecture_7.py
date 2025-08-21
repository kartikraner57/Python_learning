#File i/o in python = python can be used to operation on  a file.(read & write data)
#types of all files = 1).txt, .docx, .log etc   2)binary files : .mp4, .mov, .png, .jpeg etc.
 
# f = open("demo.txt", "r")
# data = f.read()
# print(data)
# print(data)
# print(type(data))

# x = int(input("enter the number : "))
# if(x % 7 == 0):
#     print("multiple of 7")
# else:
#     print("not a multiple")


# name = input ("enter your age :")
# print ("you entered ", name)



# age = int(input("Please enter your age: "))

# # Print a message based on the age
# if age < 18:
#     print("You are a minor.")
# elif age >= 18 and age <= 64:
#     print("You are an adult.")
# else:
#     print("You are a senior citizen.")


# class student:
#     ''' This class developed by Durga for demo purpose '''
    
#     def __init__(self):  # Corrected constructor
#         self.name = "durga"
#         self.rollno = 101
#         self.marks = 90

#     def talk(self):
#         print("Hello, my name is:", self.name)
#         print("My rollno is:", self.rollno)  # Fixed typo here
#         print("My marks are:", self.marks)

# # Creating object
# s = student()

# # Accessing attributes
# print(s.name)
# print(s.rollno)
# print(s.marks)

# # Calling method
# s.talk()



import mymodule

print(mymodule.greet("Kartik"))
print(mymodule.add(10, 5))

# # Q) Write a Function to accept 2 Numbers as Input and return Sum
# def add(x, y):
#     return x + y

# result = add(10, 20)
# print("The sum is", result)
# print("The sum is", add(100, 200))
# # If we are not writing return statement then default return value is None.
# def f1():
#     print("Hello")

# f1()
# print(f1())
# # Write a Function to check whether the given Number is Even OR Odd? 
# def even_odd(num):
#     if num % 2 == 0:
#         print(num, "is Even Number")
#     else:
#         print(num, "is Odd Number")

# even_odd(10)
# even_odd(15)
# Q) Write a Function to find Factorial of given Number?
def fact(num):
    result = 1
    while num >= 1:
        result = result * num
        num = num - 1
    return result

for i in range(1, 5):
    print("The Factorial of", i, "is:", fact(i))

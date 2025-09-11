# # The rest of the program won't be executed.
# print("Hello")
# print(10/0)
# print("Hi")


# print("stmt-1")
# print(10/0)
# print("stmt-3")

# With try-except:
print("stmt-1")

try:
    print(10/0)
except ZeroDivisionError:
    print(10/2)

print("stmt-3")
# How to Print Exception Information:
try:
    print(10/0)
except ZeroDivisionError as msg:
    print("exception raised and its description is:", msg)
# try with Multiple except Blocks:
try:
    x = int(input("Enter First Number: "))
    y = int(input("Enter Second Number: "))
    print(x / y)

except ZeroDivisionError:
    print("Can't Divide with Zero")

except ValueError:
    print("please provide int value only")

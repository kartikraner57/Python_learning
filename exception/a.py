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

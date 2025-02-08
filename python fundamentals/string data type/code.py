# Single quotes
my_string = 'Hello, World!'
print(type(my_string))

# Double quotes
another_string = "Python is awesome!"

print(my_string)
print(another_string)


single_quote_string = 'This is a string using single quotes.'
print(single_quote_string)

double_quote_string = "This is a string using double quotes."
print(double_quote_string)

triple_double_quote_string = """This is another example
of a multi-line string."""
print(triple_double_quote_string)


combined_string = "This is a string with 'single quotes' inside double quotes."
print(combined_string)

triple_combined_string = '''This string contains both "double quotes" and 'single quotes'.'''
print(triple_combined_string)

# A simple list
my_list = [1, 2, 3, 4, 5]
print(my_list)

my_list.append(6)
print(my_list)  # [1, 2, 10, 4, 5, 6]

my_list[2] = 10
print(my_list)  # [1, 2, 10, 4, 5]



# Using f-strings (formatted string literals)
name = "Alice"
age = 25
greeting = f"Hello, my name is {name} and I am {age} years old."
print(greeting)

# Using str.format()
greeting_format = "Hello, my name is {} and I am {} years old.".format(name, age)
print(greeting_format)
S
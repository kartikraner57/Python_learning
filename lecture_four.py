# print("lecture four")

# ###dictionary###
# info = {
#     "key" : "value",
#     "name" : "apnacollage",
#     "age" : "35",
#     "is_adult" : "True",
#     "12.99" : "94.4"
# }
# null_dict  = {}
# print(null_dict)
# print(info)
# info["name"]= "kartik raner"
# print(info)

# ##nested dictionaries
# student ={
#     "name":"kartik",
#     "score":{
#         "chem": 98,
#         "phy": 97,
#         "math" : "95"
#     }}
# print(student)
# print(student["score"]["math"])
# print(student["score"]["phy"])
# print(student["score"]["chem"])
# print(list(student.values()))


##Dictionary methods
# #1).keys() #Returns a view object that displays all the keys in the dictionary.
# my_dict = {"a": 1, "b": 2}
# print(my_dict.keys())  # Output: dict_keys(['a', 'b'])

# #2.values() #Returns a view object that displays all the values in the dictionary.
# my_dict = {"a": 1, "b": 2}
# print(my_dict.values())  # Output: dict_values([1, 2])

# #3).items() #This method is commonly used to iterate over both keys and values in a dictionary.
# my_dict = {"a": 1, "b": 2}
# for key, value in my_dict.items():
#     print(key, value)
# # Output:
# # a 1
# # b 2

# # #4)get() #Returns the value for the specified key. If the key does not exist, it returns None or a default value.
# my_dict = {'a': 1, 'b': 2}
# print(my_dict.get('a'))  # Output: 1
# print(my_dict.get('c'))  # Output: None
# print(my_dict.get('c', 'Not Found'))  # Output: Not Found

# # #5)update() #Updates the dictionary with elements from another dictionary
# my_dict = {'a': 1, 'b': 2}
# my_dict.update({'b': 3, 'c': 4})
# print(my_dict)  # Output: {'a': 1, 'b': 3, 'c': 4}

####set####
collection = {1,2,3,4,5,6,7,}

print(collection)
print(type(collection))
print(len(collection))

collection = {}#empty dictionary
print(type(collection))

collection = set()
print(type(collection))

my_set = {1, 2, 3}
my_set.add(4)
print(my_set)  # Output: {1, 2, 3, 4}

my_set = {1, 2, 3}
my_set.remove(2)
print(my_set)  # Output: {1, 3}
# my_set.remove(4)  # Raises KeyError because 4 is not in the set

my_set = {1, 2, 3}
my_set.clear()
print(my_set)  # Output: set()

my_set = {1, 2, 3}
element = my_set.pop()
print(element)  # Output: Random element, e.g., 1
print(my_set)  # Output: Set with one less element

################### Q)wap to get value the dictionary for the given key
# d = {100: "A", 200: "B", 300: "C", 400: "D"}
# key = int(input("Enter the key to find value: "))

# if key in d:
#     print("The corresponding value:", d.get(key))
# else:
#     print("Key not found in dictionary.")

##### vip
d = {100: "A", 200: "B", 300: "C", 400: "D"}
value = input("Enter the value to find its key: ")
available = False

for k, v in d.items():
    if v == value:
        print("The corresponding key:", k)
        available = True
        break

if available == False:
    print("Provided value not found in dictionary.")

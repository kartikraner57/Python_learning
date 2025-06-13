 #######len() Returns the number of items in the dictionary.
d = {100: 'durga', 200: 'ravi', 300: 'shiva'}  
print(len(d))


# # #######d.get(key) If the key is available then returns the corresponding value otherwise returns None.It wont raise any error.
# # d.get(key,defaultvalue) If the key is available then returns the corresponding value otherwise returns default value.

# d={100:"durga",200:"ravi",300:"shiva"} 
# print(d[100])
# print(d[400])
# print(d.get(100))
# print(d.get(400)) 
# print(d.get(100,"Guest"))
# print(d.get(400,"Guest")) 

######key():
# It returns list of tuples representing key-value pairs. [(k,v),(k,v),(k,v)] 

# d = {100: "durga", 200: "ravi", 300: "shiva"}

# print(d.keys())

# for k in d.keys():
#     print(k)

##########8) values(): It returns all values associated with the dictionary.
d = {100: "durga", 200: "ravi", 300:"shiva"}
print(d.values())
for v in d.values():
    print(v)
    


######9) items(): It returns list of tuples representing key-value pairs. [(k,v),(k,v),(k,v)] 
# d={100:"durga",200:"ravi",300:"shiva"} 
# for k,v in d.items(): 
#     print(k,"--",v)
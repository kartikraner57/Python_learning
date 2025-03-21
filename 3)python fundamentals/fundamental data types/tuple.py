#tuple this is immutable, (), less memory, faster access(performence is more)
k =(10,20,30,40,50,60,"durga")
print(k)
print(type(k))
print(k[1])
print(k[-3])
print(k[0:-4])
#appen(),removw() are not applicable for tuple because immutable
k = ()
k =(10)
print(type(k))
k = (10,) #important
print(type(k))
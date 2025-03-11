s = {10,20,30,40}
s.add(50)
s.remove(30)
print(s)

fs = {10,20,30,40}
fs = frozenset(s)
print(type(fs))
#fs.add(50) #error
fs.remove(30)
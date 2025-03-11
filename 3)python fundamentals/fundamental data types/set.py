s1 = {1, 2, 3}# =>equal
s2 = {3, 2, 1}# =>equal
s3 = {1, 3, 2}# =>equal
print(s1,s2,s3)
print(type(s1))


s = (10, 13 , 30 ,"data",50,600)
#print{s[0]}=>indexing concept not allow in set
#print(s[1:4])=>set bleet not subcriable
s = {10,20,30,40}
s.add(50) #addmethod applicable foe list but set applicable for add
print(s)
s.remove(30)
s ={}
print(type(s))
a = set()
print(type(a))
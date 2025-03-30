#Splitting of Strings: 
# We can split the given string according to specified seperator by using split() method. 
# l = s.split(seperator) 
# The default seperator is space. The return type of split() method is List.s="durga software solutions" 
# s="durga software solutions"
# l=s.split() 
# for x in l: 
#  print(x)

# s="22-02-2018" 
# l=s.split('-') 
# for x in l: 
#    print(x)

#Joining of Strings: We can join a Group of Strings (List OR Tuple) wrt the given Seperator.
#  s = seperator.join(group of strings)

t = ("durga","software","solutions")
s = "-".join(t)
print(s)
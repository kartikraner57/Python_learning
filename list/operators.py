# Using Mathematical Operators for List Objects:We can use + and * operators for List objects.
#1)Concatenation Operator (+):  We can use + to concatenate 2 lists into a single list
a = [10, 20, 30] 
b = [40, 50, 60] 
c = a+b
print(c) #-> [10, 20, 30, 40, 50, 60]
#Note = To use + operator compulsory both arguments should be list objects, otherwise we will get TypeError.
##c = a+40 #-> TypeError: unsupported operand type(s) for +: 'list' and 'int'
c = a+[40] #-> valid [10, 20, 30, 40]
## Repetition Operator (*): We can use repetition operator * to repeat elements of list specified number of times. 
# 1) x = [10, 20, 30] 

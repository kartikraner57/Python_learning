#File i/o in python = python can be used to operation on  a file.(read & write data)
#types of all files = 1).txt, .docx, .log etc   2)binary files : .mp4, .mov, .png, .jpeg etc.
 
f = open("demo.txt", "r")
data = f.read()
print(data)
print(data)
print(type(data))
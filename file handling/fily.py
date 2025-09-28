# Various Properties of File Object:

# f=open("abc.txt",'w')
# print("File Name: ",f.name)
# print("File Mode: ",f.mode)
# print("Is File Readable: ",f.readable())
# print("Is File Writable: ",f.writable())
# print("Is File Closed : ",f.closed)
# f.close()
# print("Is File Closed : ",f.closed) 


# f=open("abcd.txt",'w')
# f.write("Durga\n")
# f.write("Software\n")
# f.write("Solutions\n")
# print("Data written to the file successfully")
# f.close() 

# f=open("abcd.txt",'a')
# f.write("Durga\n")
# f.write("Software\n")
# f.write("Solutions\n")
# print("Data written to the file successfully")
# f.close() 

# # Writing Data to Text Files

# f = open("abcd.txt", "w")
# f.write("Durga\n")
# f.write("Software\n")
# f.write("Solutions\n")
# print("Data written to the file successfully")
# f.close()



# f = open("abcd.txt", "w")
# list = ["sunny\n", "bunny\n", "vinny\n", "chinny"]
# f.writelines(list)
# print("List of lines written to the file successfully")
# f.close()


# # Reading Character Data from Text Files:
# f = open("abc.txt", "r")
# data = f.read()
# print(data)
# f.close()


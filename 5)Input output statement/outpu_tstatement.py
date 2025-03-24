# # output statment
# # #######print()


# ####without arrguments :

# print("durga")
# print()
# print('soft')




# #### witharguments
# # print(string)
# print('durga')
# print("duga \n software")
# print("durga \t software")
# print("duga" + "software")
# print(10* "software")

# # #########print   stament with variable number of arguments
# a, b, c = 10, 20, 30
# print("value", a, b, c)
# print("Sum:", a + b + c)  # Correct way to sum the values



# ################ sep atributes       sep means  sepreator
# a, b, c, d =  10, 20  , 30, 40,
# print(a,b,c,d ,sep = ':')
# print(a,b,c,d ,sep = '.')
# print(a,b,c,d ,sep = '__')




# ################ end atributes /end Parameter 
# print("hello")
# print('durga')
# print('soft')
# print("hello",end = '')
# print('durga',end ='')
# print('soft')


# print("hello",end = ': :')
# print('durga',end ='****')
# print('soft')


# print(10,20,30,40,sep =':',end = '***')

# print(40,50,60,sep = ':')
# print(70,80,sep ='**',end = '$$$')
# print(90,100)


# ### print(object)
# l =[10,20,30.40]
# print(l)
# t = (10,20,30,40)
# print(t)
# ################ print() with replacemnet operator {}
name = "durga"
salory = 10000
gf =' sunny'
print("hello {}, your salory is {} and you find {} waiting".format(name,salory,gf))
print("hello {0}, your salory is {1} and you find {2} waiting".format(name,salory,gf))
print("hello {n}, your salory is {s} and you find {f} waiting".format(s =name,n =salory,f =gf))


# a , b ,c,d = 10 ,20 ,30, 40
# print('a = {}, b={}, c={}, d={}'.format(a,b,c,d))


# ################ print stament with formated string
# ##### syntax = print("formated string" % (veriable list))
# a = 10 
# print("a value : %i" %a)


# a = 10 
# b = 0
# c = 30
# print("a = %d, b = %d, c = %d"%(a,b,c))

# name = "durga"
# marks = [10,20,30,40]
# print('hello %s,your marks list : %s' %(name, marks))
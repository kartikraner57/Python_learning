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

# t = ("durga","software","solutions")
# s = "-".join(t)
# print(s)

# l = ['hyderabad', 'singapore', 'london', 'dubai'] 
# s = ':'.join(l) 
# print(s)  # Output: hyderabad:singapore:london:dubai


# Changing Case of a String:
# We can change case of a string by using the following 4 methods
# 1).upper()  To convert all characters to upper case 
# 2) lower()  To convert all characters to lower case 
# 3) swapcase()  Converts all lower case characters to upper case and all upper case characters to lower case 
# 4) title()  To convert all character to title case. i.e first character in every word should be upper case and all remaining characters should be in lower case. 
# 5) capitalize()  Only first character will be converted to upper case and all remaining characters can be converted to lower case
# s = 'learning Python is very Easy' 
# print(s.upper()) # Output: LEARNING PYTHON IS VERY EASY
# print(s.lower()) # Output: learning python is very easy
# print(s.swapcase()) # Output: LEARNING python IS VERY easy
# print(s.title()) # Output: Learning Python Is Very Easy
# print(s.capitalize())  # Output: Learning python is very easy








#########Checking Starting and Ending Part of the String: 
# Python contains the following methods for this purpose 
# 1) s.startswith(substring) 
# 2) s.endswith(substring)
# s = 'learning Python is very easy' 
# print(s.startswith('learning')) 
# print(s.endswith('learning')) 
# print(s.endswith('easy'))




# To Check Type of Characters Present in a String: Python contains the following methods for this purpose.
# 1) isalnum(): Returns True if all characters are alphanumeric( a to z , A to Z ,0 to9 ) 
# 2) isalpha(): Returns True if all characters are only alphabet symbols(a to z,A to Z) 
# 3) isdigit(): Returns True if all characters are digits only( 0 to 9) 
# 4) islower(): Returns True if all characters are lower case alphabet symbols 
# 5) isupper(): Returns True if all characters are upper case aplhabet symbols 
# 6) istitle(): Returns True if string is in title case 
# 7) isspace(): Returns True if string contains only spaces
# Eg: 
# 1) print('Durga786'.isalnum())  True 
# 2) print('durga786'.isalpha())  False 
# 3) print('durga'.isalpha())  True 
# 4) print('durga'.isdigit())  False 
# 5) print('786786'.isdigit())  True 
# 6) print('abc'.islower())  True 
# 7) print('Abc'.islower())  False 
# 8) print('abc123'.islower())  True 
# 9) print('ABC'.isupper())  True 
# 10) print('Learning python is Easy'.istitle())  False 
# 11) print('Learning Python Is Easy'.istitle())  True 
# 12) print(' '.isspace())
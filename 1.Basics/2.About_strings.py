my_name1="Narendra Kumar Reddy"
my_name2="narendra kumar reddy"
my_name3="narendrakumarreddy"
your_string_variable=my_name1
#Slicing of a string
print(your_string_variable)
print(your_string_variable[:])
print(your_string_variable[2:9])
print(your_string_variable[2:9:1])
print(your_string_variable[2:9:2])

print(your_string_variable[:-1])

#Length of a function: 
print(len(your_string_variable))

#The following string functions will convert your stirngs from lower to upper/upper to lower ......
print(your_string_variable.lower())
print(your_string_variable.upper())
print(your_string_variable.title())
print(your_string_variable.capitalize())
print(your_string_variable.swapcase())
 
#The following string functions will give output as True or False
 
print(your_string_variable.islower())
print(your_string_variable.isupper())
print(your_string_variable.istitle())
print(your_string_variable.isdigit()) #i think in python3 it is not der instead it used isnumeric()
print(your_string_variable.isalpha())
print(your_string_variable.isalnum())  #only numbers and alphabets
print(your_string_variable.isspace())
print(your_string_variable.endswith('your_argument'))
print(your_string_variable.startswith('your_argument'))

#Imp string functions: index,find,count,join,split,strip
 
print(your_string_variable.index('character/string')   #index and find will give the index of first occurence of a charter/string
print(your_string_variable.find('character/string')    #If character/string is not found then index method will give error
                                                       #but find wont give error instead it will give -1 if character/string doesnt exist.
                                                       
print("".join(your_string_variable)                                                          
print(" ".join(your_string_variable)                                                          
print("**".join(your_string_variable)                                                          
print("xxxxx".join(your_string_variable)                                                     
Note: in join method/function/operation alwasy it should take only one argument.

print(your_string_variable.split())
print(your_string_variable.split(" "))
Note: By deafult split will take space as spliting value
print(your_string_variable.split("r"))


print(your_string_variable.strip())
print(your_string_variable.strip(" "))
Note: split and strip defautl argument is space.

print(your_string_variable.rstrip())
print(your_string_variable.lstrip())


#Important:
string = "Hello World"
print( ' '.join(reversed(string)))
 
 
 
 
 
 

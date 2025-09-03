#implement all the 3 ways of denoting a string
#1 double quotes
#2 single quotes
#3 triple quotes

# print("hello world")
# print('hello world')
# print("""hello world""")

#string methods
#case conversion methods 
# print(name.upper())  #upper case
# print(name.lower())  #lower case
# print(name.title())  #title case

#whitespace and padding
# print(name.strip()) # strip will remove the whitespace
# # from start and end of the string
# print(name.lstrip())
# print(name.rstrip())

# print("hi".center(20,"*"))
# print("hi".ljust(20,"*"))
# print("hi".rjust(20,"*"))
# print("hi".zfill(20))

##character removal 
# print("hi".removeprefix("h"))
# print("hi".removesuffix("i"))

#replace and modify 
# print(name.replace("Python","Java"))
# ##expand tabs 
# print(name.expandtabs(20))

#validation / boolean checks 
# print(name.isalpha())
# print(name.isalnum()) #alpha numeric
# print(name.isdigit())
# print(name.islower())
# print(name.isupper())

# name = "PythonProgramming" 
# print(name.startswith("Py"))
# print(name.endswith("ing"))

#split and join 
# print("a b ab cd e f".split("ab")) # ["a" , "b" , "c" , "a" , "d".split(""))
## in split method you can also pass a particular 
# separator
## can you split your string by multiple values or not ?

#partiton
# print("a-b-c-d".partition("-"))
#the output you will be getting from the partition method
#will be a tuple of 3 values(left , separator , right)
#("a" , "-" , "b-c")

#join
# print("-".join(["a","b","c"]))


#data types 
#a data type defines the type of data a variable can hold.
# it tells the interpreter what kind of value is stored and what
# operations can be performed on it.

##data  types in python 
#1  numeric -- int , float , complex
#2 - sequence -- list , tuple , range,string
#3 - mapping -- dict
#4 - set - set , frozenset
#5 - boolean
#6 - None
#7 - binary types -- bytes , bytearray,memory view

#string -- 
#a string is a sequence of characters enclosed in single ,
#double or triple quotes.
# ex - "python" , 'python' , """python"""

#features of string 
#1 -- immutable
#2 -- ordered
#3 -- indexed -- positive and negative
#4 -- allow duplicate values



#indexing -- accessing single element from the string 
#slicing -- accessing multiple elements from the string

# h e l l o
#two types of indexing
# 0 1 2 3 4 5 ----> positive indexing
#-6-5-4-3-2-1 ---> negative indexing
# print(name[-13])
##slicing -- accessing multiple elements from the string
# [start:end:step/skip]
# print(name[7:18])
# name = "python programming"

# print(name[::2])
# ##reverse the string 
# print(name[::-1])


# age = 10
# # text = "my age is " + age

# #f-string//formatted string
# text = (f"my age is {age}")
# print(text)


#format
# name = "ace"
# age = 10
# text = "my name is {} and my age is {}"
# print(text.format(name,age))

##%s -- string 
name = "ace"
age = 10
text = "my name is %s and my age is %s" % (name,age)
print(text)


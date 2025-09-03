# 23/08/25
## about python 
## python is a high level programming
#  language, interpreted , object-oriented
#programming language created by guido van 
#rossum in 1991.
#2 -- it is known for its simple syntax 
# that resembles  the English language.
# print("hello world")
#3 - python is a beginner friendly language
#and widely used in fields like web development,
#data science, artificial intelligence, and
#machine learning.

## features of python 

#1 -- Simple and easy to learn 
#2 -- Interpreted language
#-- > code is executed line by line
#3 -- cross platform
#-- python file can be run on any
#  operating system like windows, linux, mac
#4 -- open source and free
# --> python is free to use , modify and
#  distribute
#5 -- object-oriented programming
#--> python supports classes , objects ,
#  inheritance , polymorphism and 
# encapsulation
#6 -- extensive standard library
##--> comes with a large collection of 
# modules and packages(math , datetime, os )
# reduces the need to write the code 
# from scratch 

#7 -- dynamic typing 
# no need to declare variable types 
# explicitly
# 8 -- huge community support 
# active community with millions of developers
# tutorials , documentation , and resources

#9 -- Scalable and flexible 
# you can integrate python with C , C++ ,
#  java 
# and can be embedded into other applications 

#10 -- wide applications 
# web devepopment -- django , flask, streamlit 
# data sci and ai - Numpy , pandas , tensorflow
# automation -- selenium 
# game development -- pygame 
# desktop apps -- tkinter , PyQt 

##in short 
# python = simple + powerful + versatile- 
# " a programming language for all" 


## what is a variable ?
# a variable is like a container in programming that 
# stores  data or information.

#so here in python you dont need to declare the type of 
#variable. python automatically assign the type 
# #based on the value you give.
# 
# there are some rules for naming variables:
# 1 -- variable name can contain letters , numbers 
# and underscore(_), but cannot start with a number.
# ex -- age = 25    
#  user_name = "ace"
# 2name = "bob"   (wrong)

#2 -- variable names are case- sensitive.
# upper case and lower case characters are treated diff
age = 25 
AGE = 25
Age = 25 
#3 should not use python keywords (like if , while , for)
# as variable names.


## types of variables 
#1 - Local var--
#declared inside a function , accessible only inside that 
#function 
#2 global var
#declared outside all functions , 
#accessible anywhere in the code. 
#3 - constants  
# python doesnt have true constants 
#by convention we write them in ALL CAPITAL LETTERS.
#ex -- PI - 3.14
# GRAVITY = 9.8 

name = "ace"
# it a actual data 


##operators 
#operators are special symbols that perform
#  operations on variables and values.
#ex - + - addition 

# types of op 
#1 - arithmetic 
#2 - logical 
#3 - assignment 
#4 - comparison 
#5 - membership 
#6 - Bitwise 
#7 - identity

#1 arithmetic op 
#used for mathematical calculations 
# + - Addition - add two values 
# - - sub -- subtracts the right operand from the left 
# * - multiplication - multiplies two values
# / - divison - divides the left operand by the right 
# % - modulus - it will return the remainder as the 
# output 
# // - floor divison  - divides and return the 
#largest whole number(integer part only)
# ex - 7.5 --> 7 
# ** - exponent - returns the value of 
# x raised to the power of y.
## ex - 2**3 = 8 --> 2 * 2 * 2 = 8 
# 2^3 = 8

#2 comparison op 
# == - equal to 
# != - not equal to 
# > - greater than 
# < - less than 
# >= - greater than or equal to 
# <= - less than or equal to

#3 logical op --used when you have to combine multiple 
# conditions.
# and -- returns true if both the conditions are true
#or - returns true if either of the conditions is true
#not -- reverses the result

#4 assignment op = used to assign values to the variables.
# = - assign values to variables 
# += - add and assign 
# -= - subtract and assign 
# *= - multiply and assign 
# /= - divide and assign 
# %= - modulus and assign 
# //= - floor division and assign 
# **= - exponent and assign 
# &= - bitwise and and assign

#5 membership op 
# in - returns true if a sequence with the specified 
# value is present in the object 
# not in - returns true if a sequence with the specified 
# value is not present in the object

#6 identity op -- used to compare the object identity
# (memory location)
# is - returns true if both variables are the same
#  object
# is not - returns true if both 
# variables are not the same object

#7 bitwise op -- bascially work on binary numbers
# & - bitwise and -- it bascially set the bit to 1 if
#  both bits are 1
# | - bitwise or -- bit is 1 if atleast one is 1 
# ^ - bitwise xor -- bit is 1 if only one is 1
# ~ - bitwise not -- it inverts all the bits
# << - bitwise left shift -shift the bits to the left,
# (adds 0s on the right) 
#each left shift multiplies the number by 2

# >> - bitwise right shift
# each right shift divides the number by 2
#shift the bits to the right(remove bits from right )

# a = 6  #110
# b = 3  #011
##i  am taking and op 
#010 --- 2
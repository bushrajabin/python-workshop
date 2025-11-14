#64 Write a Python Program to demonstrate many Exception Handling?

#The try block will generate a NameError, because x is not defined:
try:
 print(x)
except NameError:
 print("Variable x is not defined")
except:
 print("Something else went wrong")

#1/0
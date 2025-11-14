#69 Write a Python Program to demonstrate raise in Exception Handling fortype?

#Raise a TypeError if x is not an integer:
y = "hello"
if not type(y) is int:
 raise TypeError("Only integers are allowed")
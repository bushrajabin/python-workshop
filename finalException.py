#66 Write a Python Program to demonstrate final in Exception Handling?
#The finally block gets executed no matter if the try block raises anyerrors or not:
try:
 print(x)
except:
 print("Something went wrong")
finally:
 print("The 'try except' is finished")
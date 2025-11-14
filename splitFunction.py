#52 write a Python program to demonstrate split() at each white-space character:
import re
#Split the string at every white-space character:
txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)
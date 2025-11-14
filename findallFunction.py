#50 write a Python program to demonstrate Regular expression findall search function?
import re
#Return a list containing every occurrence of "ai":
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)
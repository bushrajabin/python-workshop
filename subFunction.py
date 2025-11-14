#54 write a python program to demonstrate Replace of every white-spacecharacter with the number 8?
import re
#Replace all white-space characters with the digit "8":
txt = "The rain in Spain"
x = re.sub("\s", "8", txt)
print(x)
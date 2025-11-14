#51 write a Python program to demonstrate Search for the first white- space character in the string using Regular expression?

import re
txt = "The rain in Spain"
x = re.search("\s", txt)
print("The first white-space character is located in position:",
x.start())
#55 write a python program to demonstrate metacharcters ?
#[] A set of characters "[a-m]"
import re
txt = "The rain in Spain"
#Find all lower case characters alphabetically between "a" and "m":
x = re.findall("[a-m]", txt)
print(x)

#\ Signals a special sequence (can also be used to escape specialcharacters) "\d"
import re
txt = "That will be 59 dollars"
#Find all digit characters:
x = re.findall("\d", txt)
print(x)

#. Any character (except newline character) "he..o"
import re
txt = "hello world"
#Search for a sequence that starts with "he", followed by two (any)characters, and an "o":
x = re.findall("he..o", txt)
print(x)

#^ Starts with "^hello"
import re
txt = "hello world"
#Check if the string starts with 'hello':
x = re.findall("^hello", txt)
if x:


 print("Yes, the string starts with 'hello'")
else:
 print("No match")

#$ Ends with "world$"
import re
txt = "hello world"
#Check if the string ends with 'world':
x = re.findall("world$", txt)
if x:
 print("Yes, the string ends with 'world'")
else:
 print("No match")

#* Zero or more occurrences "aix*"

import re
txt = "The rain in Spain falls mainly in the plain!"
#Check if the string contains "ai" followed by 0 or more "x" characters:
x = re.findall("aix*", txt)
print(x)
if x:
 print("Yes, there is at least one match!")
else:
 print("No match")

# {} Exactly the specified number of occurrences "al{2}"
import re
txt = "The rain in Spain falls mainly in the plain!"
#Check if the string contains "a" followed by exactly two "l" characters:
x = re.findall("al{2}", txt)
print(x)
if x:
 print("Yes, there is at least one match!")
else:
 print("No match")

#| Either or "falls|stays"
import re
txt = "The rain in Spain falls mainly in the plain!"
#Check if the string contains either "falls" or "stays":
x = re.findall("falls|stays", txt)
print(x)
if x:
 print("Yes, there is at least one match!")
else:
 print("No match")
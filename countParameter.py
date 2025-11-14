import re
#Replace the first two occurrences of a white-space character with the digit 8:
txt = "The rain in Spain"
x = re.sub("\s", "8", txt, 2)
print(x)
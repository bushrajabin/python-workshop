#62 Write a Python Program to demonstrate Delete file?
#import os
#
#os.remove("myfile.txt")

import os
if os.path.exists("myfile.txt"):
 os.remove("myfile.txt")
else:
 print("The file does not exist")
#57 Write a Python Program to demonstrate readline() with differentmethod?
f = open("demofile.txt", "r")
print(f.read(5))

#You can return one line by using the readline() method:
f = open("demofile.txt", "r")
print(f.readline())

#By calling readline() two times, you can read the two first lines:
f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())

#By looping through the lines of the file, you can read the whole file, line by line:
f = open("demofile.txt", "r")
for x in f:
 print(x)
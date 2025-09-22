#27 write a python program to demonstrate break
for letter in 'Dept of CS&IT': # First Example
    if letter == '&':
     break
    print ('Current Letter :', letter)
var = 10 # Second Example
while var > 0:
      print ('Current variable value :', var)
      var = var -1
      if var == 5:
         break
print ("Good bye!")
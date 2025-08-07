import re  # Import the regular expression module

# List of strings to check
strings = ['789', '123', '004']

# Loop through each string
for s in strings:
   # Check if the string contains only octal digits using regex
   if re.fullmatch(r'[0-7]+', s):
      print(s," -> All are Octal Digits")
   else:
      print(s," -> All are not Octal Digits")
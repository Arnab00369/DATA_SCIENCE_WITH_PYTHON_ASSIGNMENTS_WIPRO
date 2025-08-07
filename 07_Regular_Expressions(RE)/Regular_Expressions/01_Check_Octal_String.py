import re  # Import the regular expression module

# List of strings to check
strings = ['789', '123', '004']

# Loop through each string
for s in strings:
   # Check if the string contains only octal digits using regex
   if re.fullmatch(r'[0-7]+', s):
      print(f"{s} -> ✅ Only Octal Digits")
   else:
      print(f"{s} -> ❌ Not Octal Digits")

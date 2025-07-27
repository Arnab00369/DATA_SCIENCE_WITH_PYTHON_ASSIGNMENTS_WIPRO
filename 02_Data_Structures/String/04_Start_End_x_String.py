# Question 4:
# Given a string, if the first or last character is 'x', return the string without those 'x' character, else return the string unchanged. If the input is "xHix", then output is "Hi".

# Taking input from user
String_1 = input("Enter a String: ")
# Checking if the string starts and ends with 'x'
if String_1.startswith('x'):
   String_1 = String_1[1:]
   if String_1.endswith('x'):
      String_1 = String_1[:-1]
      # Displaying the resulting string
      print("\nOUTPUT::\nResulting String: ",String_1)
   else:
      # Displaying the error message if the string does not end with 'x'
      print("\nString should start and end with 'x' to give an output.")
else:
      # Displaying the error message if the string does not start with 'x'
      print("\nString should start and end with 'x' to give an output.")

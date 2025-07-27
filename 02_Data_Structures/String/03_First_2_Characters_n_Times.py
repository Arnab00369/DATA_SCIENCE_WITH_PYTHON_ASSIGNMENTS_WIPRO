# Question 3:
# Given a string, return a new string made of n copies of the first 2 chars of the original string where n is the length of the string. The string ength will be >=2.

# If input is "Wipro" then output should be "WiWiwiwiwi".

# Taking input from user
String_1 = input("Enter a String: ")
# Checking if the string has at least 2 characters
# If the string is less than 2 characters, we will not proceed with the operation
if len(String_1) < 2:
   # Printing an error message if the string is too short
   print("String must have at least 2 characters.")
else:
   # Extracting the first two characters of the string
   first_two_chars = String_1[:2]
   # Taking input for the number of times to repeat the first two characters
   n = int(input("Enter the number of times to repeat the first two characters: "))
   result = first_two_chars * n
# Displaying the resulting string
   print("\nOUTPUT::\nResulting String:", result)
# Question 4:
# Write a function that accepts a string and prints the number of upper case letters and lower case letters in it.

# This function counts the number of upper and lower case letters in a given string.
def Str_upper_lower(String_1):
   # Initializing variables to store upper and lower case letters and their counts
   upper_case = ""
   lower_case = ""
   upper_count = 0
   lower_count = 0
   # Iterating through each character in the string
   print("\nOUTPUT::")
   for char in String_1:
      if char.isupper():
         upper_case += char + " "
         upper_count += 1
      elif char.islower():
         lower_case += char + " "
         lower_count += 1
   # Displaying the results
   print("\nUpper Case Letters: ",upper_case,"\nLower Case Letters: ",lower_case)
   print("Number of Upper case characters: ", upper_count)
   print("Number of Lower case characters: ", lower_count)

# Taking input from the user
String_1 = input("Enter a String to counnt upper and lower case letters: ")
# Calling the function to count upper and lower case letters
Str_upper_lower(String_1)


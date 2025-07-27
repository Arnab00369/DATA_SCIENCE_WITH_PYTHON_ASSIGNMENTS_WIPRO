# Question 2:
# Write a program that will check whether a given String is Palindrome or not.

# A Palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).
# Taking input from user
String_1 = input("Enter a String to check if it is a Palindrome String or not: ")
# Displaying the reverse string
print("\nReverse of String: ", String_1[::-1])
String_cpy = String_1
String_1 = String_1.lower()  # Convert to lowercase for case-insensitive comparison


# Checking if the string is a palindrome
if String_1 == String_1[::-1]:
      # If the string is equal to its reverse, it is a palindrome
      print(String_cpy," is a Palindrome String")
else:
      print(String_cpy," is not a Palindrome String")
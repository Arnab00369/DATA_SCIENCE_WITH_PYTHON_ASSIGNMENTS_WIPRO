# Question 2:

String_1 = input("Enter a String to check if it is a Palindrome String or not: ")
print("\nReverse of String: ", String_1[::-1])
String_cpy = String_1
String_1 = String_1.lower()  # Convert to lowercase for case-insensitive comparison
if String_1 == String_1[::-1]:
      print(String_cpy," is a Palindrome String")
else:
      print(String_cpy," is not a Palindrome String")
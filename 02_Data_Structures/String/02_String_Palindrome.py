String_1 = input("Enter a String to check if it is a Palindrome String or not: ")

String_1 = String_1.lower()  # Convert to lowercase for case-insensitive comparison
if String_1 == String_1[::-1]:
      print(String_1," is a Palindrome String")
else:
      print(String_1," is not a Palindrome String")
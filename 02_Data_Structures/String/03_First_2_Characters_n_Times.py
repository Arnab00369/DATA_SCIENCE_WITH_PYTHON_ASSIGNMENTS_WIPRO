# Question 3:

String_1 = input("Enter a String: ")

if len(String_1) < 2:
   print("String must have at least 2 characters.")
else:
   first_two_chars = String_1[:2]
   n = int(input("Enter the number of times to repeat the first two characters: "))
   result = first_two_chars * n
   print("\nOUTPUT::\nResulting String:", result)
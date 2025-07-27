# Question 5:
# Given a string and an integer n, return a string made of n repetitions of the last n characters of the string. You may assume that n is between 0 and the length of the string inclusive. For example if the inputs are "Wipro" and 3, then the output should be "propropro".

# Taking input from user
String_1 = input("Enter a String: ")
# Checking if the string has at least n characters
n_Times = int(input("Enter the number of times to repeat the last two characters: "))
# Checking if n_Times is within the valid range
if 0 <= n_Times <= len(String_1):
      part = String_1[-n_Times:]
      result = part * n_Times
      # Displaying the resulting string
      print("\nOUTPUT::\nResulting String: ", result)
else:
      # Displaying an error message if n_Times is not valid
      print("Invalid value of 'n'. Check your input and try again")
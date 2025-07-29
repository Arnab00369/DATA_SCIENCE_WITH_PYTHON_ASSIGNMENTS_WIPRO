# Question 3:
# Write a function to calculate and return the factorial of a number (a non-negative integer).

# Defining the function to calculate factorial
def factorial(number):
   fact = 1
   # Loop to calculate factorial
   for i in range(1,number+1):
      # Multiplying each number from 1 to the given number
      fact *= i
   return fact


# Taking input from the user
number = int(input("Enter a non-negative integer: "))
# Checking if the number is negative
if number < 0:
   print("The number is negative!! Check your input again and try again.")
# If the number is non-negative, calculate and display the factorial
else:
   print("\nOUTPUT::\nThe factorial of ",number," = ",factorial(number))
# Question 1:
# Write a program to accept two numbers from the user and perform division. If any exception occurs, print an error message or else print the result.

# Program to accept two numbers and perform division with exception handling

try:
   # Accept first number from user and convert to float
   num1 = float(input("Enter first number: "))
   
   # Accept second number from user and convert to float
   num2 = float(input("Enter second number: "))

   # Perform division
   result = num1 / num2

   # Display the result
   print("Result of division:", result)

# Handle division by zero error
except ZeroDivisionError:
   print("Error: Cannot divide by zero.")

# Handle error if the user input is not a valid number
except ValueError:
   print("Error: Please enter valid numeric values.")

# Catch any other unexpected exceptions
except Exception as e:
   print("Unexpected error:", str(e))

# This block runs only if no exception was raised
else:
   print("Division performed successfully.")

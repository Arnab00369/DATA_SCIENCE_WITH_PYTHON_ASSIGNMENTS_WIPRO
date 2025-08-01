# Question 3:
# Write a program to accept 10 numbers through command line arguments and calculate the sum of prime numbers among them.

# Import argv from sys to use command-line arguments
from sys import argv

# Also importing entire sys module for potential other uses (like sys.exit)
import sys

# Define a function to check whether a number is prime
def is_prime(n):
   # Prime numbers must be greater than 1
   if n <= 1:
      return False
   
   # 2 is the only even prime number
   if n == 2:
      return True

   # Eliminate all other even numbers greater than 2
   if n % 2 == 0:
      return False

   # Check for divisibility from 3 to √n using only odd numbers
   for i in range(3, int(n**0.5) + 1, 2):
      if n % i == 0:
         return False
   
   # If none of the above conditions are met, number is prime
   return True


# Check if exactly 10 numbers are provided
if len(sys.argv) != 11:
   print("Please enter exactly 10 numbers as command-line arguments.")
   sys.exit(1)

# Convert arguments to integers
numbers = [int(arg) for arg in sys.argv[1:]]

# Calculate sum of prime numbers
prime_sum = sum(num for num in numbers if is_prime(num))

print("Sum of prime numbers:", prime_sum)

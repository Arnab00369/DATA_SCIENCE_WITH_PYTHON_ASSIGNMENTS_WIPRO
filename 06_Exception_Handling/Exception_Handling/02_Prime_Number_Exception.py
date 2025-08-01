# Question 2:
# Write a program to accept a number from the user and check whether it's prime or not. If user enters anything other than number, handle the exception and print an error message.

# Function to check if a number is prime
def is_prime(n):
   # Prime numbers are greater than 1
   if n <= 1:
      return False

   # Check divisibility up to square root of n
   for i in range(2, int(n**0.5) + 1):
      if n % i == 0:
            return False  # Found a divisor, not prime

   return True  # No divisors found, it's a prime number

try:
   # Ask the user to input a number
   num = int(input("Enter a number: "))

   # Check if the number is prime
   if is_prime(num):
      print(num, "is a prime number.")
   else:
      print(num, "is not a prime number.")

# Handle non-integer input error
except ValueError:
   print("Error: Please enter a valid integer.")

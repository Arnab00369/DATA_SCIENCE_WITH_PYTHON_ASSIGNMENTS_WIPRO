from sys import argv
import sys
def is_prime(n):
   if n <= 1:
      return False
   if n == 2:
      return True
   if n % 2 == 0:
      return False
   for i in range(3, int(n**0.5) + 1, 2):
      if n % i == 0:
            return False
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

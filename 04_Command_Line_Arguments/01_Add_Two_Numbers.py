# Question 1:
# Write a program to accept two numbers as command line arguments and display their sum.

# Importing argv from the sys module to access command-line arguments
from sys import argv

# Print a header for the output
print("\nOUTPUT::")

# Print the first number passed through command line
print("Number 1 = ", argv[1])

# Print the second number passed through command line
print("Number 2 = ", argv[2])

# Convert both arguments to integers and print their sum
print("Sum of given two numbers = ", int(argv[1]) + int(argv[2]))

# Question 2:
# Write a program to accept a welcome message through command line arguments and display the file name along with the welcome message.

# Import argv from the sys module to work with command-line arguments
from sys import argv

# Print a welcome message
print("\nOUTPUT::\nWelcome to the Command Line Arguments Program!!")

# argv[0] always contains the name of the Python file being executed
print("The File Name is = ", argv[0])

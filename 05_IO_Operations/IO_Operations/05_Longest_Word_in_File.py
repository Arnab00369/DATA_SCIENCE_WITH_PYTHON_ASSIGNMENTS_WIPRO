# Question 5:
# Write a program to find the longest word from the txt file contents, assuming that the file will have only one longest word in it.

# Ask the user to input the filename to read from
filename = input("Enter the filename: ")

# Open the file in read mode
with open(filename, 'r') as file:
   # Read the entire content and split it into words (by default, splits on whitespace)
   words = file.read().split()

# Use the built-in max() function to find the longest word
# 'key=len' tells max() to compare words by their length
longest = max(words, key=len)

# Display the longest word found in the file
print("The longest word is:", longest)

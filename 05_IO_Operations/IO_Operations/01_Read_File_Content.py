# Question 1:
# Write a program to read the entire content from a txt file and display it to the user.

# Prompt the user to enter the filename (e.g., 'Demo.txt')
filename = input("Enter the filename: ")

# Open the file in read mode
with open(filename, 'r') as file:
   # Read the entire content of the file into a single string
   content = file.read()

# Print a separator and then the entire content of the file
print("\nFile Content:\n")
print(content)


# Question 3:
# Write a program to accept input from user and append it to a txt file.

# Ask the user to input the filename to which data should be appended
filename = input("Enter the filename: ")

# Ask the user to input the data/text they want to append to the file
data = input("Enter text to append to the file: ")

# Open the file in 'append' mode ('a') which means:
# - If the file exists, new data will be added to the end of the file
# - If the file does not exist, it will be created
with open(filename, 'a') as file:
   # Write the user input to the file followed by a newline character
   file.write(data + "\n")

# Inform the user that the data has been successfully appended
print("Data appended successfully.")


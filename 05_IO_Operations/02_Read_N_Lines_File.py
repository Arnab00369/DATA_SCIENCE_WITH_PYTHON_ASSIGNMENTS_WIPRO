# Question 2:
# Write a program to read first n lines from a txt file. Get n as user input.

# Prompt the user to enter the filename (e.g., 'Demo.txt')
filename = input("Enter the filename: ")

# Prompt the user to enter how many lines they want to read from the file
n = int(input("Enter number of lines to read: "))

# Open the file in read mode using 'with' to ensure proper closing of the file
with open(filename, 'r') as file:
   # Loop to read 'n' lines one by one
   for i in range(n):
      # Read a single line from the file
      line = file.readline()

      # If the line is empty, it means end of file (EOF) is reached
      if line == '':
            break  # Exit the loop if there are no more lines to read

      # Print the line number and the line content (stripped of extra whitespace)
      print("Line", (i+1), ":", line.strip())
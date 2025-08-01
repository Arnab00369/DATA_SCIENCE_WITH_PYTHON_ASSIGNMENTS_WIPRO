# Question 4:
# Write a program to read contents from a txt file line by line and store each line into a list.

# Ask the user to input the filename from which to read the lines
filename = input("Enter the filename: ")

# Initialize an empty list to store each line from the file
lines_list = []

# Open the file in read mode ('r')
with open(filename, 'r') as file:
   # Read each line in the file one by one
   for line in file:
      # Strip leading/trailing whitespace (like '\n') and append to the list
      lines_list.append(line.strip())

# Display the list containing all lines
print("\n📄 Lines stored in list:")
print(lines_list)

# Print each line on a separate line from the list
print("\n📌 Each Line printed separately:\n")
for items in lines_list:
   print(items, end="\n")

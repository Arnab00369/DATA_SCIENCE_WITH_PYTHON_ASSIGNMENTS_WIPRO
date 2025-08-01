# Program 1: Read the entire content of a text file

filename = input("Enter the filename: ")

with open(filename, 'r') as file:
   content = file.read()

print("\nFile Content:\n")
print(content)

# Program 3: Accept user input and append to a text file

filename = input("Enter the filename: ")
data = input("Enter text to append to the file: ")

with open(filename, 'a') as file:
   file.write(data + "\n")

print("Data appended successfully.")

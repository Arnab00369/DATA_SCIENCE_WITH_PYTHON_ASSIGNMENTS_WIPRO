# Program 5: Find the longest word in a text file

filename = input("Enter the filename: ")

with open(filename, 'r') as file:
   words = file.read().split()

longest = max(words, key=len)

print("The longest word is:", longest)

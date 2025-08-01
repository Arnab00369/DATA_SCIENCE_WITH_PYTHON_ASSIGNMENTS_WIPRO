# Question 6:
# Write a program to count the frequency of a user entered word in a txt file.

# Ask the user to input the filename to read from
filename = input("Enter the filename: ")

# Ask the user to input the word to search for
search_word = input("Enter the word to search: ")

# Open the file in read mode
with open(filename, 'r') as file:
   # Read the full content of the file into a single string
   content = file.read()

# Split the content into a list of words (splits on whitespace by default)
# and count how many times the search_word appears
# ⚠️ This is case-sensitive
count = content.split().count(search_word)

# Print the result
print("The word", search_word, "appears", count, "times in the file.")


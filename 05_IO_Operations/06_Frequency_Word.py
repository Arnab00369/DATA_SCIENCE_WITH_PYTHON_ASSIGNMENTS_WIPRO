# Program 6: Count frequency of a user-entered word in a file

filename = input("Enter the filename: ")
search_word = input("Enter the word to search: ")

with open(filename, 'r') as file:
   content = file.read()

# Case-insensitive count (optional: use .lower() for both)
count = content.split().count(search_word)

print(f"The word '{search_word}' appears {count} times in the file.")

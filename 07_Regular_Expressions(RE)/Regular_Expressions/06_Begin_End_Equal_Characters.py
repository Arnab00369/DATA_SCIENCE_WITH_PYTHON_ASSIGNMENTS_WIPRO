# Given list of words
words = ["civic", "trust", "widows", "maximum", "museums", "aa", "as"]

# Create an empty list to hold matching words
matching_words = []

# Loop through each word
for word in words:
   # Compare first and last character (case-insensitive)
   if word[0].lower() == word[-1].lower():
      matching_words.append(word)

# Print the results
print("Words that start and end with the same character:")
print(matching_words)

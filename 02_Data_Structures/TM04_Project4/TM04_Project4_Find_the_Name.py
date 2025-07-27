# # Project 4:
# Given a string of n words, help Alex to find out how many times his name appears in the string.

# Constraint: 1 <= n <= 200

# Sample input: Hi Alex WelcomeAlex Bye Alex.

# Sample output: 3

# Explanation: Alex name appears 3 times in the string. Hi Alex WelcomeAlex Bye Alex.

text = input("Enter a string: ")

# Count using a simple loop (without using string functions)
count = 0
words = text.split()  # split string into words

for word in words:
   if word == "Alex" or word == "Alex.":  # cover cases like "Alex."
      count += 1

print("\nOUTPUT::\nAlex appears", count, "times.")

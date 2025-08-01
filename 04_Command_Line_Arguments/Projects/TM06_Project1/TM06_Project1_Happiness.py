# Project 1:

from sys import argv
import sys

# Ensure exactly 3 arguments are passed
if len(sys.argv) != 4:
   print("There should be exactly 3 command-line arguments: likes, dislikes, and inputs. Check your input")
   sys.exit(1)

# Extract and convert command-line arguments into sets/lists of integers
like_str = sys.argv[1]
dislike_str = sys.argv[2]
input_str = sys.argv[3]

# Convert hyphen-separated strings to sets/lists of integers
likes = set(map(int, like_str.split('-')))
dislikes = set(map(int, dislike_str.split('-')))
inputs = list(map(int, input_str.split('-')))

# Initialize happiness
happiness = 0

# Calculate happiness
for num in inputs:
   if num in likes:
      happiness += 1
   elif num in dislikes:
      happiness -= 1

# Output final happiness
print("Your Happiness Index is now = ",happiness)

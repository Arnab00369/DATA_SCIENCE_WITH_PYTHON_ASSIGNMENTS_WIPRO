# Project 1:
# Write a Python function that accepts a hyphen-separated sequence of colors as input and returns the colors in a hyphen-separated sequence after sorting them alphabetically.

# Constraint: All the colors will be completely in either lower case or upper case.

# Sample input 1: green-red-yellow-black-white

# Sample output 1: black-green-red-white-yellow

# Sample input 2: PINK-BLUE-TAN-PURPLE

# Sample output 2: BLUE-PINK-PURPLE-TAN

# Defining a function to sort colors
def sort_colors(color_input):
   color_list = color_input.split('-')   # Split on hyphen
   color_list.sort()                     # Sort alphabetically
   sorted_colors = '-'.join(color_list)  # Join back with hyphen
   return sorted_colors

# Test input from user
input_colors = input("Enter hyphen-separated colors (all lowercase or uppercase): ")
# Calling the function and printing the output
output = sort_colors(input_colors)
print("\nOUTPUT::\nSorted colors:", output)

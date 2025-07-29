def sort_colors(color_input):
   color_list = color_input.split('-')   # Split on hyphen
   color_list.sort()                     # Sort alphabetically
   sorted_colors = '-'.join(color_list)  # Join back with hyphen
   return sorted_colors

# Test input
input_colors = input("Enter hyphen-separated colors (all lowercase or uppercase): ")
output = sort_colors(input_colors)
print("\nOUTPUT::\nSorted colors:", output)

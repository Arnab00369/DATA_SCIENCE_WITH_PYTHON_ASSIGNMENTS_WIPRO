# Question 2:
# Write a program to append a new item to the end of the list.

# Creating a list with mixed data types
list_new = [1, '2', 'Arnab', 40.6, 'true']

# Displaying the list items before appending
print("The elements in the list before append are as follows:")
for item in list_new:
   print(item)
list_new.append(6)

# Displaying the list items after appending
print("\nThe elements in the list after append are as follows:")
for item in list_new:
   print(item)

print("New item added is = 6")
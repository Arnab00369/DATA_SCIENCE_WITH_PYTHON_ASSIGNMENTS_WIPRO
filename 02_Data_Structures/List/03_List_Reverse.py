# Question 3:
# Write a program to reverse the order of the items in the list.

# Creating a list with mixed data types
list_1 = [20, 'Arnab', '@', 36.8, 'Data']

# Displaying the list items in original order
print("The elements in the list in original order are as follows:")
for item in list_1:
   print(item)

# Reversing the list
list_1.reverse()

# Displaying the elements in reverse order 
print("\nThe elements in the list in reverse order are as follows:")
for item in list_1:
   print(item)

# Question 8:
# Write a program to remove the first occurrence of a specified element from a list.

# Taking input from the user to create a list
list_new = input("Enter the elements of the list separated by commas: ").split(',')
# Converting the input string elements to a list
print("The elements in the list are:")
for items in list_new:
   print(items)
# Asking the user for the element to remove
item_to_remove = input("\nEnter the element whose first occurrence is to be removed: ")
# Checking if the item exists in the list and removing the first occurrence
# If the item is not found, it will print a message
if item_to_remove in list_new:
   print("Removing the first occurrence of:", item_to_remove)
   list_new.remove(item_to_remove)
else:
   print("Item not found in the list. Enter element which is present in the list.")
# Printing the updated list after removal
print("\nThe elements in the list after removal of ",item_to_remove," are:")
for items in list_new:
   print(items)
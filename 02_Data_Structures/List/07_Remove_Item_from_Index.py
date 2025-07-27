# Question 7:
# Write a program to remove the item from a specified index in a list.

# Taking input from the user to create a list
list_new = input("Enter the elements of the list separated by commas: ").split(',')
# Converting the input string elements to a list
print("The elements in the list are:")
counter = 0
for items in list_new:
   counter += 1
   print("Position = ", counter, " ==> Element = ", items)
   
   
# Display the elements
index_remove_item = int(input("\nEnter the index of the item to remove: "))
print("To be removed element = ",list_new[index_remove_item-1]," at postion ",index_remove_item,"\n")
list_new.pop(int(index_remove_item-1))
# Printing the updated list after removing the item
counter_1 = 0
for items in list_new:
   counter_1 += 1
   print("Position = ", counter_1, " ==> Element = ", items)
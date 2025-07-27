# Question 1:
# Write a program to remove a given item from the set.

# Defining a set with mixed data types
set_1 = {'Arnab', 36, 'Python', 'true', 10,  20}
print('The elements of set already defined are: ')
for item in set_1:
   print(item)

# Asking user to input the item to be removed from the set
item_remove = input("\nEnter the item you want to remove from the set: ")
# Checking if the input is a digit and converting it to an integer if it is
if item_remove.isdigit():
   item_remove = int(item_remove)
# Checking if the item exists in the set
if item_remove in set_1:
      set_1.remove(item_remove)
      # Displaying the set after removing the item
      print("Item ",item_remove," has been removed from the set.") 
      print('The new set with removed item is: ')
      for item in set_1:
         print(item)
else:
      print("Item ",item_remove," is not present in the set. No changes made.")
      print('The set remains unchanged: ')
      for item in set_1:
         print(item)
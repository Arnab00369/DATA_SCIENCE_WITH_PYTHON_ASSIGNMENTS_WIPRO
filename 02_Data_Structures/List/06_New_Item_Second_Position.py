# # Question 6:
# Write a program to insert a new item before the second element in an existing list.

# Taking input from the user to create a list
list_new = input("Enter the elements of the list separated by commas: ").split(',')
# Converting the input string elements to a list
print("The elements in the list with respective positions before adding a new item are:")
# Iterating through the list to print each element with its position
counter = 0
for items in list_new:
   counter += 1
   print("Position = ",counter," ==> Element = ",items)

# Inserting a new item before the second element in the existing list
insert_item = input("\nEnter an elements to insert before the 2nd element in the exisitng list: ")  
# # Printing the current 2nd position element before insertion
print("Current 2nd position element is: ",list_new[1],"\n")
list_new.insert(1, insert_item)
# Printing the updated list with the new item inserted
counter_1 = 0
for items in list_new:
   counter_1 += 1
   print("Position = ",counter_1," ==> Element = ",items)
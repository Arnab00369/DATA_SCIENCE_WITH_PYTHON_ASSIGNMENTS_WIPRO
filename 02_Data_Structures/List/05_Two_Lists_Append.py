# Question 5:
# Write a program to append the items of list1 to list2 in the front.

list_1 = input("Enter the elements of List 1 separated by commas: ").split(',')
print("The elements of List 1 are:")
for item in list_1:
   print(item)  # Remove any leading/trailing whitespace

list_2 = input("Enter the elements of List 2 separated by commas: ").split(',')
print("The elements of List 2 are:")
for item in list_2:
   print(item) 

# Appending items of list_1 to list_2
for items in list_1:
   list_2.append(items)
# Printing the updated list_2
print("The elements of appended list are:")
for items in list_2:
   print(items)
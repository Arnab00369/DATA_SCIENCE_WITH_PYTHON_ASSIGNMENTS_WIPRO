list_new = input("Enter the elements of the list separated by commas: ").split(',')

print("The elements in the list are:")
for items in list_new:
   print(items)

item_to_remove = input("\nEnter the element whose first occurrence is to be removed: ")

if item_to_remove in list_new:
   print("Removing the first occurrence of:", item_to_remove)
   list_new.remove(item_to_remove)
else:
   print("Item not found in the list. Enter element which is present in the list.")

print("\nThe elements in the list after removal of ",item_to_remove," are:")
for items in list_new:
   print(items)
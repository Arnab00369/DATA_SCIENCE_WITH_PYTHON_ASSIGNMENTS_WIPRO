list_new = input("Enter the elements of the list separated by commas: ").split(',')

print("The elements in the list are:")
counter = 0
for items in list_new:
   counter += 1
   print("Position = ", counter, " ==> Element = ", items)
   # Display the elements

index_remove_item = input("Enter the index of the item to remove: ")

list_new.pop(index_remove_item)

counter_1 = 0
for items in list_new:
   counter_1 += 1
   print("Position = ", counter_1, " ==> Element = ", items)
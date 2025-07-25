set_1 = {'Arnab', 36, 'Python', 'true', 10,  20}
print('The elements of set already defined are: ')
for item in set_1:
   print(item)


item_remove = input("\nEnter the item you want to remove from the set: ")

if item_remove.isdigit():
   item_remove = int(item_remove)

if item_remove in set_1:
      set_1.remove(item_remove)
      print("Item ",item_remove," has been removed from the set.") 
      print('The new set with removed item is: ')
      for item in set_1:
         print(item)
else:
      print("Item ",item_remove," is not present in the set. No changes made.")
      print('The set remains unchanged: ')
      for item in set_1:
         print(item)
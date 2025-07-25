set_1 = {'Arnab', 36, 'Python', 'true', 10.6,  20}

print('The set already created is: ',set_1)

item_remove = input("Enter the item you want to remove from the set: ")

if item_remove in set_1:
   set_1.remove(item_remove)
   print("Item ",item_remove," has been removed from the set.") 
   print('The new set with removed item is: ',set_1)
list_new = input("Enter the elements of the list separated by commas: ").split(',')

print("The elements in the list with respective positions before adding a new item are:")

counter = 0
for items in list_new:
   counter += 1
   print("Position = ",counter," ==> Element = ",items)
   
insert_item = input("Enter an elements to insert before the 2nd element in the exisitng list: ")  

list_new.insert(1, insert_item)

for items in list_new:
   print(items)
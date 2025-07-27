list_new = input("Enter the elements of the list separated by commas: ").split(',')

print("The elements in the list with respective positions before adding a new item are:")

counter = 0
for items in list_new:
   counter += 1
   print("Position = ",counter," ==> Element = ",items)
   
insert_item = input("\nEnter an elements to insert before the 2nd element in the exisitng list: ")  

print("Current 2nd position element is: ",list_new[1],"\n")
list_new.insert(1, insert_item)

counter_1 = 0
for items in list_new:
   counter_1 += 1
   print("Position = ",counter_1," ==> Element = ",items)
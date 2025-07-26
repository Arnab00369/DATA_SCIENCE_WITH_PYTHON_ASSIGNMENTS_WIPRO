list_input = input("Enter the elements of the list separated by commas: ")

list_new = list_input.split(',')
print("The elements in the list are as follows:")
for item in list_new:
   print(item.strip())

item_count = input("\nEnter the element in the list whose frequency you want to find: ")
occurence = list_new.count(item_count)

print("The occurence of the item ",item_count, "in the list is: ", occurence)
list_1 = input("Enter the elements of List 1 separated by commas: ").split(',')
print("The elements of List 1 are:")
for item in list_1:
   print(item)  # Remove any leading/trailing whitespace

list_2 = input("Enter the elements of List 2 separated by commas: ").split(',')
print("The elements of List 2 are:")
for item in list_2:
   print(item) 

append_list = list_2.append(list_1)

print("The elements of appended list are:")
for items in append_list:
   print(items)
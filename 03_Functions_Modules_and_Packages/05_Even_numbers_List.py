def even_list(list_input):
   even_numbers = []
   for item in list_input:
      if int(item) % 2 == 0:
            even_numbers.append(int(item))
   return even_numbers

list_input = input("Enter the numbers in the list you want to filter, separated by commas: ").split(',')

print("\nOUTPUT::\nThe even numbers in the list are: ", even_list(list_input))
print("Even elements in the list are: ")
for items in even_list(list_input):
   print(items, end=" ")
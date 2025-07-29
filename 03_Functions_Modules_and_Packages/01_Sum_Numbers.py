
def sum_list(list_input):
   sum = 0
   for items in list_input:
      sum += int(items)
   return sum

list_input = input("Enter the numbers in the list you want to add, separated by commas: ").split(',')


print("The sum of the elements in the list are = ",sum_list(list_input))

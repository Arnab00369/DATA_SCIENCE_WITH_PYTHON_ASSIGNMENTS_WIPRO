# Question 1:
# Write a function to return the sum of all numbers in a list.
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20

# Defining the function to return the sum of all numbers in a list
def sum_list(list_input):
   sum = 0
   # Iterating through the list and adding each element to the sum
   for items in list_input:
      sum += int(items)
   return sum

# Taking input from the user
list_input = input("Enter the numbers in the list you want to add, separated by commas: ").split(',')
# Displaying the required output
print("The sum of the elements in the list are = ",sum_list(list_input))
# Question 5:
# Write a function to print the even numbers from a given list. List is passed to the function as an argument.

# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result : [2, 4, 6, 8]

# Defining the function to filter even numbers from a list
def even_list(list_input):
   even_numbers = []
   for item in list_input:
      if int(item) % 2 == 0:
            even_numbers.append(int(item))
   return even_numbers

# Taking input from the user
list_input = input("Enter the numbers in the list you want to filter, separated by commas: ").split(',')
# Displaying the output
print("\nOUTPUT::\nThe even numbers in the list are: ", even_list(list_input))
print("Even elements in the list are: ")
for items in even_list(list_input):
   print(items, end=" ")
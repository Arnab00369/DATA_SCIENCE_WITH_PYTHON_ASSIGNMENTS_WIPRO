# Question 3:
# Write a program to convert a list into a tuple.

# This program converts a list of integers into a tuple and displays the elements of both the list and the tuple.
list_1 = [1, 2, 30, 40, 500, 600, 7000, 8000, 900000]
# Displaying the elements of the list
print("The elements of List are::\n", list_1, "\n")
counter = 0
for items in list_1:
   counter += 1
   print("Value ",counter," = ",items)


# Coverting list to tuple
tuple_1 = tuple(list_1)
# Displaying the elements of the tuple after conversion
print("\nThe elements of Tuple after converting from list are::\n",tuple_1, "\n")
counter_1 = 0
for items in list_1:
   counter_1 += 1
   print("Value ",counter_1," = ",items)
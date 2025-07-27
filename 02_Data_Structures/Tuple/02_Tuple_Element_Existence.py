# Question 2:
# Write a program to check whether an element exists in a tuple or not.

# Defining a tuple with 10 elements
tuple_1 = (10, 20, 30, 40, 50, 60, 70, 80, 90)
print("The elements of Tuple are::\n", tuple_1, "\n")
counter = 0
for items in tuple_1:
   counter += 1
   print("Value ",counter," = ",items)
# # Asking user to input an element to check its existence in the tuple
item_find = int(input("\nEnter an element to find it exists in the tuple or not: "))

# Checking if the item exists in the tuple 
if item_find in tuple_1:
   print("Element", item_find, "exists in the tuple.")
else:
   print("Element", item_find, "does not exist in the tuple.")
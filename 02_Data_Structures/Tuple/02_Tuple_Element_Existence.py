tuple_1 = (10, 20, 30, 40, 50, 60, 70, 80, 90)
print("The elements of Tuple are::\n", tuple_1, "\n")
counter = 0
for items in tuple_1:
   counter += 1
   print("Value ",counter," = ",items)

item_find = input("\nEnter an element to find it exists in the tuple or not: ")

if item_find in tuple_1:
   print("Element", item_find, "exists in the tuple.")
else:
   print("Element", item_find, "does not exist in the tuple.")
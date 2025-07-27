tuple_1 = (111, 256, 348, 789, 123, 456, 789, 1009)

print("The elements of Tuple are::\n", tuple_1, "\n")
counter = 0
index = 0
for items in tuple_1:
   counter += 1
   print("Value ", counter, " = ", items)

item_index = int(input("\nEnter the element in the tuple of the element to find its index: "))

if item_index in tuple_1:
   print("\nThe index of element ",item_index," in the tuple is: ",tuple_1.index(item_index))
else:
   print("\nElement ",item_index," does not exist in the tuple. Check your input and try again!!")
# Question 4:
# Write a program to find the maximum and minimum value in a set.

# Defining a set with mixed data types
set_data = {60, 20, 40, 50.9, 90, 100.6}
# Displaying the elements of the set
print('The elements of the set are:')
for item in set_data:
   print(item)
# # Finding the maximum and minimum elements in the set
max_element = max(set_data)
min_element = min(set_data)

# Displaying the maximum and minimum elements
print("\nThe maximum element in the set is:", max_element)
print("The minimum element in the set is:", min_element)
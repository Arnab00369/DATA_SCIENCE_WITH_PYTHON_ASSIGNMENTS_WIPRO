# Question 3:
# Write a program to create an union of sets.

# Defining two sets with mixed data types
set_1 = {60, 'Practice', 'Arnab', 16, 'Set'}
print('The elements of the Set 1 are:')
for item in set_1:
   print(item)

set_2 = {10, 'Yes', 'Data', 50, 'Intersection'}
print('\nThe elements of the Set 2 are:')
for item in set_2:
   print(item)

# Creating a union of the two sets
# The union operation combines all unique elements from both sets
set_3_union = set_1.union(set_2)
# Displaying the union of the two sets
print('\nThe union of Set 1 and Set 2 is(are):')
for item in set_3_union:
   print(item)
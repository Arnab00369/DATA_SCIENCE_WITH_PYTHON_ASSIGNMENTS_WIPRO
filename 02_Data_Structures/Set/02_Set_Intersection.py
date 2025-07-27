# Question 2:
# Write a program to create an intersection of sets.

# Defining two sets with mixed data types
set_1 = {60, 'Practice', 'Arnab', 16, 'Set'}
print('The elements of the Set 1 are:')
for item in set_1:
   print(item)
# Defining another set with mixed data types
set_2 = {60, 'Yes', 'Arnab', 50, 16, 'Intersection'}
print('\nThe elements of the Set 2 are:')
for item in set_2:
   print(item)

# Creating an intersection of the two sets
# The intersection operation finds common elements between both sets
set_3_intersect = set_1.intersection(set_2)
# Displaying the intersection of the two sets
print('\nThe intersection of Set 1 and Set 2 (common elements between both sets) is(are):')
for item in set_3_intersect:
   print(item)
# Question 3:

set_1 = {60, 'Practice', 'Arnab', 16, 'Set'}
print('The elements of the Set 1 are:')
for item in set_1:
   print(item)

set_2 = {10, 'Yes', 'Data', 50, 'Intersection'}
print('\nThe elements of the Set 2 are:')
for item in set_2:
   print(item)

set_3_union = set_1.union(set_2)
print('\nThe union of Set 1 and Set 2 is(are):')
for item in set_3_union:
   print(item)
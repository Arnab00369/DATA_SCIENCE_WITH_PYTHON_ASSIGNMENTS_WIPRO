set_1 = {60, 'Practice', 'Arnab', 16, 'Set'}
print('The elements of the Set 1 are:')
for item in set_1:
   print(item)

set_2 = {60, 'Yes', 'Arnab', 50, 16, 'Intersection'}
print('\nThe elements of the Set 2 are:')
for item in set_2:
   print(item)

set_3_intersect = set_1.intersection(set_2)
print('\nThe intersection of Set 1 and Set 2 (common elements between both sets) is(are):')
for item in set_3_intersect:
   print(item)
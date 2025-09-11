# Defined List
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# cube every number using lambda and map
cubes_list = list(map(lambda x: x**3, list_1))

print("Original List:", list_1)
print("Cubes:", cubes_list)

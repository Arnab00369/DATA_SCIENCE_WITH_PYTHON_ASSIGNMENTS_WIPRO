dict_integer = {
      1: 10,
      2: 20,
      3: 30,
      4: 40,
      5: 50,
      6: 60,
      7: 70,
      8: 80,
      9: 90,
      10: 100
}

print("The elements of Dictionary are::\nKey Value Pair format::\n", dict_integer, "\n")
elements = 0
for items in dict_integer:
   elements += 1
   print("Position = ", elements, " ==> Key = ", items, "\twith Value = ", dict_integer[items])

sum_values = 0
for items in dict_integer:
   sum_values += dict_integer[items]

print("\nThe sum of all values in the dictionary is:", sum_values)
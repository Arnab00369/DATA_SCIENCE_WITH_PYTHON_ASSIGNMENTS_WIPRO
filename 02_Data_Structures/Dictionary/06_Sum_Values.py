# Question 6:
# Write a program to sum all the values in a  dictionary, considering the values will be of int type.

# Defining a dictionary with integer keys and values
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

# Displaying the elements of the dictionary
print("The elements of Dictionary are::\nKey Value Pair format::\n", dict_integer, "\n")
elements = 0
# Iterating through the dictionary to print each key-value pair
for items in dict_integer:
   elements += 1
   print("Position = ", elements, " ==> Key = ", items, "\twith Value = ", dict_integer[items])

sum_values = 0
for items in dict_integer:
   sum_values += dict_integer[items]
# Calculating the sum of all values in the dictionary
# This assumes all values are integers
print("\nThe sum of all values in the dictionary is:", sum_values)
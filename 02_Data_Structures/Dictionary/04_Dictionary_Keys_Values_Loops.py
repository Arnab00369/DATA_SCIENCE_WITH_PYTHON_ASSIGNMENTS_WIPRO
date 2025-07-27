# Question 4:
# Write a program to iterate over a dictionary using for loop and print the keys alone, values alone and both keys and values.

# Creating a dictionary with mixed key types
dict_new = {
      "Name": "Arnab",
      "Course": "Python",
      3: "Data Structures",
      4: 90,
      5: 40.6
}
# Displaying the elements of the dictionary
print("The elements of Dictionary are::\nKey Value Pair format::\n", dict_new,"\n")
elements = 0
for items in dict_new:
   elements += 1
   print("Position = ",elements," ==> Key = ",items," with Value = ", dict_new[items])
# Iterating and printing both keys and values
counter = 0
print("\nIterating and printing only keys:")
for items in dict_new.keys():
   counter += 1
   print("Key ",counter," = ",items)
# Iterating and printing only values
counter_1 = 0
print("\nIterating and printing only values:")
for items in dict_new:
   counter_1 += 1
   print("Value ",counter_1," = ",dict_new[items])
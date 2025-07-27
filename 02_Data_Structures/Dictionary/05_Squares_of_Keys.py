# Question 5:
# Write a program to prepare a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of the keys.

# Creating a dictionary where keys are numbers from 1 to 15 and values are their squares
dict_new = dict()
for i in range(1, 16):
   # Storing the square of the key as the value
   dict_new[i] = i * i

# Displaying the elements of the dictionary
print("The elements of Dictionary are::\nKey Value Pair format::\n", dict_new, "\n")
elements = 0
for items in dict_new:
   elements += 1
   print("Position = ", elements, " ==> Key = ", items, "\twith Value = ", dict_new[items])
# Question 3:
# Write a program to check if a given key already exists in a dictionary.

# Creating a dictionary with mixed key types
dict_new = {
      "Name": "Arnab",
      "Age": 21,
      3: "Python",
      4: 90,
      5: 40.6
}

# Displaying the elements of the dictionary
print("The elements of Dictionary are::\nKey Value Pair format::\n",dict_new)
print("\nOnly values format::")
elements = 0
for items in dict_new:
   elements += 1
   print("Position = ", elements, " ==> Key = ",items,"\twith Value = ", dict_new[items])
# Iterating and printing both keys and values
key_find = input("\nEnter the key to check if it exists in the dictionary: ")
# Check if the key is an integer or string
if key_find.isdigit():
   key_check = int(key_find)
else:
   key_check = str(key_find)
# Check if the key exists in the dictionary
if key_check in dict_new:
   print("Key ", key_check, "exists in the dictionary with value:", dict_new[key_check])
else:
   print("Key", key_check, "does not exist in the dictionary.")
dict_new = {
      "Name": "Arnab",
      "Age": 21,
      3: "Python",
      4: 90,
      5: 40.6
}

print("The elements of Dictionary are::\nKey Value Pair format::\n",dict_new)
print("\nOnly values format::")
elements = 0
for items in dict_new:
   elements += 1
   print("Position = ", elements, " ==> Key= ",dict.keys[items],"Value = ", dict_new[items])

key_find = input("\nEnter the key to check if it exists in the dictionary: ")
if key_find in dict_new:
   print("Key", key_find, "exists in the dictionary with value:", dict_new[key_find])
else:
   print("Key", key_find, "does not exist in the dictionary.")
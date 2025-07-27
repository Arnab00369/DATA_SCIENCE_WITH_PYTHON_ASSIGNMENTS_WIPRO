dict_new = dict()
for i in range(1, 16):
   # Storing the square of the key as the value
   dict_new[i] = i * i

print("The elements of Dictionary are::\nKey Value Pair format::\n", dict_new, "\n")
elements = 0
for items in dict_new:
   elements += 1
   print("Position = ", elements, " ==> Key = ", items, "\twith Value = ", dict_new[items])
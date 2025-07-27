dic1 = {
   1: 10,
   2: 20
}
print("Dictionary 1: ",dic1)

dic2 = {
   3: 30,
   4: 40
}
print("Dictionary 2: ",dic2)

dic3 = {
   5: 50,
   6: 60
}
print("Dictionary 3: ",dic3)

# Merging or concatenating dictionaries
dic2.update(dic3)
dic1.update(dic2)

print("\nOutput::\nThe key-value pairs after concatenating 3 dictionaries are: ",dic1)
# Question 2:
# Write a program to concatenate the following dictionaries to create a new one.

# Sample Dictionary :
# dic1={1:10, 2:20} dic2={3:30, 4:40} dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# Creating three dictionaries with mixed key types
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
# The above code merges dic2 and dic3 into dic1
print("\nOutput::\nThe key-value pairs after concatenating 3 dictionaries are: ",dic1)
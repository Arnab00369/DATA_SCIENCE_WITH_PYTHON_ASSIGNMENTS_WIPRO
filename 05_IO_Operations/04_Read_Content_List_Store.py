# Program 4: Read each line and store in a list

filename = input("Enter the filename: ")

lines_list = []
with open(filename, 'r') as file:
   for line in file:
      lines_list.append(line.strip())

print("\nLines stored in list:")
print(lines_list)
print("\nEach Line in seperate lines::\n")
for items in lines_list:
   print(items,end="\n")

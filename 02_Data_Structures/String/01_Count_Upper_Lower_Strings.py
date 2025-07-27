String_1 = input("Enter a String to counnt upper and lower case letters: ")

upper_case = ""
lower_case = ""
upper_count = 0
lower_count = 0
for char in String_1:
      if char.isupper():
         upper_case += char + " "
         upper_count += 1
      elif char.islower():
         lower_case += char + " "
         lower_count += 1
print("\nUpper Case Letters: ",upper_case,"\nLower Case Letters: ",lower_case)
print("Number of Upper case characters: ", upper_count)
print("Number of Lower case characters: ", lower_count)
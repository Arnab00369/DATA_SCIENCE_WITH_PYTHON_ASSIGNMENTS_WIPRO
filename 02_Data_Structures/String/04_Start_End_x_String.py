String_1 = input("Enter a String: ")

if String_1.startswith('x'):
   String_1 = String_1[1:]
   if String_1.endswith('x'):
      String_1 = String_1[:-1]
      print("\nOUTPUT::\nResulting String: ",String_1)
   else:
      print("\nString should start and end with 'x' to give an output.")
else:
      print("\nString should start and end with 'x' to give an output.")

String_1 = input("Enter a String: ")

if String_1.startswith('x'):
   String_1 = String_1[1:]
   if String_1.endswith('x'):
      String_1 = String_1[:-1]
      print(String_1)

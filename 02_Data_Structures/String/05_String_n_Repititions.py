String_1 = input("Enter a String: ")

n_Times = int(input("Enter the number of times to repeat the last two characters: "))

if 0 <= n_Times <= len(String_1):
      part = String_1[-n_Times:]
      result = part * n_Times
      print("\nOUTPUT::\nResulting String: ", result)
else:
   print("Invalid value of 'n'. Check your input and try again")
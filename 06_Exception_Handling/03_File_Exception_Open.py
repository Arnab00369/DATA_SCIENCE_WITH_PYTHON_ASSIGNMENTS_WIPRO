# Question 3:


try:
   filename = input("Enter the filename: ")
   
   with open(filename, 'r') as file:
      content = file.read()
      print("\nFile Content in Title Case:\n")
      print(content.title())

except FileNotFoundError:
   print("Error: File not found.")
except Exception as e:
   print("Unexpected error:", str(e))
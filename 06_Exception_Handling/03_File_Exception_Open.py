# Question 3:
# Write a program to accept the file name to be opened from the user, if file exist print the contents of the file in title case or else handle the exception and print an error message.

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
# Question 3:
# Write a program to accept the file name to be opened from the user, if file exist print the contents of the file in title case or else handle the exception and print an error message.

try:
   # Prompt the user to enter the filename (with .txt or full name)
   filename = input("Enter the filename: ")

   # Attempt to open the file in read mode
   with open(filename, 'r') as file:
      # Read the entire content of the file
      content = file.read()

      # Display the content converted to title case
      print("\nFile Content in Title Case:\n")
      print(content.title())

# Handle case when the file is not found
except FileNotFoundError:
   print("Error: File not found.")

# Handle any other unexpected errors
except Exception as e:
   print("Unexpected error:", str(e))

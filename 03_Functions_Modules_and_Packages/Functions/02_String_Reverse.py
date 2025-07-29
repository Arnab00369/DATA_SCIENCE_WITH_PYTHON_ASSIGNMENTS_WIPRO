# Question 2:
# Write a function to return the reverse of a string.
# Sample String : "1234abcd"
# Expected Output : "dcba4321"

# Defining the function to reverse a string
def Str_Reverse(String_new):
   rev_str = ""
   rev_str = String_new[::-1]
   return rev_str


# Taking input from the user
String_new = input("Enter a String: ")
# Calling the function to reverse the string
print("The reverse of the string is: ", Str_Reverse(String_new))
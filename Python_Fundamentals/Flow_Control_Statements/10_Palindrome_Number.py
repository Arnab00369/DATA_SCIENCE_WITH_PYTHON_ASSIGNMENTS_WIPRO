# Question 10:Write a program to find if the given number is palindrome or not

# Example:1
# I/P:110011
# O/P: 110011 is a palindrome.

# Example:2
# I/P:1234
# 0/P: 1234 is not a palindrome.
number = int(input("Enter a number = "))
number_copy = number
reverse_number = 0
while number_copy!=0:
   remainder = number_copy%10
   reverse_number = reverse_number * 10 + remainder
   number_copy = number_copy//10

print("The reverse of the given number = ",reverse_number)
if(reverse_number == number):
   print(number," is a Palindrome Number")
else:
   print(number," is a not a Palindrome Number")
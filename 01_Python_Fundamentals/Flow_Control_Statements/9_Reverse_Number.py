# Question 9: Write a program to reverse a given number and print.

# Example:1
# I/P: 1234
# 0/P:4321

# Example:2
# I/P:1004
# O/P:4001

number = int(input("Enter a number = "))
number_copy = number
reverse_number = 0
while number_copy!=0:
   remainder = number_copy%10
   reverse_number = reverse_number * 10 + remainder
   number_copy = number_copy//10
print("The reverse of ",number," is ",reverse_number)
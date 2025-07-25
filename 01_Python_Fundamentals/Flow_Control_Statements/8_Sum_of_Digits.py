# Question 8: Write a program to print the sum of all the digits of a given number.
# Example:
# I/P:1234
# O/P:10

number = int(input("Enter a given number = "))
number_copy = number
sum_digits = 0
while number_copy!=0:
   remainder = number_copy % 10
   sum_digits += remainder
   #Using // for integer division
   number_copy = number_copy//10
print("The sum of digits of ",number," is = ",sum_digits)
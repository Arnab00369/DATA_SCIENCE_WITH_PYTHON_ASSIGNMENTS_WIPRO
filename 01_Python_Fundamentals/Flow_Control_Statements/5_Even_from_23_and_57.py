# Question 5: Write a program to print even numbers between 23 and 57. Each number should be printed in a separate row.

print("Even Numbers in between 23 and 57 in seperate rows are as follows:")
for number in range(23, 58):
   if number % 2 == 0:
      print(number," \n")
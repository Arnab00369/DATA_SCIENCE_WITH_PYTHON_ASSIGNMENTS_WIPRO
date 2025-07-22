# Question: Write a program to check if a given number is prime or not.

number = int(input("Enter a number = "))
counter = 0

for i in range(1,number+1):
   if(number % i==0):
      counter+=1
print("Output::")
if(counter == 2):
   print(number," is a Prime Number")
else:
   print(number," is Not a Prime Number")
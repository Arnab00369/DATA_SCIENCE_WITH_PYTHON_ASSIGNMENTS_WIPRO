def factorial(number):
   fact = 1
   for i in range(1,number+1):
      fact *= i
   return fact
   
number = int(input("Enter a non-negative integer: "))

if number < 0:
   print("The number is negative!!Check your input again and try again.")
else:
   print("The factorial of ",number," = ",factorial(number))
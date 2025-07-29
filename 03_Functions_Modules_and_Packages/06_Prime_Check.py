# Question 6:
# Write a function that takes a number as a parameter and checks whether the number is prime or not.

# Defining the function to check if a number is prime
def Prime_Check(number):
   counter = 0
   # for loop 
   for i in range(1,number+1):
      if(number % i==0):
         counter+=1
   print("\nOUTPUT::")
   # If the counter is 2, then the number is prime
   if(counter == 2):
      print(number," is a Prime Number")
   else:
      print(number," is Not a Prime Number")

# Enter a number from the user
number = int(input("Enter a number = "))
if number < 0:
   print("The number is negative!! Check your input again and try again.") 
else:
   Prime_Check(number)
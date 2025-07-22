# Question 1: Write a program to check if a given number is Positive, Negative, or Zero.

number = int(input("Enter a number: "))
print("\nOutput is:")
if(number>0):
   print(number," is a positive number")
elif(number<0):
   print(number," is a negative number")
else:
   print(number," is zero")

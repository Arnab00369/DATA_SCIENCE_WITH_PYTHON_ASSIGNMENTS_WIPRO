# Question 3: Given two non-negative values, print true if they have the same last digit, such as with 27 and 57.
# lastDigit(7, 17) + true
# lastDigit(6, 17) + false
# lastDigit(3, 113) > true

number_1 = int(input("Enter a non-negative number: "))
number_2 = int(input("Enter another non-negative number: "))
print("\nOutput:")
if(number_1 > 0 & number_2 > 0):
   if(number_1 % 10 == number_2 % 10):
      print(number_1," and ",number_2," have Same Digits")
   else:
      print(number_1," and ",number_2," have Different Digits")
elif(number_1 > 0 & number_2 < 0):
   print(number_2," is a negative number so cannot check any further. Please check if both the numbers are non-negative")
elif((number_2 > 0) & (number_1 < 0)):
   print(number_1," is a negative number so cannot check any further. Please check if both the numbers are non-negative")

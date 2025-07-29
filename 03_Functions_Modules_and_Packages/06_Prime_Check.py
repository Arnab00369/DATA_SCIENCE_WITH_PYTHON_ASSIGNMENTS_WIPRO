
def Prime_Check(number):
   counter = 0

   for i in range(1,number+1):
      if(number % i==0):
         counter+=1
   print("\nOUTPUT::")
   if(counter == 2):
      print(number," is a Prime Number")
   else:
      print(number," is Not a Prime Number")


number = int(input("Enter a number = "))
if number < 0:
   print("The number is negative!! Check your input again and try again.") 
else:
   Prime_Check(number)
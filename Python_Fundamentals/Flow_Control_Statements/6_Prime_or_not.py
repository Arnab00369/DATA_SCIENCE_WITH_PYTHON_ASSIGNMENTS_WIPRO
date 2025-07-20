number = int(input("Enter a number = "))

for i in number:
   if(number % i==0):
      counter+=counter
if(counter == 2):
   print("Prime")
else:
   print("Not Prime")
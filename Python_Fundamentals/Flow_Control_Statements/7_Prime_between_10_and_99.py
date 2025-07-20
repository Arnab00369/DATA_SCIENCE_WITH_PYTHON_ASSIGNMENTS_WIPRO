print("Prime numbers between 10 and 99 are:")
number_counter = 0
for i in range(1, 100):
   counter = 0
   for j in range(1, i+1):
      if i%j==0:
         counter+=1
         
   if counter == 2:
      number_counter+=1
      print(i,end=" ")
print("\nTotal number of prime numbers between 10 and 99 is:", number_counter)
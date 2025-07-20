number = int(input("Enter a number = "))
number_copy = number
reverse_number = 0
while number_copy!=0:
   remainder = number_copy%10
   reverse_number = reverse_number * 10 + remainder
   number_copy = number_copy//10
print("The reverse of ",number," is ",reverse_number)
# Question 4:
# Declare a list with 10 integers and ask the user to enter an index. Check whether the number in that index is positive or negative number. If any invalid index is entered, handle the exception and print an error message.

numbers = [10, -5, 7, -12, 0, 23, -34, 8, -1, 3]

try:
   index = int(input("Enter an index (0 to 9): "))
   value = numbers[index]
   if value > 0:
      print("The number at index",index," is Positive: ",value)
   elif value < 0:
      print("The number at index: ",index," is Negative: ",value)
   else:
      print("The number at index",index," is Zero.")

except IndexError:
   print("Error: Index out of range. Enter a value between 0 and 9.")
except ValueError:
   print("Error: Please enter a valid integer index.")
except Exception as e:
   print("Unexpected error:", str(e))
# Question 1:

try:
   num1 = float(input("Enter first number: "))
   num2 = float(input("Enter second number: "))
   
   result = num1 / num2
   print("Result of division:", result)

except ZeroDivisionError:
   print("Error: Cannot divide by zero.")
except ValueError:
   print("Error: Please enter valid numeric values.")
except Exception as e:
   print("Unexpected error:", str(e))
else:
   print("Division performed successfully.")

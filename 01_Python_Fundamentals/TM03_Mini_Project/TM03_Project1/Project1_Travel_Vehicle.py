# Project 1: Create a python program that asks the user how far they want to travel. If they want to travel less than three miles tell them to ride Bicycle. If they want to travel more than three miles, but less than three hundred miles, tell them to ride Motor-Cycle. If they want to travel three hundred miles or more tell them to driver Super-Car.

# Sample Output:
# How far would you like to travel in miles? 2500
# I suggest Super-Car to your destination

# Code:

#Taking input from user for distance to be travelled
distance = float(input("How far would you like to travel in miles? "))

#Checking the distance and suggesting the mode of travel
if distance > 0:
   if distance < 3:
      print("Your destination is close-by, that is ",distance,"miles away.");
      print("I suggest Bicycle to your destination");
   elif 3<= distance < 300:
      print("Your destination is far away, which is ",distance,"miles.");
      print("I suggest Motor-Cycle to your destination");
   elif distance >= 300:
      print("Your destination is very far, that is ",distance,"miles away.");
      print("I suggest Super-Car to your destination");
   else:
      print("Invalid Input!! Please check yourr input and try again.")
else:
   
   print("Distance cannot be negative. Please enter a valid distance.")


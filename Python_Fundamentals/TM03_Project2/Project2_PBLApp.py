# Project 2: Let's assume you are planning to use your Python skills to build a PBLApp for Mobile. You decide to host your application on servers running in the cloud. You pick a hosting provider that charges $0.51 per hour. You will launch your service using one server and want to know how much it will cost to operate per day,per week,per month. 

# Write a Python program that displays the answers to the following questions:

# How much does it cost to operate one server per day?
# How much does it cost to operate one server per week?
# How much does it cost to operate one server per month?
# How many days can I operate one server with $918?

# Code:

charges_per_hour = 0.51

hours_per_day = 24
hours_per_week = 7 * hours_per_day
hours_per_month = 30 * hours_per_day

cost_per_day = charges_per_hour * hours_per_day
cost_per_week = charges_per_hour * hours_per_week
cost_per_month = charges_per_hour * hours_per_month

days_with_budget = 918 / cost_per_day

print("Cost to operate one server per day: $", round(cost_per_day, 2))
print("Cost to operate one server per week: $", round(cost_per_week, 2))
print("Cost to operate one server per month: $", round(cost_per_month, 2))
print("Days of operation with $918 = ", int(round(days_with_budget, 2))," days")   


#! /usr/bin/env python3

meal = int(input("Enter the price of your meal."))
percent = int(input("Enter the percent of tip that you want to leave."))
tip = ((meal * percent) / 100)
bill = (meal + tip)
print("Your tip amount is", tip, "and the total bill is", bill)

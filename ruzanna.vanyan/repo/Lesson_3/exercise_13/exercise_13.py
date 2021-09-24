#! /usr/bin/env python3

cost = int(input("Enter the cost of your meal: "))
tax = cost * 10 / 100
tip = cost * 18 / 100
total = cost + tax + tip
print("Your bill's tax amount is", round(tax, 2), "\n",  "The tip amount is", round(tip, 2),"\n", "The total price of the meal is", round(total, 2))
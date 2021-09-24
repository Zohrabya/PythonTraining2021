#! /usr/bin/env python3

num1 = float(input("Enter tha number of containers which are holding one liter or less: "))
num2 = float(input("Enter the number of containers which are holding more than one liter: "))
dep1 = 0.10
dep2 = 0.25
print("Your refund is", round(num1 * dep1, 2) + round(num2 * dep2, 2), "$")
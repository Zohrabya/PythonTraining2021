#!/usr/bin/env python3

cont_1 = float(input("Enter tha number of containers which are holding one liter or less: "))
cont_2 = float(input("Enter the number of containers which are holding more than one liter: "))
print("Your refund is", round(cont_1 * 0.10, 2) + round(cont_2 * 0.25, 2), "$")
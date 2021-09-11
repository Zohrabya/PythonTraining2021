#!/usr/bin/env python3

length = float(input("Enter the length of the field in feet: "))
width = float(input("Enter the width of the field in feet: "))
acre = (length * width) / 43560
print("The area of the field in acre is: ", round(acre, 2))
#! /usr/bin/env python3

length = float(input("Enter the length of the field in feet:"))
width = float(input("Enter the width of the field in feet:"))
feet = (length * width) 
acre = 43560 #square feet
print("The area of the field in acre is:", round(feet / acre, 2))
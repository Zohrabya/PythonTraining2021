#!/usr/bin/env python3
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
num4 = int(input("Enter the fourth number: "))
num5 = int(input("Enter the fifth number: "))
min = num1
max = num1
#smallest
if num2 < num1:
    min = num2
if num3 < num1:
    min = num3
if num4 < num1:
    min = num4
if num5 < num1:
    min = num5
print("Tha smallest number is {}:".format(min))

#largest
if num2 > num1:
    max = num2
if num3 > num1:
    max = num3
if num4 > num1:
    max = num4
if num5 > num1:
    max = num5
print("The largest number is {}:".format(max) )
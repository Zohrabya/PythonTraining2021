#!/usr/bin/env python3

num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))
if num_1 > num_2:
    print(num_1, "Is larger.")
elif num_2 > num_1:
    print(num_2, "Is larger.")
else:
    print("These numbers are equal.")
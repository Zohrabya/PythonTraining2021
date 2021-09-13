#!/usr/bin/env python3

num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))
if num_1 % num_2 == 0:
 print(f"The {num_1} is a multiple of {num_2}")
else:
    print(f"The {num_1} is not multiple of {num_2}")
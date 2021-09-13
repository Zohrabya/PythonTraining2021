#!/usr/bin/env python3

radius = int(input("Enter the radius of circle: "))
Pi =  3.14159
print("The circle's diameter is: ", round(radius * 2, 2))
print("The circle's circumference is: ", round(radius * 2 * Pi, 2))
print("The circle's area is: ", round(Pi * radius ** 2, 2))
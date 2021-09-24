#! /usr/bin/env python3

radius = int(input("Enter the radius of circle: "))
PI =  3.14159
print("The circle's diameter is: ", round(radius * 2, 2))
print("The circle's circumference is: ", round(radius * 2 * PI, 2))
print("The circle's area is: ", round(PI * radius ** 2, 2))
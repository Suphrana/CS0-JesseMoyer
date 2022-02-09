'''
Name: Jesse Moyer
Date: 2/9/2022

Finding the circumference / area of a circle with user inputs

'''
from cmath import pi

circLen=input("What is the radius of the circle? ->")
circLen=float(circLen)
area=(pi*circLen**2)
print("The area of the circle is:", area)
circumference=(2*pi*circLen)
print("The circumference of the circle is:", circumference)
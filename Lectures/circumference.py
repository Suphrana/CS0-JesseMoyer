'''
Name: Jesse Moyer
Date: 2/9/2022

Finding the circumference / area of a circle with user inputs

'''
#Imported pi value from cmath
from cmath import pi

#Prompted input and converted into float
circLen=input("What is the radius of the circle? ->")
circLen=float(circLen)

#Calculate and print area
area=(pi*circLen**2)
print("The area of the circle is:", area)

#Calculate and print circumference
circumference=(2*pi*circLen)
print("The circumference of the circle is:", circumference)
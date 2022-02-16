'''
Name: Jesse Moyer
Date: 2/9/2022

Finding the area of a triangle using 3 sides

'''

from math import sqrt


a=float(input("Side a ->"))
b=float(input('Side b ->'))
c=float(input("Side c ->"))
s=(((a+b+c)/2))

Perimeter=(a+b+c)
Area=sqrt(s*(s-a)*(s-b)*(s-c))
print("Area:", Area)
print("Perimeter:", Perimeter)
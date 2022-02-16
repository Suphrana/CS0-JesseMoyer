'''
Name: Jesse Moyer
Date: 2/9/2022

Finding the area and perimeter of a triangle using 3 sides

'''
#Importing a math function
from math import sqrt 

#Assigning variables to user inputs
a=float(input("Side a ->"))
b=float(input('Side b ->'))
c=float(input("Side c ->"))

#Determines whether the sides form a triangle or not
if (a+b < c) or (a+c < b) or (b+c < a):
    print("These sides do not form a triangle.")
else:
    print("These sides form a triangle.")

#Semiperimeter formula
s=(((a+b+c)/2))

#Assigning equations to a variable
Perimeter=float(a+b+c)
Area= float(sqrt(s*(s-a)*(s-b)*(s-c)))

#Printing answers to show user
print("Area:", Area)
print("Perimeter:", Perimeter)


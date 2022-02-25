'''
Name: Jesse Moyer
Date: 2/9/2022

Finding the area and perimeter of a triangle using 3 sides

''' 

#Assigning variables to user inputs
a=float(input("Side a ->"))
b=float(input('Side b ->'))
c=float(input("Side c ->"))

#Created a function with all of the formulas in order to compress
def demensions():
    perimeter = (a+b+c)
    s = perimeter/2
    area = (s*(s-a)*(s-b)*(s-c))**1/2
    print(f"These sides form a triangle with Area: {area}, Perimeter: {perimeter}")

#Determines whether the sides form a triangle or not
if (a+b < c) or (a+c < b) or (b+c < a):
    print("These sides do not form a triangle.")
else:
    demensions()

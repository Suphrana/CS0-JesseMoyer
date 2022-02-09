'''
Name: Jesse Moyer
Date: 2/7/2022

Finding area and perimeter of a rectangle with user inputs.

'''
#Prompt user inputs
rectLength=input('What is the length of the rectangle? ->')
rectWidth=input('What is the width of the rectangle? ->' )

#Convert values into floats
rectLength = float(rectLength)
rectWidth=float(rectWidth)

#Calculate and print area
area=(rectLength*rectWidth)
print('The area of the rectangle is:', area)

#Calculate and print perimeter
perimeter=(2*(rectWidth+rectLength))
print('The perimeter of the rectangle is:', perimeter)
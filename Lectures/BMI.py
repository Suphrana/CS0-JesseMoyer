'''
Name: Jesse Moyer
Date: 2/9/2022

Finding BMI with height and weight

Step 1: Prompt user for weight and height
Step 2: Convert inputs into floats
Step 3: Convert Height and Weight into metric measurements
Step 4: Calculate BMI using kg/m**2
Step 5: Print BMI calculation
'''
#Step 1
Weight = input("Weight (in pounds):")
Height = input("Height (in inches):")

#Step 2
Height = float(Height)
Weight = float(Weight)

#Step 3/4
BMI = ((0.453592*Weight)/((0.0254*Height)**2))

#Step 5
print("Your BMI is:", BMI)
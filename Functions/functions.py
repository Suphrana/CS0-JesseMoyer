'''
Name: Jesse Moyer
Date: 02/25/22

Write a Python program that performs some arithmetic operations
on two given numbers (entered by user) along with the following requirements.

'''
#Import sqrt function
from math import sqrt 

#Main function:
#User inputs for 2 numbers
def main():
    print("Please enter two positive integers:")
    num1, num2 = float(input()), float(input())
    test()
    print("Sum",addition(num1, num2))
    print("Product",multiplicaiton(num1, num2))
    print("Quotient",division(num1, num2))
    print("Difference",subtraction(num1, num2))
    print("Remainder",modulus(num1, num2))
    print("Power",power(num1, num2))
    print("Square root of the first number",root(num1))
    print(bigger_number(num1, num2))
    return num1, num2

#Defining functions for arithmetic equations
def addition(num1, num2):
    return num1+num2

def multiplicaiton(num1, num2):
    return num1*num2

def division(num1, num2):
    return num1/num2 

def subtraction(num1, num2):
    return num1-num2

def modulus(num1, num2):
    return num1%num2

def power(num1, num2):
    return num1**num2

def root(num1):
    return sqrt(num1)

#Extra Credit
def bigger_number(num1, num2):
    if (num1>num2):
        print(f"{num1} is greater than {num2}.")
    elif (num1==num2):
        print(f"{num1} is equal to {num2}.")
    else:
        print(f"{num2} is greater than {num1}.")

#Test function
def test():
    assert addition(5,5) == 10
    assert addition(6,9) == 15

    assert multiplicaiton(2,3) == 6
    assert multiplicaiton(8,8) == 64

    assert division(4,2) == 2
    assert division(8,2) == 4

    assert subtraction(20,10) == 10
    assert subtraction(35,5) == 30

    assert modulus(5,5) == 0
    assert modulus(4,3) == 1

    assert power(4,2) == 16
    assert power(5,2) == 25

    assert root(4) == 2
    assert root(16) == 4
    print("All test cases passed")
    

#Function placed to output everything within
main()


'''
Name: Jesse Moyer
Date: 02/25/22

Write a Python program that performs some arithmetic operations
on two given numbers (entered by user) along with the following requirements.

'''
#Main function:
#User inputs for 2 numbers
def main():
    print("Please enter two positive integers:")
    num1, num2 = float(input()), float(input())
    print("Sum",addition(num1, num2))
    print("Product",multiplicaiton(num1, num2))
    print("Quotient",division(num1, num2))
    print("Difference",subtraction(num1, num2))
    print("Remainder",modulus(num1, num2))
    print("Power",power(num1, num2))
    print("Square root",root(num1, num2))
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

def root(num1, num2):
    return num1**(1/num2)

#Extra Credit
def bigger_number(num1, num2):
    if (num1>num2):
        print(f"{num1} is greater than {num2}.")
    elif (num1==num2):
        print(f"{num1} is equal to {num2}.")
    else:
        print(f"{num2} is greater than {num1}.")

#Test function
def test(num1, num2):
    assert addition(5,5) == 10
    assert

    assert
    assert

    assert
    assert

    assert
    assert

    assert
    assert

    assert
    assert

    assert
    assert
    

#Function placed to output everything within
main()


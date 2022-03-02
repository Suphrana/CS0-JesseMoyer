'''
Name: Jesse Moyer
Date: 03/02/22

Write a Python program that computes certain values such as sum, product, max, min
and average of 5 given numbers.
'''

def main():
    print("Please enter 5 numbers:")
    a,b,c,d,e = (float(input(">")), float(input(">")), float(input(">")), float(input(">")), float(input(">")))
    test()
    print("Sum:", sum(a,b,c,d,e))
    print("Product:", product(a,b,c,d,e))
    print("Average:", average(a,b,c,d,e))
    print("Maximum:", maximum(a,b,c,d,e))
    print("Minimum:", minimum(a,b,c,d,e))
    return a,b,c,d,e 

def sum(a,b,c,d,e):
    return a+b+c+d+e
    
def product(a,b,c,d,e):
    return a*b*c*d*e

def average(a,b,c,d,e):
    return (sum(a,b,c,d,e)/5)

def maximum(a,b,c,d,e):
    pass

def minimum(a,b,c,d,e):
    pass

def test():
    assert sum(1,2,3,4,5) == 15
    assert sum(2,4,6,8,10) == 30
    assert
    assert
    assert
    assert
    assert
    assert

main()
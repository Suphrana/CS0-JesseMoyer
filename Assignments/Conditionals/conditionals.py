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
    if a > (b and c and d and e):
        return a
    elif b > (a and c and d and e):
        return b
    elif c > (a and b and d and e):
        return c
    elif d > (a and b and c and e):
        return d
    elif e > (a and b and c and d):
        return e
    

def minimum(a,b,c,d,e):
    if a < (b and c and d and e):
        return a
    elif b < (a and c and d and e):
        return b
    elif c < (a and b and d and e):
        return c
    elif d < (a and b and c and e):
        return d
    elif e < (a and b and c and d):
        return e

def test():
    assert sum(1,2,3,4,5) == 15
    assert sum(2,4,6,8,10) == 30
    assert product(2,2,2,2,2) == 32
    assert product(1,1,1,1,1) == 1
    assert average(1,2,3,4,5) == 3
    assert average(2,4,6,8,10) == 6
    assert maximum(4,5,7,1,9) == 9
    assert maximum(2,9,5,6,7) == 9
    assert minimum(1,2,3,4,5) == 1
    assert minimum(1,2,4,6,8) == 1

main()


'''
Name: Jesse Moyer
Date: 03/14/2022

Solve the avian kattis problem using python 3
'''
def main():
    #Storage for blimp reg numbers
    CIA = []


    #FBI blimp counter
    for i in range(5):
        blimp = input("Gay")
        if "FBI" in blimp:
            CIA.append(str(i+1))
            
    if CIA:
        print(" ".join(CIA))
    else:
        print("HE GOT AWAY!")

main()
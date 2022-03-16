'''
Name: Jesse Moyer
Date: 03/14/2022

Solve the avian kattis problem using python 3
'''

#Main function
def main():
    #Storage for blimp reg numbers
    CIA = []

    #FBI blimp counter
    for i in range(5):
        blimp = input()
        if "FBI" in blimp:
            CIA.append(str(i+1))
    #Add a space between the numbers if CIA has contents        
    if CIA:
        print(" ".join(CIA))
    #No contents = he escaped   
    else:
        print("HE GOT AWAY!")
    print(" ".join(CIA))
    return CIA

main()




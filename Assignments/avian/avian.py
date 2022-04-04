'''
Name: Jesse Moyer
Date: 03/14/2022

Solve the avian kattis problem using python 3
'''
def input_blimp():
        blimp = input()
        return blimp

def blimpfinder(blimps, i):
        CIA = []
        if "FBI" in blimps:
                        CIA.append(str(i+1))
        if CIA:
                " ".join(CIA)
      
        else:
                "HE GOT AWAY!"

        return CIA

def main():
        for i in range (5):
                blimps = input_blimp()
                blimpfinder(blimps, i)
        
main()


'''
Name: Jesse Moyer
Date: 03/14/2022

Solve the avian kattis problem using python 3
'''
#give blimp values
def input_blimp():
        blimp = input()
        return blimp

#function to find and mark any blimps
def blimpfinder(blimps, i, CIA):
        #find fbi in the blimps
        if "FBI" in blimps:
                        CIA.append(str(i+1))

#main function to process all functions in their order
def main():
        CIA = []
        for i in range (5):
                blimps = input_blimp()
                blimpfinder(blimps, i, CIA)
        
        if CIA:
                print (*CIA, sep=" ")
        
        else: print("HE GOT AWAY!")
        
main()


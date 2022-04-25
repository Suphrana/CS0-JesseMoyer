'''
Name: Jesse Moyer
Date: 03/14/2022

Solve the avian kattis problem using python 3
'''
#function to find and mark any blimps
def blimpfinder(blimp,blimp2,blimp3,blimp4,blimp5):
        #Create list placeholder
        Cia = []
        #find fbi in the blimps
        if "FBI" in blimp:
                       Cia.append(str(+1))
        if "FBI" in blimp2:
                       Cia.append(str(+2))
        if "FBI" in blimp3:
                       Cia.append(str(+3))
        if "FBI" in blimp4:
                       Cia.append(str(+4))
        if "FBI" in blimp5:
                       Cia.append(str(+5))
     
        return Cia
#main function to process all functions in their order
def main():
        #Blimp inputs from user
        blimp = input()
        blimp2 = input()
        blimp3 = input()
        blimp4 = input()
        blimp5 = input()
        
        #prints function to allow tests to work in kattis as well as print result
        jj = print(*blimpfinder(blimp,blimp2,blimp3,blimp4,blimp5), sep=" ")
        print(jj)
        if jj == None:
                print("HE GOT AWAY!")
 
        
        #assert tests
        assert blimpfinder("FBI","FBI","l","l","l") == ['1', '2']
        assert blimpfinder("FBI","FBI","FBI","l","l") == ['1', '2', '3']
        assert blimpfinder("FBI","FB","l","l","l") == ['1']
main()


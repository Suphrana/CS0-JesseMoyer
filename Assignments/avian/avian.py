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
    

    def test():
    #Storage for blimp reg numbers
        CIA = []
    #FBI blimp counter
        blimp = ["FBI","HUG","FBI","BRUH","AHAH"]
        if "FBI" in blimp[0]:
                CIA.append(str(+1))
        if "FBI" in blimp[1]:
                CIA.append(str(+2))
        if "FBI" in blimp[2]:
                CIA.append(str(+3))
        if "FBI" in blimp[3]:
                CIA.append(str(+4))
        if "FBI" in blimp[4]:
                CIA.append(str(+5))
        #Add a space between the numbers if CIA has contents        
        if CIA:
            " ".join(CIA)
        #No contents = he escaped   
        else:
            print("HE GOT AWAY!")
        
        assert CIA == ['1','3']
        
    test()
    def test2():
        CIA = []

        blimp = ["FBI","FBI","FBI","BRUH","AHAH"]
        if "FBI" in blimp[0]:
                CIA.append(str(+1))
        if "FBI" in blimp[1]:
                CIA.append(str(+2))
        if "FBI" in blimp[2]:
                CIA.append(str(+3))
        if "FBI" in blimp[3]:
                CIA.append(str(+4))
        if "FBI" in blimp[4]:
                CIA.append(str(+5))
        #Add a space between the numbers if CIA has contents        
        if CIA:
            " ".join(CIA)
        #No contents = he escaped   
        else:
            print("HE GOT AWAY!")
        
        assert CIA == ['1','2','3']
    test2()
    def test3():
        CIA = []

        blimp = ["FBI","FBI","FBI","FBI","AHAH"]
        if "FBI" in blimp[0]:
                CIA.append(str(+1))
        if "FBI" in blimp[1]:
                CIA.append(str(+2))
        if "FBI" in blimp[2]:
                CIA.append(str(+3))
        if "FBI" in blimp[3]:
                CIA.append(str(+4))
        if "FBI" in blimp[4]:
                CIA.append(str(+5))
        #Add a space between the numbers if CIA has contents        
        if CIA:
            " ".join(CIA)
        #No contents = he escaped   
        else:
            print("HE GOT AWAY!")
        
        assert CIA == ['1','2','3','4']
    test3()

main()
#The tests are jank, but they do the job.
#Aside from the asserts I liked the compact code i created for the original program and was unable to use asserts or find a way to use them in conjunction with it.




'''
Name: Jesse Moyer
Date: 03/30/2022

Create a computer program that can play simon says perfectly
'''
#Create Function
def simonsays():

#Lines of dialogue for game
    turns = int(input())

#Repeat until all lines are inputted
    for i in range(turns):
        simonsays = input()

#Print desired task if simon says to do so AKA print all characters after 10 spaces
        if "Simon says " in simonsays:
            print(simonsays[10:])
    return simonsays


def test():
    assert simonsays == ""
    print("All test cases passed!")

def main():
    simonsays()
    test()
    
main()


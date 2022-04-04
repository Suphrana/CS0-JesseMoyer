'''
Name: Jesse Moyer
Date: 03/30/2022

Create a computer program that can play simon says perfectly
'''
#User inputs amount of lines for game
def input_turns():
    turn = int(input())
    return turn

#Grabs words after simon says if string has simon says
def simonsays(strings):
    if "Simon says " in strings:
        print(strings[10:])
    return strings

#User inputs the lines for game
def input_string():
    inputted_string = input()
    return inputted_string

#Test function, removed print to work for test
def simonsaystest(strings):
    if "Simon says " in strings:
        return strings[10:]

#Main function assigns variables and combines to create game
def main():
    turns = input_turns()
    for i in range (turns):
        strings = input_string()
        simonsays(strings)

    #test functions   
    assert (simonsaystest("Simon says bruh") == " bruh")
    assert (simonsaystest("Simon says jump") == " jump")
    assert (simonsaystest("Simon says lol") == " lol")
main()


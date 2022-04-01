'''
Name: Jesse Moyer
Date: 03/30/2022

Create a computer program that can play simon says perfectly
'''

def input_turns():
    turn = int(input("Number of simon says commands ->"))
    return turn

def simonsays(strings):
        if "Simon says " in strings:
            print(strings[10:])
        return strings

def input_string():
    inputted_string = input("Simon says commands ->")
    return inputted_string

# def test():
#     assert (simonsays("Simon says die") == " die")

def main():
    turns = input_turns()
    for i in range (turns):
        strings = input_string()
    simonsays(strings)
main()
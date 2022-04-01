'''
Name: Jesse Moyer
Date: 03/30/2022

Create a computer program that can play simon says perfectly
'''
#Create Function
def input_turns():
    turn = input("Number of simon says commands ->")
    return turn

def simonsays(turns, simonsays):

#Repeat until all lines are inputted
    for i in range(turns):
        strings = []

#Print desired task if simon says to do so AKA print all characters after 10 spaces
        if "Simon says " in simonsays:
            print(simonsays[10:])
    return simonsays

def input_string():
    inputted_string = input("Simon says commands ->")
    return inputted_string

def main():
    turns = input_turns()
    strings = input_string()


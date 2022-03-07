'''
Name: Jesse Moyer
Date: 03/07/22

Designing and implimenting the "Guess the number game" 

'''
from random import randint

def main():
    name = (input("Welcome to Guess the Number! \nWhat is your name? ->"))
    print(f"Hello, {name}. I am thinking of a number between 1 and 20. \nYou get 6 tries to guess the number. Take a guess!:")

    rng = randint(1,20)

    for i in range (1,7):
        guess = int(input(f"You have {7-i} guesses remaining->"))
        if (guess > rng):
            print("Your guess was too high")
        elif (guess < rng):
            print("Your guess was too low")
        elif (guess == rng):
            print("By some miracle... You won.")
        else:
            continue
        
        if i == 6:
            print("L")

main()
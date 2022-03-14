'''
Name: Jesse Moyer
Date: 03/07/22

Designing and implimenting the "Guess the number game" 

'''
def wrapmain():
#import random integer function
    from random import randint

#Username and information
    name = (input("Welcome to Guess the Number! \nWhat is your name? ->"))
    print("To quit the game type '0'")

    wins = 0
    losses = 0
    #Create main function
    def main(wins, losses):
        print(f"Hello, {name}. I am thinking of a number between 1 and 20. \nYou get 6 tries to guess the number. Take a guess!:")
        #Create random integer
        rng = randint(1,20)
        
        #Create guess functions and let player know if the number is too high or too low
        for i in range (1,7):
            guess = int(input(f"You have {7-i} guesses remaining->"))
            
            if (guess > rng):
                print("Your guess was too high")
            elif (guess < rng) and (guess != 0):
                print("Your guess was too low")
            elif (guess == rng):
                print("By some miracle... You won.")
                print(f"You guessed my number in {i} tries!")
                wins += 1
                main(wins, losses)
            
            #Fail player when tries run out
            if i == 6:
                print("Here's this... L")
                print(f"The number I was thinking of was {rng}")
                losses += 1
                main(wins, losses)
            
            #Exit game and recieve stats
            if (guess == 0):
                print(f"You have quit the game with {wins} wins and {losses} losses.")
                break
    main(wins, losses)            
wrapmain() 


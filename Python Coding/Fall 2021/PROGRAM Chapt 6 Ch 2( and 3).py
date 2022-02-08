# Guess my number
#
# the user will pick between a range of two numbers
# the computer will pick a number from random between the range
# the player then tries to guess it and the computer will let
# the player know if the guess is too high or too low
#
# i tried doing some exception handling and ran into another wall
# im just happy i got this working with the user input as of now!
# please let me know if i utilized the def ask_number(): correctly  
####################################

import random

def intro():
    #displays the intro to the program
    print("\tWelcome to \"Guess My Number\"!")
    print("\tI will allow you to choose a range of numbers.")
    print("\tThen, I will pick a random number between your low and high") 
    print("\tTry to guess it in as few attemps as possible.\n")

def ask_number (low, high, guess):
    #takes a range of numbers and your guess
    low = ""
    high = ""
    guess = int(input("Take a guess: "))
    return guess

def main():
    # main part of program
    intro()
    low = int(input("First, Pick your low range: "))
    high = int(input("Second, Pick your high range: "))
    while high < low:
        high = int(input("What are you doing? pick again: "))
    # This is where the computer picks a random number    
    the_number = random.randint(low, high)
    guess = ask_number(low, high,"")
    tries = 1
    # this loop will continue until you win 
    while guess != the_number:
        if guess < low:
            print("Not gonna break me, try again, by the way this attempt still cost a try lol")
        elif guess > high:
            print("You thought you had me lmao, AND im taking a try!")
        elif guess > the_number:
            print("Lower...")
        else:
            print("Higher...")
        guess = int(input("Try another: "))
        tries += 1

    print("you guessed it! the number was", the_number)
    print("And it only took you ", tries, "tries!\n")
    input("Thanks for playing! press enter to quit")




main()

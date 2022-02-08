# Kathy
# This program generates a random number between lower and upper input by the user
# The user is then prompted to guess the number.
# The response is based on how far the user is away from the guess

import random
print ("""

    Welcome to the Guessing Game!

    You will enter a range of numbers to use.

    You will then be asked to guess a random number between the two.

""")
    
lower = int(input("Enter the lower number ==> "))
upper = int(input("Enter the upper number ==> "))

if lower >= upper :
    print ("OOPS!  the lower number is greater than or equal to the upper numer.")
else :
    myNumber = random.randint(lower, upper)

    print (lower, upper, myNumber)

    userGuess = int(input("\nEnter your guess ==> "))

    if userGuess == myNumber :
        print ("YOU ARE CORRECT!")
    elif userGuess > upper :
        print ("Your guess is greater than the upper range (",upper,")")
    elif userGuess < lower :
        print ("Your guess is less than the lower range (",lower,")")
    else :
        print ("So sad...not even close.")
        
    

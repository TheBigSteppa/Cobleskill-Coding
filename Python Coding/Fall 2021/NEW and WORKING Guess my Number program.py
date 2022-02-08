# Mark Fraser
# Guess the number V2
# how t read files (192)
# while loop needed to make the game run until user closes (77)
# compound while loop (78-79)
# make the read file an integer
#=====================
import random
import sys

#========================================

def intro ():
# Intro to program
    print("""


\t\t\tWelcome to:
\t\t\t\t Guess The Numberrrr  V2 !!!!\n
This is a game where the computer will pick a number \nfrom random while the user guesses it.

""")

    input("Press Enter to get started. \n")

def openFile(fileName, mode):
# open the file with the mode given
    try:
        theFile = open(fileName, mode)
    except IOError as e:
        print ("unable to open file ", fileName, "\nending program.\n", e)
        input ("\n\nPress enter to exit")
        sys.exit()
    else:
        return theFile

def ask_user(Question):
    VALID = 1
    while VALID == 1:
        try:
            response = int(input(Question))
        except ValueError as e:
            print("\nNOT A VALID ENTRY, TRY AGAIN\n")
            VALID = 1
        else:
            break
    return response

def GuessLoop ():
    #replay = ""
    #tries = 1
    play = True
    while play == True:
        rando = random.randint(low, high)
        #print("DEBUG::",rando)
        guess = ask_user("Take your first guess: ")
        tries = 1
        while guess != rando and tries != atm:
            if guess > rando:       #
                print("too high")   # i think the issue is within this block but i have no idea
            elif guess < rando:     #
                print("too low")    #
            guess = ask_user("\nGuess again: ")
            tries +=1
            #print("DEBUG::",tries)
            #print("DEBUG::",rando)
        if guess == rando:
            print("\nAyeee big winner, it only took you",tries,"tries")
        if tries == atm:
            print("\nMax amount of tries, the number was",rando)
        replay = input("\nwould you like to play again? y/n: ")
        #print(replay)
        if replay == "y":
            print(replay)
            play = True
        else:
            play = False
    
    #if replay == ("n"):
     #   print(replay)
      #  play = False
    #else:
     #   print(replay)
      #  play = True
            
    
def main():
    intro()
    GuessLoop()
    


#==================== Varibles ==============
theFile = open("fileToRead.txt","r")
high = int(theFile.readline())
low = int(theFile.readline())
atm = int(theFile.readline())
tries = 1
#test = low + high

#print(low)
#print(high)
#print(atm)
#print(test)
#===================== Main =================

main()





# By Mark Fraser
# coin flip out of 100 program

import random


print("""

\t\t\tHello!
\t\twelcome to the coinflip program.
\t\t we will be able to flip a coin
\t\t  as mant times as you'd like!""")

#input(print("Press enter to get started"))

totalFlips = int(input("\nEnter how many times you would the coin flipped ==> "))   # allows user to input how many coin flips are there
      


numHeads = 0
numTails = 0
#totalFlips = 100 \\ Old way that allowed 100 coin flips, now the program allows the user to choose how many coin flips are done

while totalFlips > 0:
    coinFlip = random.randint(0,1)
    #print (coinFlip) Debug
    if coinFlip == 0:
        numHeads += 1
        #print (numHeads) Debug
    else:
        numTails += 1    
        #print (numTails) Debug
    totalFlips = totalFlips - 1

print ('you flipped "Heads" a total of', numHeads, 'times!')
print ('you flipped "Tails" a total of', numTails, 'times!')



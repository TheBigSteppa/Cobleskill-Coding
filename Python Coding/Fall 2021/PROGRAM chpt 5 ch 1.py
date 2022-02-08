# Mark Fraser
# Create a program that prints a list of words in random order.
# The program should print all the words and not repeat any
####################

import random

# list of vars for this program

wordList = ""       # list of words to be put in random order
wordLen = ""        # the length of items in the list
randIndex = ""      # random interger choosen to represent random word
randWord = ""       # random word choosen from the list based on randIndex 

print("""

\tWelcome to the random word generator
\tthis program will put a list of words in random order!
\twithout using the "random.choice()" function lol..

""")

input("Press enter to get started!\n")

wordList = [
    "This",
    "is",
    "the",
    "correct",
    "order",
    ]

print("The list of unrandomized words are:")

for i in wordList:
    print("\t", i)

wordLen = len(wordList)

#print("DEBUG::", wordLen)
#wordNum = random.randint(0, len(wordList)-1)
#randWord = (wordList[wordNum])

#print("DEBUG::", wordNum)
#print("DEBUG::", randWord)


input("\nPress enter to see the random words\n")

print("The randomized list of words are:")
while wordLen > 0:
    randIndex = random.randint(0, len(wordList)-1)
    randWord = (wordList[randIndex])
    print("\t",randWord)
    del wordList[randIndex]
    wordLen -= 1

input("\nThanks for playing, press enter to quit.")
    




#junk v



#    wordNum
 #   print(randWord)
    #del (wordList[wordNum])
  #  wordList.remove(randWord)





#for i in wordList:
 #   print(randWord)
  #  wordList.remove(randWord)

    #randWord = (wordList[wordNum])
   # print(randWord)
   #print(wordList[wordNum])
   #wordList.remove(randWord)
    

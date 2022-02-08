# Mark Fraser
# Word Jumble V2
# pg213
# word.remove

import random

# =-=-=-=-=Definitions=-=-=--=-=-
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
            response = (input(Question))
        except ValueError as e:
            print("\nNOT A VALID ENTRY, TRY AGAIN\n")
            VALID = 1
        else:
            break
    return response

def welcome():
    # This Displays the welcome screen
    print("""
                U  ___ u   ____     ____            _      _   _   __  __     ____     _     U _____ u 
 __        __    \/"_ \/U |  _"\ u |  _"\        U |"| uU |"|u| |U|' \/ '|uU | __")u  |"|    \| ___"|/ 
 \"\      /"/    | | | | \| |_) |//| | | |      _ \| |/  \| |\| |\| |\/| |/ \|  _ \/U | | u   |  _|"   
 /\ \ /\ / /\.-,_| |_| |  |  _ <  U| |_| |\    | |_| |_,-.| |_| | | |  | |   | |_) | \| |/__  | |___   
U  \ V  V /  U\_)-\___/   |_| \_\  |____/ u     \___/-(_/<<\___/  |_|  |_|   |____/   |_____| |_____|  
.-,_\ /\ /_,-.     \\     //   \\_  |||_         _//    (__) )(  <<,-,,-.   _|| \\_   //  \\  <<   >>  
 \_)-'  '-(_/     (__)   (__)  (__)(__)_)       (__)        (__)  (./  \.) (__) (__) (_")("_)(__) (__) 


\t\t\t\tBy: Mark Fraser

""")

def instruc():
    #This displays the instructions
    input("""
\n\n\t\t\tThe goal of this game is to guess the jumbled word
\t\t\tthat the computer chooses randomly from a file.
\t\t\tThose who complete the list get a
\t\t\tCOMPLEMENTARY BOTTLE OF WHISKEY!!!!!!
\n\t\t\tthere are 10 words in total and the topic is:

\t\t\t\t\tUpstate New York

\t\t\t Press enter when you are ready to play.

""")

def listWords():
    # takes each word from our external tuple and place them in a list
    # turns each word from each line into a var.(word)
    WORDS = []
    # KLS: read the first word and check the length.
    # this allows you to make sure there is word there and not blanks.
    word = theFile.readline().replace("\n", "")
    # This variable is blank thus its creating blanks in my list when my list is less than 10.
    #for i in range(10):                       # 10 is my length
    # KLS: while there are words in the file and not blanks.
    while len(word) > 0:
        WORDS.append(word)
        word = theFile.readline().replace("\n", "")
        # THANK YOU PROFESSOR!!!!!!!
    return WORDS
        

def keepPlaying():
    # This def contains the game it runs loops until the words in the txt file are finished
    print("GoodLuck!!!\n")
    theFile.close()
    keepPlaying = True
    try: #will handle IndexError exception, if there are no characters in text file itll prompt the user and cleanly close
        while keepPlaying:
            word = random.choice(WORDS)
            correct = word
            WORDS.remove(correct)
            #print("DEBUG::",correct)
            jumble = ""
            while word:
                position = random.randrange(len(word))  #Changes the position of letters to effectively jumble the words
                jumble += word[position]                # places the neew jumbled word in the var.(jumble)
                word = word[:position] + word[(position + 1):]
            print("The jumble is:", jumble)
            guess = ask_user("\nYour guess: ")
            while guess != correct and guess != None:
                print("Yeah... no, try again")
                guess = ask_user("Your guess: ")
            if guess == correct:
                print("\nAyeee you did it\n")               #removes the correctly guessed word from the list/tuple
                #print("DEBUG::",WORDS)
            if len(WORDS)== 0: #if user finishes all words they get their prize
                print("\nCongrats you've finished all the words!!!")
                print("Thanks for playing!!! You have earned yourself a bottle of whiskey")
                print("""

                                                                                                                        
                                  ░░▓▓██▓▓           
                                  ░░▓▓▓▓▓▓         
                                  ░░████▓▓         
                                ▓▓▓▓▒▒██▓▓██       
                                    ▓▓▓▓▓▓                                                                       
                                  ░░▓▓░░▓▓           
                                ▓▓██▓▓▓▓██▓▓       
                                ▓▓▓▓▓▓▒▒▒▒██      
                                ▓▓▓▓▓▓▒▒░░██      
                                ░░░░▓▓▒▒▓▓░░                
                                ▓▓▓▓▒▒▒▒▒▒██      
                              ▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓    
                            ░░▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓░░  
                            ▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓██    
                            ██▓▓▓▓▒▒▒▒▒▒▓▓▓▓▒▒██                     
                            ▓▓▓▓▓▓▒▒▒▒▒▒▓▓▓▓▒▒██    
                            ██▒▒▓▓▒▒▒▒▒▒▒▒▓▓▒▒██  
                            ████▓▓▓▓▓▓██▓▓▓▓▓▓▓▓  
                            ████░░░░░░░░░░░░████    
                            ██░░▓▓██████████▒▒██  
      ██████████████████    ██████▓▓░░░░░░████▓▓  
      ██            ░░██    ██████▓▓██████▓▓▓▓██  
      ██      ░░      ██    ██▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓██  
      ██      ░░░░  ░░██    ████░░░░░░░░░░▒▒████   
      ██▒▒▒▒▒▒▒▒░░▒▒▒▒██    ████████▓▓██████████   
      ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓██    ████▒▒░░░░░░▒▒▒▒████   
      ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓██    ██▓▓▓▓▓▓▓▓▒▒▒▒▒▒▓▓██     
        ██████▓▓▓▓██▓▓        ████▓▓██████████       
                                    
                                                                                                                        
                                                                                                                

    """)
                input("\n\nPress ENTER to quit and have a great Christmas!")
                writeFile = openFile("words to jumble.txt", "w")
                for i in range(len(WORDS)): #this writes back any remaining words back to the file
                    writeFile.write(WORDS[i])
                    writeFile.write("\n")
                break
            else:
                runItBack = input("Would you like to contiune playing? y/n: ")
                if runItBack == "n":
                    keepPlaying = False
                    print("\nOK =( I saved your progress so you may continue when you get back =)")
                    input("\nPress enter to be a quitter")
                    #WORDS.append(correct) # OLD:: how do i append more than one removed word???????
                    writeFile = openFile("words to jumble.txt", "w")
                    for i in range(len(WORDS)):
                        writeFile.write(WORDS[i])
                        writeFile.write("\n")
                        #print("DEBUG::",WORDS)
                else:
                    keepPlaying = True
    except IndexError as e:
        print("\ncheck your .txt file, it may be blank\n")
        print('"',e,'"',sep='')
        input("\npress enter to quit")

def main():
    welcome()
    instruc()
    listWords() 
    keepPlaying()





# =-=-=-=-=Varibles=-=-=--=-=-
theFile = openFile("words to jumble.txt", "r")
writeFile = ''
WORDS = listWords()



#print(WORDS)

main()

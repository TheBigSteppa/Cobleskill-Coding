def GuessLoop ():
    #replay = ""
    #tries = 1
    play = True
    while play == True:
        rando = random.randint(low, high)
        print("DEBUG::",rando)
        guess = ask_user("Guess???")
        tries = 1
        while guess != rando and tries != 10:
            if guess > rando:
                print("too high")
            elif guess < rando:
                print("too low")
            guess = ask_user("Guess again: ")
            tries +=1
            print("DEBUG::",tries)
            print("DEBUG::",rando)
        if guess == rando:
            print("Ayeee big winner, it only took you",tries,"tries")
        if tries == 10:
            print("MAx amount of tries, the number was",tries)
        replay = input("would you like to play again? y/n: ")
        #print(replay)
        if replay == "y":
            print(replay)
            play = True
        else:
            play = False


#==========================================

def GuessLoop():
    play = True
    while play == True:
        rando = random.randint(low, high)
        print(rando)
        guess = ask_user("What is your guess?: ")
        tries = 0
        while guess != rando and tries !=10:
            if guess > rando:
                print("\nToo high\n")
            if guess < rando:
                print("\nToo low\n")
            guess = ask_user("Try again: ")
            tries += 1
        if guess == rando:
            print("ayye")
        elif tries == 10:
            print("aww")
        break
    replay = input("Would you like to play again?: ")
    while replay == ("y"):
        play = True
        if not play == False: break


#==============================================

def GuessLoop():
    play = True
    while play == True:
        rando = random.randint(low, high)
        print(rando)
        guess = ask_user("What is your guess?: ")
        tries = 0
        while guess != rando and tries !=10:
            if guess > rando:
                print("\nToo high\n")
            if guess < rando:
                print("\nToo low\n")
            guess = ask_user("Try again: ")
            tries += 1
        while guess == rando:
            print("ayeee")
            if not tries == 10:
                print("aww")
                break
        replay = input("Would you like to play again?: ")
        print(replay,play)
        while replay == ("n"):
            print(replay,play)
            play = False
            if not play == True: break

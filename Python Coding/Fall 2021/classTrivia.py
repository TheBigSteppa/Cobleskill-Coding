# trivia program
import sys

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

def nextLine (theFile):
    # return the next line from the trivia file
    line = theFile.readline()
    line = line.replace("/", "\n")
    return line

def welcome(title):
    # welcome the player and read their name
    print ("\t\tWelcome to The Trivia Challenge\n")
    print ("\t\tTopic: ", title, "\n")

def nextBlock (theFile):
    # return the next block of trivia
    category = nextLine(theFile)
    question = nextLine(theFile)

    answers = []
    for i in range(MAX_ANSWERS):
        answers.append(nextLine(theFile))

    correct = nextLine(theFile)
    if correct:
        correct = correct[0]

    explanation = nextLine(theFile)
    return category, question, answers, correct, explanation
        

MAX_ANSWERS = 4
score = 0
theFile = openFile("triviaInput.txt", "r")
title = nextLine(theFile)
welcome(title)

# read the first block of data
category, question, answers, correct, explanation = nextBlock(theFile)

# while category is not null (there is data in the file)
while category:
    # print the category, the question and the 4 answers
    print ("category: ", category)
    print ("question: ", question)
    for i in range(MAX_ANSWERS):
        print ("\t", i+1, "-", answers[i])
        
    # ask the user for their answer
    answer = input ("what is your answer...")

    # check their answer
    if answer == correct:
        print ("BINGO!", end=" ")
        score +=1
    else:
        print ("NOT!", end=" ")

    # print the explanation and their score
    print (explanation)
    print ("score: ", score, "\n\n")

    # read the first block of data
    category, question, answers, correct, explanation = nextBlock(theFile)

# no more data to print...wrap it up
theFile.close()
print("no more questions.  you correctly answered ", score)

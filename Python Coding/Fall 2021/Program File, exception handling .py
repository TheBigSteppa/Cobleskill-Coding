# This program reads a list of inventory items from a data file
# The uses is asked which item to delete

# Your assignment is to add exception handling to this program.
# 1. Add exception handling where there might be an "IndexError" exception
# 2. Add exception handling where there might be a "FileNotFountError" exception
# Be sure to demonstrate that you are catching these specific errors and
#   any other general errors

import sys

# opens file for user // Will handle error the exception "IOError"
def openFile(fileName, mode):
    try:
        theFile= open(fileName, mode)
    except IOError as e:
        print ("unable to open the file ", fileName, "\nKilling the program.\n", e)
        input ("\n\nPress enter to exit")
        sys.exit()
    else:
        return theFile

        
# ask the user for an item number // Will also handle an exception "ValueError"
def ask_for_an_item (question) :
    # asks a question and returns the response
    try:
        response = int(input(question))
    except ValueError as e:
        print("\nYour entry is not a valid one\n")
        print(e)
        input("\n\n Press enter to quit")
        sys.exit()
    else:
        return response


# print the current inventory
def print_inventory (invnentory):
    # figure out how long the inventory is
    inventoryCount = len(inventory)

    print ("you have ", inventoryCount,  "items")
    print ("inventory :")
    for i in range(0,inventoryCount):
      print ("\t", i+1, " - ",inventory[i])

# read the contents of a file into a list
def read_inventory(fileToRead):
    return fileToRead.readlines()
#========== Varibles ============

theFile = openFile("InputForChapter7.txt", "r")


# =========  MAIN ===============

# open the file for reading -- OLD:// # fileToRead = open("InputForChapter7.txt", "r")
fileToRead = openFile("InputForChapter7.txt", "r")


# read the contents of the file into my list
inventory = read_inventory(fileToRead)

# print the inventory
print_inventory(inventory)

# ask the user for an item number to delete
itemToDelete = ask_for_an_item ("Enter the item number to be deleted: ")

# adjust the number for 0-based list
itemToDelete -= 1

# delete the requested item from the list
del inventory[itemToDelete]

# print the revised inventory
print_inventory(inventory)





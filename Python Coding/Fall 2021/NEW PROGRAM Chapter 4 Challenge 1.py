# Mark Fraser
# Write a program that counts for the user. let the user enter the starting number,
# the ending number, and the amount by which to count

#intro to program
print("""


░█████╗░░█████╗░██╗░░░██╗███╗░░██╗████████╗███████╗██████╗░░░░██████╗░██╗░░░██╗
██╔══██╗██╔══██╗██║░░░██║████╗░██║╚══██╔══╝██╔════╝██╔══██╗░░░██╔══██╗╚██╗░██╔╝
██║░░╚═╝██║░░██║██║░░░██║██╔██╗██║░░░██║░░░█████╗░░██████╔╝░░░██████╔╝░╚████╔╝░
██║░░██╗██║░░██║██║░░░██║██║╚████║░░░██║░░░██╔══╝░░██╔══██╗░░░██╔═══╝░░░╚██╔╝░░
╚█████╔╝╚█████╔╝╚██████╔╝██║░╚███║░░░██║░░░███████╗██║░░██║██╗██║░░░░░░░░██║░░░
░╚════╝░░╚════╝░░╚═════╝░╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝╚═╝░░░░░░░░╚═╝░░░

By: Mark Fraser

""")
print(input("This is a program that'll count for youuu \nbased on the numbers that YOUUU enter!\nPress enter to get started"))


numStart = ""
numEnd = ""
numInterval = ""


#First selection
numStart = int(input("\nEnter your 1st NUMBER here. "))
#print("DEBUG::",numOne)
numEnd = int(input("\nNow, enter your 2nd NUMBER here (make it higer than your first). "))
if numEnd <= numStart:
    print("\nNo breaking the program, START OVER!")
    #print("DEBUG::", numEnd)
else:
    numInterval = int(input("\nFinally, How would you like to count?\n(P.S. use a negative num to count backwards) "))
    print(input("\nSo, your Starting point is "+str(numStart)+", your ending point is "+str(numEnd)+", and how you would like to count is by "+str(numInterval)+"s.\n Press enter to get started."))
    # This for loop does all the counting for the user based on peripherals 

    for i in range(numStart, numEnd, numInterval):
        print(i, end=" ")
    if numInterval < 0: #This is the change I made to allow the program to count backwards
        for i in range(numEnd, numStart, numInterval):
            print(i, end=" ")
            

        
print(input("\nThanks for playing! Enter to quit"))

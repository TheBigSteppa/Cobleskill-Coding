# Mark Fraser
# Python3 program to find number of days
# between two given dates

from datetime import date

def intro():
    # This prints the intro
    print("""
▓█████▄  ▄▄▄     ▓██   ██▓  ██████     ▄████▄   ▄▄▄       ██▓     ▄████▄   █    ██  ██▓    ▄▄▄     ▄▄▄█████▓ ▒█████   ██▀███  
▒██▀ ██▌▒████▄    ▒██  ██▒▒██    ▒    ▒██▀ ▀█  ▒████▄    ▓██▒    ▒██▀ ▀█   ██  ▓██▒▓██▒   ▒████▄   ▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒
░██   █▌▒██  ▀█▄   ▒██ ██░░ ▓██▄      ▒▓█    ▄ ▒██  ▀█▄  ▒██░    ▒▓█    ▄ ▓██  ▒██░▒██░   ▒██  ▀█▄ ▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒
░▓█▄   ▌░██▄▄▄▄██  ░ ▐██▓░  ▒   ██▒   ▒▓▓▄ ▄██▒░██▄▄▄▄██ ▒██░    ▒▓▓▄ ▄██▒▓▓█  ░██░▒██░   ░██▄▄▄▄██░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄  
░▒████▓  ▓█   ▓██▒ ░ ██▒▓░▒██████▒▒   ▒ ▓███▀ ░ ▓█   ▓██▒░██████▒▒ ▓███▀ ░▒▒█████▓ ░██████▒▓█   ▓██▒ ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒
 ▒▒▓  ▒  ▒▒   ▓▒█░  ██▒▒▒ ▒ ▒▓▒ ▒ ░   ░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▒░▓  ░░ ░▒ ▒  ░░▒▓▒ ▒ ▒ ░ ▒░▓  ░▒▒   ▓▒█░ ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░
 ░ ▒  ▒   ▒   ▒▒ ░▓██ ░▒░ ░ ░▒  ░ ░     ░  ▒     ▒   ▒▒ ░░ ░ ▒  ░  ░  ▒   ░░▒░ ░ ░ ░ ░ ▒  ░ ▒   ▒▒ ░   ░      ░ ▒ ▒░   ░▒ ░ ▒░
 ░ ░  ░   ░   ▒   ▒ ▒ ░░  ░  ░  ░     ░          ░   ▒     ░ ░   ░         ░░░ ░ ░   ░ ░    ░   ▒    ░      ░ ░ ░ ▒    ░░   ░ 
   ░          ░  ░░ ░           ░     ░ ░            ░  ░    ░  ░░ ░         ░         ░  ░     ░  ░            ░ ░     ░     
 ░                ░ ░                 ░                          ░                                                            

                                                              ░░                          
                                                    ▒▒▓▓▓▓██▓▓▓▓                        
                                                    ▒▒░░░░░░░░░░                        
                                                    ▒▒░░▒▒▓▓░░░░                        
                                                    ▒▒░░░░▓▓░░░░                        
                                                    ▒▒░░▒▒▓▓▒▒░░                        
                                                    ▒▒░░░░░░░░░░                        
                                                    ░░
                                                    

                         ▄▄▄▄ ▓██   ██▓    ███▄ ▄███▓ ▄▄▄       ██▀███   ██ ▄█▀     █████▒
                        ▓█████▄▒██  ██▒   ▓██▒▀█▀ ██▒▒████▄    ▓██ ▒ ██▒ ██▄█▒    ▓██   ▒ 
                        ▒██▒ ▄██▒██ ██░   ▓██    ▓██░▒██  ▀█▄  ▓██ ░▄█ ▒▓███▄░    ▒████ ░ 
                        ▒██░█▀  ░ ▐██▓░   ▒██    ▒██ ░██▄▄▄▄██ ▒██▀▀█▄  ▓██ █▄    ░▓█▒  ░ 
                        ░▓█  ▀█▓░ ██▒▓░   ▒██▒   ░██▒ ▓█   ▓██▒░██▓ ▒██▒▒██▒ █▄   ░▒█░    
                        ░▒▓███▀▒ ██▒▒▒    ░ ▒░   ░  ░ ▒▒   ▓▒█░░ ▒▓ ░▒▓░▒ ▒▒ ▓▒    ▒ ░    
                        ▒░▒   ░▓██ ░▒░    ░  ░      ░  ▒   ▒▒ ░  ░▒ ░ ▒░░ ░▒ ▒░    ░      
                         ░    ░▒ ▒ ░░     ░      ░     ░   ▒     ░░   ░ ░ ░░ ░     ░ ░    
                         ░     ░ ░               ░         ░  ░   ░     ░  ░              
                              ░░ ░
""")

def Instructions():
    print("""
\t\t This Calculator will calculate the number of days between 2 dates
\t\t The format used for this calulator is:
\t\t\t\t\t\t >>YYYY/MM/DD<<
\t\t This application will also calulate the seconds, minutes, hours, weeks, months, and years! 
""")
    input("press Enter to get started\n")

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
 
def numOfDays(date1, date2):
# Calculates number of days by subtracting the dates given by the user
    return (date2-date1).days

def userInput():
# Takes user input for the year, month, and days.
    # This while loop allows the user to confirm the dates, if they have an objection they can run it back from the top
    confirmLoop = True
    while confirmLoop == True:
        y1  = ask_user("Enter the year of the first date(yyyy): ")
        
        # This while loop stops the user from entering silly years lol
        while y1 < 999 or y1 > 9999:
            print("\n\tAre you a time traveler? What buisness do you have in the year",y1,end="?\n")
            print("\tPlease use years from 999 to 9999 McFly")
            y1  = ask_user("\nEnter the year of the first date(yyyy): ")
            
        # This while loop stops the user from entering silly months lol    
        m1 = ask_user("\nEnter the Month of the first date(M): ")
        while m1 >= 13 or m1 <= 0:
            print("\n\tI don\'t know what planet you're from, but on earth, there are only 12 months")
            print("\tNot",m1,"or whatever you put")
            m1 = ask_user("\nEnter the Month of the first date(M): ")
            
        # This while loop stops the user from entering silly days lol
        d1   = ask_user("\nEnter the Day of the first date(D): ")
        while d1 >= 32 or d1 <= 0:
            print("\n\tWhat month has",d1,"days in it? This a days calendar for EARTHHHHHHH\n")
            d1 = ask_user("Enter the Month of the first date(D): ")
            
        #This is the format that python uses to calculate dates (YYYY/MM/DD)
        date1 = date(y1, m1, d1,)
        print("\n\tThe first date you entered is",date1)

        #This allows the "confirmLoop" to loop if the user chooses to do so (by inputting n, if the user presses y the loop stops and continues) 
        Cc = input("\tis this correct? y/n: ")
        if Cc == "n":
            confirmLoop = True
            input("\n\tOk, press enter to Enter the First Date again\n")
        else:
            confirmLoop = False
            input("\n\tAwesome, press enter proceed to the second date\n")
        
    confirmLoop2 = True
    while confirmLoop2 == True:
        y2  = ask_user("Enter the year of the second date(yyyy): ")
        while y2 < 999 or y2 > 9999:
            print("\n\tAre you a time traveler? What buisness do you have in the year",y2,end="?\n")
            print("\tPlease use years from 999 to 9999 McFly")
            y2  = ask_user("\nEnter the year of the first date(yyyy): ")
            
        m2 = ask_user("\nEnter the month of the second date(M): ")
        while m2 >= 13 or m2 <= 0:
            print("\n\tI don\'t know what planet you're from, but on earth, there are only 12 months")
            print("\tNot",m2,"or whatever you put")
            m2 = ask_user("\nEnter the Month of the first date(M): ")
            
        d2   = ask_user("\nEnter the Day of the second date(D): ")
        while d2 >= 32 or d2 <= 0:
            print("\n\tWhat month has",d2,"days in it? This a days calendar for EARTHHHHHHH\n")
            d2 = ask_user("Enter the Month of the first date(D): ")

        date2 = date(y2, m2, d2)
        print("\n\tThe first date you entered is",date2)
        Cc2 = input("\tis this correct? y/n: ")
        if Cc2 == "n":
            confirmLoop2 = True
            input("\n\tOk, press enter to Enter the Second Date again\n")
        else:
            confirmLoop2 = False
            input("\n\tAwesome, press enter begin calculating the days between your dates\n")
            
    #print("DEBUG::",y1, m1, d1, y2, m2, d2, date1, date2)
    return y1, m1, d1, y2, m2, d2

def calaMath(y1, m1, d1, y2, m2, d2):
    # turns the user input into a varible so calculations are done easier
    date1 = date(y1, m1, d1)
    date2 = date(y2, m2, d2)
    DAY = numOfDays(date1, date2)
    SECONDS = DAY * 86400
    MINUTES = DAY * 1440
    HOUR = DAY * 24
    WEEK = DAY / 7
    MONTH = DAY * 0.032855
    YEAR = DAY / 365
    print("There are \"",DAY, "\" days between \"",date1,"\" and \"",date2,"\"\n",sep='')
    print("I also calulated the seconds, minutes, hours, weeks, and years!")
    input("Press Enter to see =)")
    print("\tThat is \"",SECONDS,"\" seconds",sep='',end='!\n')
    print("\tThat is \"",MINUTES,"\" minutes",sep='',end='!\n')
    print("\tThat is \"",HOUR,"\" hours",sep='',end='!\n')
    print("\tThat is \"",WEEK,"\" weeks",sep='',end='!\n')
    print("\tThat is \"",MONTH,"\" months",sep='',end='!\n')
    print("\tThat is \"",YEAR,"\" years",sep='',end='!\n') 

def main():
    intro()
    Instructions()
    goAgain = True
    while goAgain == True:
        y1, m1, d1, y2, m2, d2 = userInput()
        calaMath(y1, m1, d1, y2, m2, d2)
        Cc3 = input("\nWould you like to play again? y/n: ")
        if Cc3 == "n":
            goAgain = False
            input("""
 ▄▀▀█▄▄   ▄▀▀█▀▄    ▄▀▀▄ ▀▄  ▄▀▀▀▀▄        ▄▀▀█▄▄   ▄▀▀▀▀▄   ▄▀▀▄ ▀▄  ▄▀▀▀▀▄   
▐ ▄▀   █ █   █  █  █  █ █ █ █             ▐ ▄▀   █ █      █ █  █ █ █ █         
  █▄▄▄▀  ▐   █  ▐  ▐  █  ▀█ █    ▀▄▄        █▄▄▄▀  █      █ ▐  █  ▀█ █    ▀▄▄  
  █   █      █       █   █  █     █ █       █   █  ▀▄    ▄▀   █   █  █     █ █ 
 ▄▀▄▄▄▀   ▄▀▀▀▀▀▄  ▄▀   █   ▐▀▄▄▄▄▀ ▐      ▄▀▄▄▄▀    ▀▀▀▀   ▄▀   █   ▐▀▄▄▄▄▀ ▐ 
█    ▐   █       █ █    ▐   ▐             █    ▐            █    ▐   ▐         
▐        ▐       ▐ ▐                      ▐                 ▐                  
                                                                               
Watch our for the closing doors on your way out
(Press enter to close the app)""")
        else:
            goAgain = True

# =-=-=-= Main =-=-=-=-=

main()

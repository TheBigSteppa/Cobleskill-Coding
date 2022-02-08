# Mark Fraser
# Chapter 2 Challenge 4
# This is a program for a car dealership that will do all of the math for you
# it also collects user data to create a personal connection
# also, added some ASCII art for cool reasons lol


print("""

███    ███  █████  ██████  ██   ██ ███████                                 
████  ████ ██   ██ ██   ██ ██  ██  ██                                      
██ ████ ██ ███████ ██████  █████   ███████                                 
██  ██  ██ ██   ██ ██   ██ ██  ██       ██                                 
██      ██ ██   ██ ██   ██ ██   ██ ███████                                 
                                                                           
                                                                           
██████  ███████  █████  ██      ███████ ██████  ███████ ██   ██ ██ ██████  
██   ██ ██      ██   ██ ██      ██      ██   ██ ██      ██   ██ ██ ██   ██ 
██   ██ █████   ███████ ██      █████   ██████  ███████ ███████ ██ ██████  
██   ██ ██      ██   ██ ██      ██      ██   ██      ██ ██   ██ ██ ██      
██████  ███████ ██   ██ ███████ ███████ ██   ██ ███████ ██   ██ ██ ██       Located in Cobleskill, NY
                                                                           
                                                                           """)
print("This provided tool will give you a rough estimate on your \nvehicle's purchase price, \nas well as label all additonal fees and Taxes.")
input("\nPress the ENTER key to get started")

print("""_______________________________________________________________________________________""")

userName = input("\nFirst things first, what is your name? ==> ") #user will enter their name here
carName = input("Second, what is the name of the car you plan on purchasing? ==> ")

print("""_______________________________________________________________________________________""") #makes it look neat and organized lol 

print("\nGreat! nice to meet you", userName +"!")
print("We will make sure we get a",carName,"in your driveway pronto!!!")
input("\nPress ENTER to continue to the fees disclaimer")

print("""_______________________________________________________________________________________""")

print("\nAs stated previously, this tool is desgined to help you figure out the FINAL price of the",carName,"you wish to buy.")
print("these MANDATORY fees that are added to all car purchases are the following:")
input("\npress ENTER to see the numbers") #These are based on state and nation averages

print("""_______________________________________________________________________________________""")

print("""\n\t    NY state Taxes ==>               8% (added after fees)
            Registration ==>                 $47 
            license ==>                      $25
            dealer fees ==>                  $500 (hey, we have to eat too lol)
            destination charge ==>           $1000
            and your extended warranty!! ==> $3000 (not a scam)
            """)

print("""_______________________________________________________________________________________""")

input("Press ENTER to get started")

print("\nFirst, Enter the base price of the", carName,"you wish to purchase, \n(non entry or using letters will result in an error.)")
carPrice = input("Enter only the BASE price of your "+carName+".==> ")
carPrice = float(carPrice)

print("""_______________________________________________________________________________________""")

print("Great! \n"+userName+", the",carName,"you would like to buy has a base price of $",carPrice,".")
input("to see the price before taxes, press ENTER")

print("""_______________________________________________________________________________________""")

print("\nWith all the fees added,and before taxes, you are looking at")

carPrice = carPrice+47+25+500+1000+3000

print("\t\t$",carPrice)

print("""_______________________________________________________________________________________""")

input("Press ENTER to add sales Tax")

nyTax = carPrice*.08
carPrice = nyTax+carPrice
#debug to check if tax math works
#print(nyTax)

print("""_______________________________________________________________________________________""")

print("\nWith your taxes being")
print("$",nyTax)
print("the total price of your car comes out to be")
print("$",carPrice)

print("""_______________________________________________________________________________________""")

input("ENTER to conclude tool use")


print("\n\nThis is the end of Mark's dealership tool!")
print("to reuse this tool please restart me,")
print("If not, I wish you a great day",userName+".")
print("and we hope you do get your",carName,"today!")

input("\nThanks and be safe on your way to our dealership!!!")

print("""




 
           .      ..
   __..---/______//-----.        ((  )
 .".--.```|    - /.--.  =:    ( VROOM! ))  
(.: {} :__L______: {} :__; __--( __- -_= ) 
   *--*           *--*                     
 






""")

input("press Enter to quit")


# Note to Self: create a working code, BACK IT UP!!, THENNNNN MAKE IT COOL!
# I broke this code and spent half an hour trying to figure out why it wouldnt work AFTER I already had had it working
# all because i wanted to get fancy lol

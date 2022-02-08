# Mark fraser
# this program will compute the area/volume of shapes that the user picks from my selection
# ACII art is from google, it just makes my program look cooler lol


#================== Imports ============================================
import sys 

#================== Varibles ===========================================
PI = 3.14159265359 # PIE down to the 11th decimal 
FRONT = 0   # n/a
SWITCH = 0  # Var responsible for switching between the different functions
response = ""
L = "" # Length
W = "" # Width
D = "" # Depth/Height
A = "" # Area
V = "" # Volume
radius = "" #wait for it... radius lol
    
#================= Var End ================================================


# Will print the intro/ main menu
def intro():
    SWITCH = 8 
    print("""
                                            Welcome to my
                                 (                        )             (      
                           (     )\ )           (      ( /(    (        )\ )   
                           )\   (()/(  (   (    )\     )\())   )\   (  (()/(   
                        ((((_)(  /(_)) )\  )\((((_)(  ((_)\  (((_)  )\  /(_))  
                         )\ _ )\(_))_ ((_)((_))\ _ )\  _((_) )\___ ((_)(_))_   
                         (_)_\(_)|   \\ \ / / (_)_\(_)| \| |((/ __|| __||   \  
                          / _ \  | |) |\ V /   / _ \  | .` | | (__ | _| | |) | 
                         /_/ \_\ |___/  \_/   /_/ \_\ |_|\_|  \___||___||___/  

                             ☆.。.:*・°☆.。.:*・°☆.。.:*・°☆.。.:*・°☆        

                                       Calculator() By: Mark \n\n
""")
          
    input("\t\t\t\tPress ENTER to go to make your selection. ")
    return ("Make a selection") 
    


# this ask_users function will take user input in the form of an int
def ask_user(Question):
    VALID = 1
    while VALID == 1:
        try:
            response = int(input(Question))
        except ValueError as e:
            print("NOT A VALID ENTRY, TRY AGAIN")
            VALID = 1
        else:
            break
    return response #this loop is producing "None" after a few exceptions and i have no idea why after tinkering with it for a few hours, the app still functions well so this will just have to stay like this lol

# will find the area of a rectangle
def comp_rec_area(L,W):
    print("""\n\nComputing the area of a rectangle.

                        |--------|
                        |        |
                        |--------|
""")
    SWITCH = 1
    L = ""
    W = ""
    A = ""
    L = ask_user("First, Enter the Lenth: \n")
    W = ask_user("Second, Enter the Width: \n")
    A = L * W
    print ("\tThe Length was \"",L,"\" and, the width was \"",W,".\"",sep='') #i know you are against google but im  against spaces between my commas and i needed to figure it out once and for all lol (Via sep='') 
    print ("\tAfter computing the equation 'Length x Width = Area'")
    print ("\tThe Area of your rectangle is \"",A,".\"\n",sep='')
    input ("Press enter to go back to the main menu")
    

# Will find the volume of a cube
def comp_cube_vol(L,W,D):
    print("""\n\nComputing the Vol of a cube.

                           +--------------+
                          /|             /|
                         / |            / |
                        *--+-----------*  |
                        |  |           |  |
                        |  |           |  |
                        |  |           |  |
                        |  +-----------+--+
                        | /            | /
                        |/             |/
                        *--------------*
""")
    L = ""
    W = ""
    D = ""
    V = ""
    L = ask_user("First, Enter the Length: \n")
    W = ask_user("Second, enter the Width: \n")
    D = ask_user("Lastly, enter the depth: \n")
    V = L * W * D
    print ("\tThe Length was \"",L,",\" the width was \"",W,",\" and the depth was \"",D,".\"",sep='') 
    print ("\tAfter computing the equation 'Length x Width x depth = Volume'")
    print ("\tThe area of your Cube is \"",V,".\"\n",sep='')
    input ("Press enter to go back to the main menu")
    

# Will find the Volume of a circle
def comp_circle_area(radius):
    print("""\n\nComputing the area of a circle.

                             .-""-.
                            /      \  
                           ;        ;
                            \      /
                             '-..-'
""")
    r = ""
    A = ""
    r = ask_user("Please enter the radius of the circle: \n")
    A = (r*r) * PI
    print ("\tThe radius of your circle was \"",r,".\"",sep='')
    print ("\tAfter computing the equation 'PI * (r*r) = Area'")
    print ("\tThe area of your circle is \"",A,".\"",sep='')
    input ("\nPress enter to go back to the main menu")
    

#Will find the Volume of a shpere
def comp_sphere_vol(radius):
    print("""\n\nComputing the volume of a sphere.
                                                                                                                                                                                                                                                                           
                              ▓▓▓▓▓▓▓▓▓▓▓▓                                                                              
                        ░░████░░░░░░░░░░░░████                                                                          
                       ░░██▒▒░░░░░░░░░░░░░░░░░░██                                                                        
                     ░░██▒▒▒▒░░░░░░░░░░░░░░░░░░░░██                                                                      
                     ██▒▒▒▒░░░░░░░░░░░░░░    ░░░░░░██                                                                    
                     ██▒▒▒▒░░░░░░░░░░░░        ░░░░██                                                                    
                   ██▓▓▒▒▒▒░░░░░░░░░░░░        ░░░░░░██                                                                  
                   ██▓▓▒▒▒▒░░░░░░░░░░░░░░    ░░░░░░░░██                                                                  
                   ██▓▓▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░██                                                                  
                   ██▓▓▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░██                                                                  
                   ██▓▓▓▓▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░██                                                                  
                   ██▓▓▓▓▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░██                                                                  
                     ▓▓▓▓▓▓▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░██                                                                    
                     ██▓▓▓▓▓▓▒▒▒▒▒▒▒▒░░░░░░░░░░▒▒▒▒██                                                                    
                     ░░▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░                                                                    
                       ░░▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒██░░                                                                      
                          ░░██▓▓▓▓▓▓▓▓▓▓▓▓▓▓████░░                                                                        
                            ░░░░████████████░░                                                                            
                              ░░░░░░░░░░░░                                                                              
""")
    r = ""
    V = ""
    frac = (4/3)
    r = ask_user("What is the radius: \n")
    V = frac * PI * (r*r*r)
    print ("\tThe radius of your sphere was \"",r,".\"",sep='')
    print ("\tAfter computing the equation '(4/3) * PI * (r*r*r) = Volume'")
    print ("\tThe volume of your sphere is \"",V,".\"",sep='')
    input ("\nPress enter to go back to the main menu")

def user_pick(SWITCH):
    SWITCH = 9
    try:
        SWITCH = int(input("""
\t\t\t\tWith this calculator, you can:\n
\t\t\tCompute the area of a Rectangle = 1
\t\t\tCompute the Volume of a Cube = 2
\t\t\tCompute the area of a circle = 3
\t\t\tCompute the volume of a sphere = 4

\t\t\tOther controls include: \n
\t\t\tMake another selection = 9  
\t\t\tSee the awesome intro again = 8
\t\t\tEnd the program = 0\n

\n\t\t\t\tPick a number to get started: """))
    except ValueError as e:
        print("not a valid entry, try again")
    if SWITCH == 1:
        print(comp_rec_area(L, W))
    elif SWITCH == 2:
        print(comp_cube_vol(L, W, D))
    elif SWITCH == 3:
        print(comp_circle_area(radius))
    elif SWITCH == 4:
        print(comp_sphere_vol(radius))
    elif SWITCH == 9:                  ## Redundant, the program will always loop back to the selection:
        print(user_pick(9))            ## //
    elif SWITCH == 8:
        print(intro())
    elif SWITCH == 0:
        sys.exit()
    else:
        print("Not a selection")
        return SWITCH
    
# ================= MAIN ===========================

def main():
    intro()
    i = 0
    while i < 25:           # this was my solution to making my program loop until the user closes it by entering 0 in the intro/menu
        user_pick(SWITCH)
        i += 1
    return main


#=================================================== 

main()

#print(comp_sphere_vol(20))



# Mark Fraser
# Create a program that gets a message from the user and then
# prints it out backwards

print(input("\t\t\t\\\\\Funny text manipulator\\\\\ \n\nThis program will take any text you input\nand throw it back at you backwards! \npress enter to get started "))

# User input
message = ""

message = str(input("Enter your message.==> "))
#print("DEBUG::", message)

print('Your message is "'+message+'" and it contains "',len(message),'" characters.')
input("Press enter to flip it! ")

# I could not for the LIFE of me remember the way that was taught in class how to print a string backwards T_T
# this came from trying to re-learn it from youtube (video:https://www.youtube.com/watch?v=USw-dS6fHm4)(top comment helped me)
# print (message[::-1])<===== the code I learned from youtube

print (message[::-1])

input ("Press enter to end this program")


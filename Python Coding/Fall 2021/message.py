# need to use the random number functions
#import random
inventory = ''
COUNT = 5

# prompt the user for a message and print that message
for i in range(COUNT):
    inventory += input ("enter your item ==> ")

print ("DEBUG: ", inventory)

# get the length of the message
#high = len(message)
#low = -len(message)

for item in inventory :
    # get a random position in the message
 #   position = random.randrange(low, high)
    
    # prints the single character at this location
  print ("inventory[", item, "] ", inventory(item))
   # print ("message[",position,"] ", message[position])

    #start = i
    #finish = position

  #  print ("message[", start,":",finish,"] ", message[start:finish],"\n")
    
    



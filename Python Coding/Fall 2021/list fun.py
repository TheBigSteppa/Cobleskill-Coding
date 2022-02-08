# create my inventory list
inventory = ["sword","gun","tie","healing potion","shield","boots","armour"]
inventoryCount = len(inventory)

print ("you have ", inventoryCount,  "items")
print ("inventory :")
for item in inventory:
  print ("\t",item)

bonusInventory = ["rocket","shark mounted laser"]
#print (bonusInventory)
inventory += bonusInventory
print (inventory)

inventory.remove("tie")
print (inventory)

specialItem = "homing rocket"
inventory.append(specialItem)
print (inventory)

inventory.sort(reverse=True)
print (inventory)

#inventory[1:3] = ["bow and arrow"]
#print (inventory)

#del inventory [7]
#print (inventory)

#if "tie" in inventory :
#  print ("you are very well-dressed in digi-land.")
#else :
#  print (" you are the slob in the village.")

#start = int(input("enter the index number for start of slice "))
#finish = int(input("enter the index number for end of slice "))

#if start >= inventoryCount :
#  print ("stop being stupid...you will die first")
#elif finish > inventoryCount:
#  print ("still stupid...")
#elif finish <= start :
#  print ("final stupid...")
#else :
#  print ("you have selected ", inventory[start:finish])


                  


# fun with dictionaries

idiotsGuide = {
  "shield" : "the thing you hold up in front to stop the flaming arrows",
  "flaming arrow" : "pointy stick with fire on it",
  "fire" : "the flame stuff",
  "helmet" : "brain bucket",
  "mace" : "club with a spiked orb on the end",
  "trebuchet" : "french for big sling shot",
  "battle ax" : "swings both ways"
  }

print (idiotsGuide)
print (idiotsGuide[2])
print (idiotsGuide["mace"])

myFire = "FIRE".lower()

if myFire in idiotsGuide :
  print (myFire, "...and that means ", idiotsGuide.get(myFire))
else :
  print ("cold weens and beans for dinner")

idiotsGuide["potion"] = "the nyquil of knights"
print (idiotsGuide)

idiotsGuide["fire"] = "OWWWW!"
idiotsGuide["FIRE"] = "big hot fire"
print (idiotsGuide)

del idiotsGuide["fire"]
print (idiotsGuide)

for key in idiotsGuide.keys() :
  print (key)

for value in idiotsGuide.values() :
  print (value)

for item in idiotsGuide.items() :
  print (item)
  

  








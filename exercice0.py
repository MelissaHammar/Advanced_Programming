#TAXI RIDES
try:
    people =int(input("How many people need a ride? "))
except ValueError:
    print("ERROR: integer expected")
    
try:
    max =int(input("How many people can firt in one taxi? "))
except ValueError:
    print("ERROR: integer expected")
  
if people % max==0:  
    rides=people//max 
else: 
    rides=people//max +1

print("number of taxis needed is: " ,rides)
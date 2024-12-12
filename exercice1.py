#Ticket Purchase system
name =input("please enter your name: ")
tickets=0
if name!="VIP":
    try:
        tickets =int(input("how many tickets would you like to buy?"))
    except ValueError:
        print("please enter an integer")
   
    cost= tickets * 15.5
    print("the total cost is: ",cost)
    print("Enjoy your tickets")
else: print("Enjoy your show for free")  
   